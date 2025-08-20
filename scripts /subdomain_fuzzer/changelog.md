

## Changelog
---

#### Date : Aug 20 | 2025 

- implemented **ThreadPoolExecutor**
    - as perviously script was checking one subdomain at time
    - adding a `ThreadPoolExecutor` can check subdomains in parallel
    - `threads` can be modified , 20 threads refers to scanning up to 20 subdomains in parallel 
    - as for now `threads=20` is set to default
---

- Futures 
    - as python is running in background it does not return immediately 
    - `Futures` holds the promise to return post completion


- Fixed : [ ! ] FileNotFound Exception
    - implemented abs self diretory detection
    - it will detect `subdomain.txt` directory if its stored on the current directory the script is running from 

- **Added** : Output save txt
    - saves the terminal output and status in txt file 
    - the file is created automatically and gets stored to the working directory

 
 > Status (Running) script is now in a running state 