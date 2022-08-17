from  TestCase import globalEnv


def CaseFailCount(func):
    def caseFail():
        try:
            return func()
        finally:
            print(globalEnv,"diaomaomaoa")
            globalEnv.skipCase={func.__class__:{func.__name__:0}}
            print(func.__class__)
            print(func.__name__)
    return caseFail


