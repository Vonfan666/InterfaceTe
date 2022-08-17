import ddt,os

from Logs.LogFile import Log
from TestCase import *

# p=Public()
# customerInfo=CustomerInfo()
"""
0: 失败
1：成功
"""
path= os.path.join(setting.DATA_PATH,"data.yaml")
globalEnv.failList=[]
@ddt.ddt
class  TestLogin(unittest.TestCase):
    def setUp(self):
        self.logger = Log()
        self.logger.info('_______start_______')
    @ddt.file_data(path)
    def testcase(self,**kwargs):
        data=getYamlData(kwargs)
        self._testMethodName = data.caseMethodName
        res = req(url=data.url, header=data.header, data=data.data)
        res = res(data.type)
        status=res.status_code
        isAseertObj=data.isAssert
        self.assertEqual(isAseertObj["status"], status, msg="嘎嘎嘎嘎")
        # self.assertEqual(isAseertObj["data"]["name"], status, msg="嘎嘎嘎嘎")

    def testcase_001(self):
        self.logger.info("这是执行的22")
    def tearDown(self):
        failures = str([fail[0] for fail in self._outcome.result.failures])
        # globalEnv.failList=failures
        errors = str([error[0] for error in self._outcome.result.errors])
        skipped = str([error[0] for error in self._outcome.result.skipped])



if __name__=="__main__":
    unittest.main()

    # suite=unittest.TestSuite()
    # suite.addTest(TestLogin("test_001"))
    # suite.addTest(TestLogin("test_002"))
    # suite.addTest(TestLogin("test_003"))
    # # suite.addTest(TestLogin("test_002"))
    # # suite.addTest(TestLogin("test_003"))
    # # suite.addTest(TestLogin("test_009"))
    # # suite.addTest(TestLogin("test_019"))
    # # suite.addTest(TestLogin("test_060"))
    #

    # self.expecting_failure = False
    # self.result = result
    # self.result_supports_subtests = hasattr(result, "addSubTest")
    # self.success = True
    # self.skipped = []
    # self.expectedFailure = None
    # self.errors = []



