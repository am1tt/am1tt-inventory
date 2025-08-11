
import requests



def load_subdomains(payload_file):
    try:
        with open(payload_file,'r') as f:
            return f.read().splitlines()
    
    except FileNotFoundError:
        print(f"[!] file not found : {payload_file}")
        return []

    

def check_subdomains(domain,payload):

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