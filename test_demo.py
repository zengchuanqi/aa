import pytest
import requests


def test_get_token():
    url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
    corpid = 'wwf554c8829cd2e054'
    secret = 'GHIBI-zM6PjZr_SZ1iboGKWN1-IWxCfcXu7ukI-0cXo'
    r = requests.get(url, params={'corpid': corpid,
                                  'corpsecret': secret})
    token = r.json()['access_token']
    print(token)
    return token


def test_member_read():
    url = 'https://qyapi.weixin.qq.com/cgi-bin/user/get'
    r = requests.get(url, params={'access_token': test_get_token(), 'userid': '435435438354'})
    print(r.json())


def test_member_create(userid,name,mobile):
    url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={test_get_token()}'
    data = {
        "userid": userid,
        "name": name,
        "mobile": mobile,
        "department": [2],
    }
    r = requests.post(url, json=data)
    return r.json()

@pytest.mark.parametrize("userid,name,mobile",[("zhansan","xiaobai","17872301002")])
def test_all(userid,name,mobile):
    assert test_member_create(userid,name,mobile)["errmsg"] =="created"


def test_department_create():
    url = f'https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={test_get_token()}'
    data = {
        "name": "afhj",
        "parentid": 1,

    }

    r = requests.post(url, json=data)
    print(r.json())


def test_department_update():
    url = f'https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={test_get_token()}'
    data = {
        "id": 11,
        "name": "Hello",
    }

    r = requests.post(url, json=data)
    print(r.json())


def test_department_delete():
    url = f'https://qyapi.weixin.qq.com/cgi-bin/department/delete?'
    r = requests.get(url, params={'access_token': test_get_token(),
                                  'id': 12})
    print(r.url)
    print(r.json())


def test_department_list():
    url = 'https://qyapi.weixin.qq.com/cgi-bin/department/list?'
    r = requests.get(url, params={'access_token': test_get_token(),
                                  'id': 2})
    print(r.url)
    print(r.json())
