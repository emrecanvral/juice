import os
import requests
import sys

file_name = sys.argv[1]
scan_type = ''

if file_name == 'gitleaks.json':
    scan_type = 'Gitleaks Scan'
elif file_name == 'njsscan.sarif':
    scan_type = 'SARIF'
elif file_name == 'semgrep-results.json':
    scan_type = 'Semgrep JSON Report'
elif file_name == 'zap.xml':
    scan_type = 'ZAP Scan'
elif file_name == 'dependency-check.xml':
    scan_type = 'Dependency Check Scan'
elif file_name == 'greype.json':
    scan_type = 'Anchore Grype'

api_token = os.getenv('SCAN_API_TOKEN')
if not api_token:
    raise ValueError('API token not found in environment variables.')

headers = {
    'Authorization': f'Token {api_token}'
}

url = 'http://34.45.199.182:8080/api/v2/import-scan/'

data = {
    'active': True,
    'verified': True,
    'scan_type': scan_type,
    'minimum_severity': 'Low',
    'engagement': 1
}

files = {
    'file': open(file_name, 'rb')
}

response = requests.post(url, headers=headers, data=data, files=files)

if response.status_code == 201:
    print('Scan results imported successfully')
else:
    print(f'Failed to import scan results: {response.content}')
