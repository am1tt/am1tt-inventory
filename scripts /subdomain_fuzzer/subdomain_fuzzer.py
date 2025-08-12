
import requests

from requests.exceptions import ConnectionError, Timeout, InvalidURL, RequestException


def load_subdomains(payload_file):
    try:
        with open(payload_file,'r') as f:
            return f.read().splitlines()
    
    except FileNotFoundError:
        print(f"[!] file not found : {payload_file}")
        return []



def fuzz_subdomain(domain,subdomain): 
    """ Check if a subdomain is alive and return the status"""

    protocols = ["http","https"]

    results = []


    for protocol in protocols:
        url = f"{protocol}://{subdomain}.{domain}"

        try:
            response = requests.get(url,timeout=3)
            results.append(f"[+] {url} - Status : {response.status_code}")
        except ConnectionError: 
            results.append(f"[-] {url} - Failed to Connect")
        except TimeoutError:
            results.append(f"[-] {url} - Request timed out")
        except InvalidURL: 
            results.append(f"[-] {url} - Invalid URL")
        except RequestException as e:
            results.append(f"[-] {url} - Request error : {e} ")
    
    return results





