
import requests


from requests.exceptions import ConnectionError, Timeout, InvalidURL, RequestException

from concurrent.futures import ThreadPoolExecutor

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
        except Timeout:
            results.append(f"[-] {url} - Request timed out")
        except InvalidURL: 
            results.append(f"[-] {url} - Invalid URL")
        except RequestException as e:
            results.append(f"[-] {url} - Request error : {e} ")
    
    return results


def run_scanner(domain,payload_file,threads=10): 
    """subdomain fuzzer"""

    subdomains = load_subdomains(payload_file)

    if not subdomains: 
        return
    

    with ThreadPoolExecutor(max_workers=threads) as executor: 
        futures = [executor.submit(fuzz_subdomain,domain,sub) for sub in subdomains]

        for future in futures:
            for result in future.result():
                print(result)



if __name__ == "__main__": 
    domain = "example.com"
    payload_file = "subdomain.txt"

    run_scanner(domain,payload_file,threads=10) 