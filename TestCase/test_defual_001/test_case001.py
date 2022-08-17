from Logs.LogFile import Log
from TestCase import *

# p=Public()
# customerInfo=CustomerInfo()
"""
0: 失败
1：成功
"""

globalEnv.failList=[]
# def skip_dependon(depend=""):
#     """
#     :param depend: 依赖的用例函数名，默认为空
#     :return: wraper_func
#     """
#     def wraper_func(test_func):
#         def inner_func(self):
#             if depend == test_func.__name__:
#                 raise ValueError("{} cannot depend on itself".format(depend))
#             failures = str([fail[0] for fail in self._outcome.result.failures])
#             errors = str([error[0] for error in self._outcome.result.errors])
#             skipped = str([error[0] for error in self._outcome.result.skipped])
#             flag = (depend in failures) or (depend in errors) or (depend in skipped)
#             if failures.find(depend) != -1:
#                 # 输出结果 [<__main__.TestDemo testMethod=test_login>]
#                 # 如果依赖的用例名在failures中，则判定为失败，以下两种情况同理
#                 # find()方法：查找子字符串，若找到返回从0开始的下标值，若找不到返回 - 1
#                 test = unittest.skipIf(flag, "{} failed".format(depend))(test_func)
#             elif errors.find(depend) != -1:
#                 test = unittest.skipIf(flag, "{} error".format(depend))(test_func)
#             elif skipped.find(depend) != -1:
#                 test = unittest.skipIf(flag, "{} skipped".format(depend))(test_func)
#             else:
#                 test = test_func
#             return test(self)
#
#         return inner_func
#
#     return wraper_func

class  TestLogin(unittest.TestCase):
    def setUp(self):
        self.logger = Log()
        self.logger.info('_______start_______')
    def test_001(self):
        globalEnv.cc = 1
        self.logger.info("这是CC啊%s"%globalEnv.cc)
        data=getYamlData("login")
        res=req(url=data.url,header=data.header,data=data.data)
        res=res(data.type)
        self.logger.info(res.json())
        res=res.json()
        self.assertEqual("inde11",res["data"]["fengfan"],msg="嘎嘎嘎嘎")

    @returnRunCase(count=5)
    def test_002(self):
        globalEnv.cc=1
        data = getYamlData("login2")
        res = req(url=data.url, header=data.header, data=data.data)
        res = res(data.type)
        if status_code==200:
            res = res.json()
            self.assertEqual("index", res["data"]["fengfan"], msg="嘎嘎嘎嘎")

    @skip_func("test_002")  # 如果test_002执行失败就跳过这个方法
    @returnRunCase(count=5) #用例失败重新执行--最多执行五次
    def test_003(self):
        globalEnv.cc = 2222222
        self.logger.info("这是CC啊%s" % globalEnv.cc)
        data = getYamlData("login3")
        res = req(url=data.url, header=data.header, data=data.data)
        res = res(data.type)
        self.logger.info(res.json())
        res = res.json()
        self.assertEqual("inde11x", res["data"]["fengfan"], msg="嘎嘎嘎嘎")
    def test_004(self):
        data = getYamlData("login3")
        res = req(url=data.url, header=data.header, data=data.data)
        res = res(data.type)
        self.logger.info(res.json())
        res = res.json()
        self.assertEqual("inde11x3424324", res["data"]["fengfan"], msg="000")

    @unittest.expectedFailure
    def test_005(self):
        pass


    def tearDown(self):
        self.logger.info('________over_______\n%s' % (self._outcome.result.failures))
        self.logger.info("断言失败列表 -----%s" % self._outcome.result.failures)
        self.logger.info("错误列表啊 -----%s" % self._outcome.result.errors)
        self.logger.info("跳过列表 -----%s" % self._outcome.result.skipped)
        self.logger.info("+++++++++++++%s"%self._outcome.result.failures)
        failures = str([fail[0] for fail in self._outcome.result.failures])
        # globalEnv.failList=failures
        errors = str([error[0] for error in self._outcome.result.errors])
        skipped = str([error[0] for error in self._outcome.result.skipped])
        self.logger.info("断言失败列表 **********-%s" % failures)
        self.logger.info("错误列表啊  **********-%s" % errors)
        self.logger.info("跳过列表  **********-%s" % skipped)


if __name__=="__main__":
    unittest.main()
    print("______________aa__________________________",globalEnv.failList)
    if globalEnv.failList:
        suite=globalEnv.failList

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
        runner=unittest.TextTestRunner()
        runner.run(suite)
    # self.expecting_failure = False
    # self.result = result
    # self.result_supports_subtests = hasattr(result, "addSubTest")
    # self.success = True
    # self.skipped = []
    # self.expectedFailure = None
    # self.errors = []



