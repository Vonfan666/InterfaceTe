#unittest封装的一下装饰器
import functools

from TestCase import unittest


def skip_func(depend=""):
    # 封装skip指定测试用例跳过装饰器
    """
    :param depend: 依赖的用例函数名，默认为空
    :return: wraper_func
    """
    def wraper_func(test_func):

        def inner_func(self):
            if depend == test_func.__name__:
                raise ValueError("{} cannot depend on itself".format(depend))
            failures = str([fail[0] for fail in self._outcome.result.failures])
            errors = str([error[0] for error in self._outcome.result.errors])
            skipped = str([error[0] for error in self._outcome.result.skipped])
            flag = (depend in failures) or (depend in errors) or (depend in skipped)
            if failures.find(depend) != -1:
                # 输出结果 [<__main__.TestDemo testMethod=test_login>]
                # 如果依赖的用例名在failures中，则判定为失败，以下两种情况同理
                test = unittest.skipIf(flag, "{} failed".format(depend))(test_func)
            elif errors.find(depend) != -1:
                test = unittest.skipIf(flag, "{} error".format(depend))(test_func)
            elif skipped.find(depend) != -1:
                test = unittest.skipIf(flag, "{} skipped".format(depend))(test_func)
            else:
                test = test_func
            return test(self)

        return inner_func

    return wraper_func

def returnRunCase(func=None, count=1, func_prefix="test"):
    """
    :param
    target: 被装饰的对象，可以是class, function
    :param
    max_n: 重试次数，没有包含必须有的第一次执行
    :param
    func_prefix: 当装饰class时，可以用于标记哪些测试方法会被自动装饰
    :return: wrapped
    :return:
    """
    def prefix_func(func_test):
        @functools.wraps(func_test)
        def inner_func(*args,**kwargs):
            func=None
            for  item  in  range(count+1):
                try:
                    func=func_test(*args,**kwargs)
                    return func
                except Exception as f:
                    if item<count:
                        print("第{count}次执行,抛出错误：%{error}".format(count=item,error=f))
                    else:
                        raise Exception("第{count}次执行,抛出错误：%{error}".format(count=item,error=f))
            return func
        return inner_func
    return prefix_func


if  __name__=="__main__":
    skip_func(depend="test_oo2")
    print()