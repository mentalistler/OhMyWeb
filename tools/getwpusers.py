import requests
import useragent
from urllib.parse import urlparse
def send_req(domain):

    response = requests.get(f"{domain}/wp-json/wp/v2/users",headers={'User-agent': useragent.get_useragent()},timeout=15)
    return response.json()

def user_check(domain):
    users = []
    try:
        response = send_req(domain)
        for i in range(len(response)):
            users.append(response[i]["slug"])
        #print(domain,users)
        return users
    except:
        return None
