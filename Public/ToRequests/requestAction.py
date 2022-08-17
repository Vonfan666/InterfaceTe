#针对请求封装

import requests,json,urllib3

requests.packages.urllib3.disable_warnings()
class ReqClass(object):
    def __init__(self,url,header=None,data=None):
        self.url=url
        self.header=header
        self.data=data


    def __call__(self, *args, **kwargs):
        return self.run(*args, **kwargs)

    def run(self,method="post"):
        self.method=method
        res=self.isRquests()
        return res

    def isRquests(self):
        if self.method=="get":
            return self.from_get()
        if self.method=="post":
            return self.dataTypeChange()




    def isType(self):
        """判断data数据格式是否为json"""
        try:
            json.loads(self.data)
            return True
        except:
            return False

    def dataTypeChange(self):
        headerType=self.header["Content-Type"]
        if  headerType in  "application/json":
            if  self.isType():
                return self.data_post()
            elif type(self.data) is dict:
                return self.json_post()
            else:
                raise TypeError("数据类型错误")


    def from_get(self):
        return requests.get(url=self.url, params=self.data, verify=False, timeout=30)

    def data_post(self):
        return requests.post(url=self.url, data=self.data, verify=False, timeout=30)

    def json_post(self):
        return requests.post(url=self.url, json=self.data, verify=False, timeout=30)







