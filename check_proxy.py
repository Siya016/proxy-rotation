# import threading
# import queue
# import requests
#
# q = queue.Queue()
# valid_proxies = []
#
# with open("proxy_list.txt","r") as f:
#     proxies = f.read().split("\n")
#     for p in proxies:
#         q.put(p)
#
# def check_proxies():
#     global q
#     while not q.empty():
#         proxy = q.get()
#         try:
#             res= requests.get("http://ipinfo.io/json" ,
#                               proxies={"http": proxy,
#                                         "https": proxy})
#
#         except :
#             continue
#         if res.status_code == 200:
#             print(proxy)
#
# for i in range(10):
#     threading.Thread(target=check_proxies).start()



import threading
import queue
import requests

# Queue to store proxies
q = queue.Queue()

# Read proxy list
with open("proxy_list.txt", "r") as f:
    proxies = f.read().splitlines()  # splitlines() handles newlines better
    for p in proxies:
        if p.strip():  # Skip any empty lines
            q.put(p)

# Function to check proxies
def check_proxies():
    global q
    while not q.empty():
        proxy = q.get()
        try:
            # Make the request to check proxy validity
            res = requests.get("http://ipinfo.io/json",
                               proxies={"http": proxy, "https": proxy},
                               timeout=10)  # Added timeout to avoid hanging indefinitely

            if res.status_code == 200:
                print(f"Proxy {proxy} is working.")
            else:
                print(f"Proxy {proxy} returned status code: {res.status_code}")

        except requests.exceptions.RequestException as e:
            # Catch any request-specific errors (network, SSL, etc.)
            print(f"Failed with proxy {proxy}: {e}")
        finally:
            q.task_done()

# Create a lock for safe printing (optional)
lock = threading.Lock()

# Create threads for concurrent proxy checking
threads = []
for i in range(10):
    thread = threading.Thread(target=check_proxies)
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

print("Proxy checking complete.")


