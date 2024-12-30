import socket
import requests
from bs4 import BeautifulSoup

def scan_network(network):
    # Scan for open ports
    print(f"Scanning network {network} for open ports...")
    for port in range(1, 65535):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)
        result = sock.connect_ex((network, port))
        if result == 0:
            print(f"Port {port} is open")
        sock.close()

def scan_website(url):
    # Scan for outdated software versions and misconfigurations
    print(f"Scanning website {url} for vulnerabilities...")
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Check for outdated software versions
        software_versions = ['WordPress', 'Drupal', 'Joomla']
        for version in software_versions:
            if version in response.text:
                print(f"Outdated {version} version found")
        
        # Check for misconfigurations
        misconfigurations = ['X-Frame-Options', 'X-XSS-Protection', 'X-Content-Type-Options']
        for misconfig in misconfigurations:
            if misconfig not in response.headers:
                print(f"Misconfiguration: {misconfig} not found")
        
        # Check for common vulnerabilities
        vulnerabilities = ['SQL injection', 'Cross-site scripting', 'Directory traversal']
        for vulnerability in vulnerabilities:
            if vulnerability in response.text:
                print(f"Potential {vulnerability} vulnerability found")
    
    except requests.exceptions.RequestException as e:
        print(f"Error scanning website: {e}")

# Example usage
network = '192.168.1.0/24'
scan_network(network)

url = 'https://example.com'
scan_website(url)