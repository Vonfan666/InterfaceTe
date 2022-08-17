import unittest
from Public.ToRequests.requestAction import ReqClass
from Public.FeilsRead.YamlRead import yamlObj
from Public.ToRequests.decoratorAction import skip_func,returnRunCase
from Config import setting
#全局变量
class  GlobalEnv(object):
    def __init__(self,*args,**kwargs):
        self.args=args
        self.kwargs=kwargs

class GetYamlData(object):
    def __init__(self,name):
        self.__name=name
        self.getYamlData()
    def getYamlData(self):
        if isinstance(self.__name,str):
            self.__obj=yamlObj[self.__name]
        elif isinstance(self.__name,dict):
            self.__obj=self.__name
            print(self.__obj,"___________________________________________")
        else:
            raise Exception("yaml files Data type error")
        self.url=self.__obj["url"]
        self.header=self.__obj["header"]
        self.data=self.__obj["data"]
        self.type=self.__obj["type"]
        self.isAssert=self.__obj["asserDict"]
        self.caseMethodName=self.__obj["caseMethodName"]
#yaml文件导入
# path = os.path.join(os.path.dirname(os.path.dirname(__file__)),"Config",'data.yaml')
#
# with open(path,"r",encoding="utf-8") as  f:
#     yamlObj=yaml.load(f.read(),Loader=yaml.FullLoader)


#导入requests封装后的对象
getYamlData = GetYamlData
req = ReqClass
globalEnv = GlobalEnv()
__all__= ["globalEnv","getYamlData","yamlObj","req","unittest","skip_func","returnRunCase","setting"]











