

## Changelog
---

#### Date : Aug 20 | 2025 

- implented **ThreadPoolExecutor**
    - as perviously script was checking one subdomain at time
    - adding a `ThreadPoolExecutor` can check subdomains in parallel
    - `threads` can be modified , 20 threads refers to scanning up to 20 subdomains in parallel 
    - as for now `threads=20` is set to default
---

- Futures 
    - as python is running in background it does not return immediately 
    - `Futures` holds the promise to return post completion
