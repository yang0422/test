__author__ = 'yang'

import json
import requests

res = None


class HttpRequest:
    def __init__(self, url, param=None):
        self.url = url
        self.param = param

    def http_request(self, method, headers=None):
        global res
        if method.upper() == 'GET':
            res = requests.get(self.url, eval(self.param), headers=headers)
        elif method.upper() == 'POST':
            res = requests.post(self.url, json=eval(self.param), headers=headers)
        elif method.upper() == "DELETE":
            res = requests.delete(self.url, params=eval(self.param),headers=headers)
        elif  method.upper() == "PUT":
            res = requests.put(self.url, json=eval(self.param), headers=headers)
        else:
            print("你的请求方式不对！")

        return res


if __name__ == '__main__':
    url = "http://dm.dev.deepexi.top/activity-center/api/v1/activities/test/719"
    param = {"tenantId":"1da54cd1277d4d5d81ba700bf4fc9275"}
    headers = {"User-Agent": "Mozilla/5.0",
               "Content-Type": "application/json"}
    t = HttpRequest(url, str(param)).http_request("get", headers)
    print(t.json())


