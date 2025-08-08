
import requests


def check_subdomains(domain,payload):
    with open(payload, 'r') as f:

        subdomains = f.read().splitlines() 

        for sub in subdomains: 
            for protocol in ["http","https"]: 

                url = f"{protocol}://{sub}.{domain}"

                try:
                    response = requests.get(url,timeout=2)
                    print(f"[+] {url} - status : {response.status_code}")
                except requests.ConnectionError:
                    print(f"[-] {url} - failed to connect") 
                except requests.Timeout: 
                    print(f"[-] {url} - Request timed out")
    

domain = "google.com"

check_subdomains(domain,"subdomain.txt")