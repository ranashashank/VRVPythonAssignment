import re
import csv
from collections import Counter
from datetime import datetime

def analyze_log_file(file_path):
    """
    Analyze log file and extract key security insights.
    """
    # Log parsing with detailed information extraction
    log_entries = []
    ip_requests = Counter()
    endpoint_visits = Counter()
    login_attempts = {}

    # Read and process log file
    with open(file_path, 'r') as file:
        for line in file:
            # Enhanced log parsing
            match = re.search(
                r'(?P<ip>\d+\.\d+\.\d+\.\d+).*"(?P<method>\w+) (?P<endpoint>\S+).*" (?P<status>\d+).*',
                line
            )
            
            if match:
                ip = match.group('ip')
                endpoint = match.group('endpoint')
                status = int(match.group('status'))
                
                # Track IP requests
                ip_requests[ip] += 1
                
                # Track endpoint visits
                endpoint_visits[endpoint] += 1
                
                # Track failed login attempts
                if status == 401 and '/login' in endpoint:
                    login_attempts[ip] = login_attempts.get(ip, 0) + 1

    # Identify suspicious activities
    suspicious_ips = {
        ip: attempts 
        for ip, attempts in login_attempts.items() 
        if attempts > 5  # Configurable threshold
    }

    # Prepare comprehensive report
    report = {
        'top_ips': ip_requests.most_common(5),
        'top_endpoints': endpoint_visits.most_common(3),
        'suspicious_ips': suspicious_ips
    }

    return report

def generate_security_report(report):
    """
    Generate a human-readable security report.
    """
    print("\n=== 🔒 VRV Security Log Analysis Report 🔒 ===")
    
    # Top IP Addresses
    print("\n📍 Top IP Addresses by Request Volume:")
    for ip, count in report['top_ips']:
        print(f"  {ip}: {count} requests")
    
    # Most Visited Endpoints
    print("\n🌐 Most Accessed Endpoints:")
    for endpoint, visits in report['top_endpoints']:
        print(f"  {endpoint}: {visits} visits")
    
    # Suspicious Activity Detection
    print("\n🚨 Suspicious Login Attempts:")
    if report['suspicious_ips']:
        for ip, attempts in report['suspicious_ips'].items():
            print(f"  ALERT: {ip} - {attempts} failed login attempts")
    else:
        print("  No suspicious activities detected.")

def save_report_to_csv(report, filename='security_report.csv'):
    """
    Save analysis results to a CSV file.
    """
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        # IP Requests Section
        writer.writerow(['Top IP Addresses'])
        writer.writerow(['IP', 'Request Count'])
        writer.writerows(report['top_ips'])
        
        # Endpoint Visits Section
        writer.writerow([])
        writer.writerow(['Top Endpoints'])
        writer.writerow(['Endpoint', 'Visits'])
        writer.writerows(report['top_endpoints'])
        
        # Suspicious IPs Section
        writer.writerow([])
        writer.writerow(['Suspicious Login Attempts'])
        writer.writerow(['IP', 'Failed Attempts'])
        writer.writerows(report['suspicious_ips'].items())
    
    print(f"\n💾 Detailed report saved to {filename}")

def main():
    """
    Main execution function for log analysis.
    """
    try:
        # Analyze log file
        log_file = 'sample.log'
        security_report = analyze_log_file(log_file)
        
        # Display report
        generate_security_report(security_report)
        
        # Save to CSV
        save_report_to_csv(security_report)
    
    except FileNotFoundError:
        print(f"Error: Log file '{log_file}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    main()