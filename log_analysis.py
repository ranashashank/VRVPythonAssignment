import re
from collections import Counter
import csv

def analyze_ip_requests(log_file_path):
    """
    Analyze IP addresses and their request patterns with detailed categorization.
    """
    # Counters for different IP request types
    total_ip_requests = Counter()
    successful_requests = Counter()
    failed_requests = Counter()
    
    # IP categorization
    unique_ips = set()
    
    try:
        with open(log_file_path, 'r') as file:
            for line in file:
                # Extract IP address
                ip_match = re.search(r'(\d+\.\d+\.\d+\.\d+)', line)
                if not ip_match:
                    continue
                
                ip = ip_match.group(1)
                unique_ips.add(ip)
                
                # Count total requests for each IP
                total_ip_requests[ip] += 1
                
                # Categorize requests by status
                if ' 200 ' in line:
                    successful_requests[ip] += 1
                elif ' 401 ' in line:
                    failed_requests[ip] += 1
    
    except FileNotFoundError:
        print(f"Error: Log file {log_file_path} not found.")
        return None
    
    # Prepare comprehensive IP analysis
    ip_analysis = []
    for ip in unique_ips:
        ip_analysis.append({
            'ip_address': ip,
            'total_requests': total_ip_requests[ip],
            'successful_requests': successful_requests[ip],
            'failed_requests': failed_requests[ip],
            'success_rate': round(successful_requests[ip] / total_ip_requests[ip] * 100, 2) if total_ip_requests[ip] > 0 else 0
        })
    
    # Sort by total requests in descending order
    ip_analysis.sort(key=lambda x: x['total_requests'], reverse=True)
    
    return ip_analysis

def generate_ip_report(ip_analysis):
    """
    Generate a detailed report of IP request analysis.
    """
    print("\n=== Comprehensive IP Request Analysis ===")
    
    for entry in ip_analysis[:10]:  # Top 10 IPs
        print(f"\nIP: {entry['ip_address']}")
        print(f"  Total Requests:      {entry['total_requests']}")
        print(f"  Successful Requests: {entry['successful_requests']}")
        print(f"  Failed Requests:     {entry['failed_requests']}")
        print(f"  Success Rate:        {entry['success_rate']}%")
        
        # Risk classification
        if entry['failed_requests'] > 5:
            print("  POTENTIAL SECURITY RISK")

def save_ip_analysis_to_csv(ip_analysis, filename='ip_request_analysis.csv'):
    """
    Save IP analysis to a CSV file with detailed breakdown.
    """
    try:
        with open(filename, 'w', newline='') as csvfile:
            # Define CSV headers
            fieldnames = [
                'IP Address', 
                'Total Requests', 
                'Successful Requests', 
                'Failed Requests', 
                'Success Rate (%)'
            ]
            
            # Create CSV writer
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            # Write headers
            writer.writeheader()
            
            # Write IP data
            for entry in ip_analysis:
                writer.writerow({
                    'IP Address': entry['ip_address'],
                    'Total Requests': entry['total_requests'],
                    'Successful Requests': entry['successful_requests'],
                    'Failed Requests': entry['failed_requests'],
                    'Success Rate (%)': entry['success_rate']
                })
        
        print(f"\nDetailed IP analysis saved to {filename}")
    
    except IOError:
        print("Error: Unable to write CSV file.")

def main():
    """
    Main execution function for IP request analysis.
    """
    log_file = 'sample.log'
    
    # Analyze IP requests
    ip_analysis = analyze_ip_requests(log_file)
    
    if ip_analysis:
        # Generate console report
        generate_ip_report(ip_analysis)
        
        # Save to CSV
        save_ip_analysis_to_csv(ip_analysis)

if __name__ == '__main__':
    main()