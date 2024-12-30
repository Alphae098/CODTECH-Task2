# CODTECH-Task2
Name : Alphae P Khristi
Compamy : CODTECH IT Solutions
ID : CT08EWQ
Domain : CYBER ECURITY AND ETHICAL HACKING
Duration : 20/12/2024 to 20/1/2025
Mentor : Neela Santhosh Kumar 

Overview of CODTECH Internship Task 2 : VULNERABILITY SCANNING TOOL
This script is a lightweight tool for performing network and website vulnerability assessments. It includes functionalities for:

Network Scanning:

Scans a specified network range for open ports using a TCP connection test.
Identifies potential entry points on the network.
Website Vulnerability Scanning:

Detects outdated CMS versions such as WordPress, Drupal, and Joomla.
Checks for common misconfigurations in HTTP security headers.
Identifies text patterns suggesting common vulnerabilities (e.g., SQL injection, XSS).
Features
Port Scanning: Iterates through all TCP ports (1–65535) and identifies open ports on a specified network address.
Website Scanning:
Inspects HTTP response headers and page content.
Detects missing or misconfigured headers like X-Frame-Options and X-XSS-Protection.
Identifies potential vulnerabilities or outdated software using keyword matching.
Usage
Replace the network variable with your desired subnet (e.g., '192.168.1.0/24').
Set the url variable to the target website URL (e.g., 'https://example.com').
Run the script using Python:

bash
Copy code
python vulnerability_test.py
Limitations
Port scanning can be slow for large ranges; consider narrowing the range or increasing the timeout duration.
The script doesn't verify findings; it only flags potential issues based on simple pattern matching.
For ethical use only. Do not run this tool on networks or websites without proper authorization.



The output for this code will be in two saperate divisions one for the website and one for the Network

1. Network Scanning Output:

Scanning network 192.168.1.0/24 for open ports...
Port 22 is open
Port 80 is open
Port 443 is open

2. Website Scanning Output:

Scanning website https://example.com for vulnerabilities...
Outdated WordPress version found
Misconfiguration: X-Frame-Options not found
Potential SQL injection vulnerability found
