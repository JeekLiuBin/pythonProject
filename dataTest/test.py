import requests

if __name__ == '__main__':
    session = requests.session()
    res = session.get('https://ww.baidu.com')
    info_mode = res.status_code
    print(info_mode)
