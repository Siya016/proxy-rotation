# import requests
#
# with open("valid_proxies.txt","r") as f :
#     proxies = f.read().split("\n")
#
# sites_to_check = ["https://books.toscrape.com/",
#                   "https://books.toscrape.com/catalogue/category/books/travel_2/index.html"]
#
# counter = 0
# for site in sites_to_check:
#     try:
#         print(f"Using the proxy: {proxies[counter]}")
#         res = requests.get(site, proxies ={"http": proxies[counter],
#                                            "https":proxies[counter]})
#         print(res.status_code)
#         print(res.text)
#     except:
#         print("Failed")
#     finally:
#         counter += 1
#         counter % len(proxies)

# import requests
#
# # Load proxies from a file
# with open("valid_proxies.txt", "r") as f:
#     proxies = f.read().split("\n")
#
# # List of sites to check
# sites_to_check = [
#     "https://books.toscrape.com/",
#     "https://books.toscrape.com/catalogue/category/books/travel_2/index.html"
# ]
#
# counter = 0  # Proxy index counter
#
# for site in sites_to_check:
#     try:
#         proxy = proxies[counter]
#         print(f"Using the proxy: {proxy}")
#
#         # Make the request using the current proxy
#         res = requests.get(site, proxies={"http": proxy, "https": proxy}, timeout=10,verify=False)
#
#         # Print status and content
#         print(f"Status Code: {res.status_code}")
#         print(res.text)
#     except Exception as e:
#         print(f"Failed with proxy {proxy}: {e}")
#     finally:
#         # Move to the next proxy, loop back to the start if at the end
#         counter = (counter + 1) % len(proxies)


# import requests
# import warnings
#
# # Suppress SSL warnings for unverified requests
# from urllib3.exceptions import InsecureRequestWarning
#
# warnings.simplefilter('ignore', InsecureRequestWarning)
#
# # Load proxies from a file
# with open("valid_proxies.txt", "r") as f:
#     proxies = f.read().split("\n")
#
# # List of sites to check
# sites_to_check = [
#     "https://books.toscrape.com/",
#     "https://books.toscrape.com/catalogue/category/books/travel_2/index.html"
# ]
#
# counter = 0  # Proxy index counter
#
# for site in sites_to_check:
#     try:
#         proxy = proxies[counter]
#         print(f"Using the proxy: {proxy}")
#
#         # Make the request using the current proxy
#         res = requests.get(
#             site,
#             proxies={"http": proxy, "https": proxy},
#             timeout=10,
#             verify=False  # Ignore SSL certificate verification
#         )
#
#         # Print status and content if successful
#         print(f"Status Code: {res.status_code}")
#         if res.status_code == 200:
#             print(res.text)
#         else:
#             print(f"Non-200 Status Code: {res.status_code}")
#     except requests.exceptions.RequestException as e:
#         print(f"Failed with proxy {proxy}: {e}")
#     finally:
#         # Move to the next proxy, loop back to the start if at the end
#         counter = (counter + 1) % len(proxies)


# import requests
# import warnings
# from urllib3.exceptions import InsecureRequestWarning
#
# # Suppress SSL warnings for unverified requests
# warnings.simplefilter('ignore', InsecureRequestWarning)
#
# # Load proxies from a file
# with open("valid_proxies.txt", "r") as f:
#     proxies = [proxy.strip() for proxy in f.readlines() if proxy.strip()]
#
# # List of sites to check
# sites_to_check = [
#     "https://books.toscrape.com/",
#     "https://books.toscrape.com/catalogue/category/books/travel_2/index.html"
# ]
#
# # Test each proxy with all sites
# for proxy in proxies:
#     print(f"\nTesting proxy: {proxy}")
#     for site in sites_to_check:
#         try:
#             print(f"  Using proxy: {proxy} for site: {site}")
#             response = requests.get(
#                 site,
#                 proxies={"http": proxy, "https": proxy},
#                 timeout=10,
#                 verify=False  # Ignore SSL certificate verification
#             )
#
#             if response.status_code == 200:
#                 print(f"  Success! Status Code: {response.status_code}")
#                 print(f"  First 200 characters of the content:\n{response.text[:200]}")
#             else:
#                 print(f"  Non-200 Status Code: {response.status_code}")
#         except requests.exceptions.RequestException as e:
#             print(f"  Failed with proxy {proxy} for site {site}: {e}")
#     print("-" * 50)  # Separator for readability
#
# print("\nAll proxies have been tested.")



import requests
import random
import warnings
from urllib3.exceptions import InsecureRequestWarning

# Suppress SSL warnings for unverified requests
warnings.simplefilter('ignore', InsecureRequestWarning)

# File paths
proxy_file = "valid_proxies.txt"
valid_proxy_file = "valid_proxy1.txt"

# Test URLs
test_urls = [
    "https://books.toscrape.com/",
    "https://books.toscrape.com/catalogue/category/books/travel_2/index.html"
]

# Function to test a single proxy
def test_proxy(proxy, timeout=15):
    proxies = {"http": proxy, "https": proxy}
    for url in test_urls:
        try:
            response = requests.get(url, proxies=proxies, timeout=timeout, verify=False)
            if response.status_code == 200:
                print(f"Proxy {proxy} is valid for {url}")
            else:
                print(f"Proxy {proxy} failed with status code {response.status_code} for {url}")
                return False
        except requests.exceptions.RequestException as e:
            print(f"Proxy {proxy} failed for {url}: {e}")
            return False
    return True

# Filter valid proxies
def filter_proxies(input_file, output_file):
    with open(input_file, "r") as infile, open(output_file, "w") as outfile:
        for proxy in infile:
            proxy = proxy.strip()
            if test_proxy(proxy):
                outfile.write(proxy + "\n")

# Rotate proxies
def rotate_proxies(proxy_file):
    with open(proxy_file, "r") as infile:
        proxies = infile.readlines()
        if not proxies:
            print("No valid proxies available!")
            return None
        return random.choice(proxies).strip()

# Main script
if __name__ == "__main__":
    # Step 1: Filter proxies and save to valid_proxy.txt
    print("Filtering valid proxies...")
    filter_proxies(proxy_file, valid_proxy_file)

    # Step 2: Load valid proxies from the file
    with open(valid_proxy_file, "r") as f:
        proxies = [proxy.strip() for proxy in f.readlines() if proxy.strip()]

    # Step 3: Test each proxy with all sites
    for proxy in proxies:
        print(f"\nTesting proxy: {proxy}")
        for site in test_urls:
            try:
                print(f"  Using proxy: {proxy} for site: {site}")
                response = requests.get(
                    site,
                    proxies={"http": proxy, "https": proxy},
                    timeout=10,
                    verify=False  # Ignore SSL certificate verification
                )

                if response.status_code == 200:
                    print(f"  Success! Status Code: {response.status_code}")
                    print(f"  First 200 characters of the content:\n{response.text[:200]}")
                else:
                    print(f"  Non-200 Status Code: {response.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"  Failed with proxy {proxy} for site {site}: {e}")
        print("-" * 50)  # Separator for readability

    # Step 4: Use valid proxies for requests by rotating
    print("\nRotating proxies for requests...")
    for _ in range(5):  # Example: Make 5 requests
        proxy = rotate_proxies(valid_proxy_file)
        if proxy:
            print(f"Using proxy: {proxy}")
            test_proxy(proxy)

    print("\nAll proxies have been tested.")
