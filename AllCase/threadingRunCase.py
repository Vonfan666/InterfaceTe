 # coding:utf-8
#! /usr/bin/python
import  unittest,requests,HTMLTestRunner,time,os,threading
# from requests.packages.urllib3.exceptions import InsecureRequestWarning
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
# from feng_test_method.feng_test_MethodCode import *
# from appium import webdriver
import smtplib, os, re  # 发送库
from email.mime.text import MIMEText  # 构建文本邮件库
from email.mime.multipart import MIMEMultipart
PATH = lambda  p:os.path.abspath(
       os.path.join(os.path.dirname(__file__),p)
)

def allCase():
    # allTests=[]
    #待执行用例的目录
    BASE_PATH=os.path.dirname(os.path.dirname(__file__))
    case_dir=os.path.join(BASE_PATH,"TestCase")
    pathList=os.listdir(case_dir)
    pathLists=[]
    for  item  in  pathList:
        if item.startswith("test"):
            pathLists.append(item)
    #构造测试集合
    suite=unittest.TestSuite()
    pathLists=sorted(pathLists,key=lambda x:x.split("_")[-1])

    #获取到一个模块的list集合
    for item  in  pathLists:
        path=os.path.join(BASE_PATH,"TestCase",item)
        path=os.path.abspath(path)
        print(path)
        allTest = unittest.defaultTestLoader.discover(path,pattern="test*.py",top_level_dir=case_dir)
#pattern————匹配脚本名称规则，test*.py是匹配所有test开头的所有脚本
#top_level_dir 这个是顶层目录的名称 ，一般为空就可以了
        suite.addTests(allTest)

    return  suite


# HTMLTestRunner
import sys,datetime
from HTMLTestRunner import _TestResult
class  HTMLTestRunnerNew(HTMLTestRunner.HTMLTestRunner):
    def __init__(self,stream=sys.stdout, verbosity=1, title=None, description=None,result=None):

        super().__init__(stream=stream, verbosity=1, title=title, description=description)
        self.result=result
        self.verbosity=verbosity

    def run(self,test,caseinfo={}):
        self.test=test
        self.caseinfo=caseinfo
        if self.result is None:
            self.result = _TestResult(self.verbosity)
        test(self.result)
        self.stopTime = datetime.datetime.now()
        self.oute=self.last_generateReport(self.test, self.result, self.caseinfo)
        print(sys.stderr, '\nTime Elapsed: %s' % (self.stopTime - self.startTime))

    def writeReport(self):
        self.stream.write(self.oute.encode('utf-8'))
if __name__=="__main__":
    result=HTMLTestRunner._TestResult()
    suites=allCase()
    lens=len(suites._tests)
    Threads=[]
    pathCode =os.path.dirname(os.path.dirname(__file__))+'/results/'
    curtime=time.strftime('%Y%m%d%H%M%S',time.localtime())
    report_path = pathCode+curtime+'.html'
    report_set = open(report_path, 'wb')
    runner = HTMLTestRunnerNew(stream=report_set,title=u'自动化测试报告',description=u'用例执行情况：',result=result)
    def getRun(item=None):
        runner.run(item)
    suiteCase=[]
    for item  in  suites._tests:
        if len(item._tests) > 0:
            suiteCase.append(item)
    for  index,item  in   enumerate(suiteCase):
        name="t_%s"%(index)
        name=threading.Thread(target=getRun,kwargs={"item":item})
        Threads.append(name)
        name.start()
    for  Thread  in Threads:
            Thread.join()
    runner.writeReport()
    report_set.close()

