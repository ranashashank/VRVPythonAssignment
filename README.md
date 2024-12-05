
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
   - Save results in a CSV file named `ip_request_analysis.csv`.

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
├── ip_analysis.py      # Main Python script for analysis
├── sample.log          # Sample log file to analyze
├── ip_request_analysis.csv  # Generated results (output)
└── README.md           # Documentation
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
   python ip_analysis.py
   ```
3. Check the output:
   - View a detailed report in the terminal.
   - Open the `ip_request_analysis.csv` file for the saved results.

---

## **Expected Output**

### **Terminal Output**
```bash
=== Comprehensive IP Request Analysis ===

IP: 203.0.113.5
  Total Requests:      8
  Successful Requests: 0
  Failed Requests:     8
  Success Rate:        0.0%
  POTENTIAL SECURITY RISK

IP: 198.51.100.23
  Total Requests:      8
  Successful Requests: 8
  Failed Requests:     0
  Success Rate:        100.0%

IP: 192.168.1.1
  Total Requests:      7
  Successful Requests: 7
  Failed Requests:     0
  Success Rate:        100.0%

IP: 10.0.0.2
  Total Requests:      6
  Successful Requests: 6
  Failed Requests:     0
  Success Rate:        100.0%

IP: 192.168.1.100
  Total Requests:      5
  Successful Requests: 0
  Failed Requests:     5
  Success Rate:        0.0%
Detailed IP analysis saved to ip_request_analysis.csv
```
