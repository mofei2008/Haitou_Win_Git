import requests

def get_token():
    host1 = 'https://api.haitoutech.com/haitou-user/user/'
    doc1 = 'loginByMobile'
    url1 = ''.join([host1, doc1])
    data1 = {'mobile': '18610806332',
             'password': 'Aa111111',
             'regionalCode': '+86',
             'userType': '1',
             'clt': 'h5Wealth'}
    r1 = requests.post(url1, data=data1)
    token = r1.json()["data"]
#    print(token)
    return token
