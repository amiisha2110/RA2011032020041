import requests
import json

def fetch_num_from_urls(urls):
    num = []
    for url in urls:
        response = requests.get(url)
        if response.status_code == 200:
            num.extend(response.json()["numb"])
    return num

def main():
    api_endpoints = [
        "http://20.244.56.144/numbers/primes",
        "http://20.244.56.144/numbers/fibo",
        "http://20.244.56.144/numbers/odd",
        "http://20.244.56.144/numbers/rand"
    ]
    
    all_num = fetch_num_from_urls(api_endpoints)
    sorted_num = sorted(set(all_num))
    
    result = {"num": sorted_num}
    print(json.dumps(result))

if __name__ == "_main_":
    main()