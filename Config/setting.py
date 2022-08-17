#存放各种路径
#各种文件的绝对路径
#mysql、redis等地方的host、prod  username、password
import os,sys
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_PATH,"Config" ,'caseData')   #yaml测试用例存放位置
CASE_PATH = os.path.join(BASE_PATH, "TestCase") #测试用例存放位置
REPORT_PATH = os.path.join(BASE_PATH, 'results')  #测试报告存放位置

print(DATA_PATH)
print(CASE_PATH)
print(REPORT_PATH)

mysqlInfo = {

}

redisInfo = {

}