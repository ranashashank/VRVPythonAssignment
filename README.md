
# **Python Assignment Intern**

## **Problem Statement**

This script analyzes web server logs to extract meaningful insights. It performs the following tasks:

1. **Comprehensive IP Address Analysis**:
   - Analyze total requests, successful requests, and failed requests per IP address.
   - Categorize each IP's success rate and classify potential security risks based on failed requests.

2. **Risk Classification**:
   - Highlight IP addresses with more than 5 failed requests as potential security risks.

3. **Output Results**:
   - Display a detailed report in the terminal (Top 10 IPs).
   - Save results in a CSV file named `security_report.csv`.

---

## **Log File Format**

The script processes a log file (`sample.log`) with entries in the following format:

```
<IP Address> - - [<Timestamp>] "<HTTP Method> <Endpoint> <Protocol>" <Status Code> <Response Size> ["Failure Message (if any)"]
```

Example:
```
192.168.1.1 - - [03/Dec/2024:10:12:34 +0000] "GET /home HTTP/1.1" 200 512
203.0.113.5 - - [03/Dec/2024:10:12:35 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
```

---

## **Code Overview**

### **File Structure**
```
├── vrv_log_analysis.py  # Main Python script
├── sample.log           # Sample log file for analysis
├── security_report.csv  # Generated report (output)
└── README.md            # Documentation
```


## **How to Run**

### **Requirements**
- Python 3.x installed on your system.

### **Steps**
1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```
2. Run the script:
   ```bash
   python log_analysis.py
   ```
3. Check the output:
   - View a detailed report in the terminal.
   - Open the `security_report.csv` file for the saved results.

---

## **Expected Output**

### **Terminal Output**
```bash
=== 🔒 VRV Security Log Analysis Report 🔒 ===

📍 Top IP Addresses by Request Volume:
  203.0.113.5: 8 requests
  198.51.100.23: 8 requests
  192.168.1.1: 7 requests
  10.0.0.2: 6 requests
  192.168.1.100: 5 requests

🌐 Most Accessed Endpoints:
  /login: 13 visits
  /home: 5 visits
  /about: 5 visits

🚨 Suspicious Login Attempts:
  ALERT: 203.0.113.5 - 8 failed login attempts

💾 Detailed report saved to security_report.csv
```
