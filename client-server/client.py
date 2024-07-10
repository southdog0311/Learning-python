import requests # type: ignore

try:
    response = requests.get('https://yakimhsu.com')
    print('statusCode:', response.status_code)
    print('headers:', response.headers)  # 多印 response 的 header
    print('body:', response.text)
except requests.exceptions.RequestException as e:
    print('error:', e)
