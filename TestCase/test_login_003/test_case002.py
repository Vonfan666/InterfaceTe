

from Logs.LogFile import Log
from TestCase import *


# p=Public()
# customerInfo=CustomerInfo()
class  TestLogin(unittest.TestCase):
    def setUp(self):
        self.logger = Log()
        self.logger.info('_______start_______')
    def tearDown(self):
        self.logger.info('________over_______\n')
    def test_001(self):
        print(globalEnv)
    def test_002(self):
        self.logger.info("这是第二二个 {}".format(globalEnv.cc))
    def test_003(self):
        print(333)


if __name__=="__main__":
    # unittest.main()
    suite=unittest.TestSuite()
    suite.addTest(TestLogin("test_001"))
    suite.addTest(TestLogin("test_002"))
    suite.addTest(TestLogin("test_003"))
    # suite.addTest(TestLogin("test_002"))
    # suite.addTest(TestLogin("test_003"))
    # suite.addTest(TestLogin("test_009"))
    # suite.addTest(TestLogin("test_019"))
    # suite.addTest(TestLogin("test_060"))
    #
    results=unittest.TestResult()
    runner=unittest.TextTestRunner(resultclass=results)
    runner.run(suite)



