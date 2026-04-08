# 张贴复制格式没解决，把每个部分改成方法或类
from operator import truediv


def study_basic_exception():
   #尝试捕获异常，并以可视化异常
   try:
       x = int(input("请输入第一个数：") or "10")
       y = int(input("请输入第二个数：") or "2")
       print(x / y)
   except ZeroDivisionError:
       print("第二个数不可为0")
   # except ValueError:
   #     print("error:not a valid number")  # 用户输入a
   # except Exception as e:
   #     print(f"unkown error:{e}")


def study_muffled_class():
    # 启用抑制功能
    class muffled:
        muff = False
        def calc(self):
            try:
                muffled_select = input("是否开启抑制开关Y/N")
                if muffled_select == "Y":
                    self.muff = True
                expr = input("请输入计算表达式（例如10/2）")
                print("结果为：", eval(expr))
                return eval(expr)
            except ZeroDivisionError:
                if self.muff:print(" ZeroDivisionError")
                else:raise
    c = muffled()
    c.calc()


def study_exception_transform():
    #异常转换
    try:
        #study_muffled_class()
        10/0
    except ZeroDivisionError:
        raise ValueError(" value error")


def much_except():
    #多个except,except叠加
    try:
        'h' + 1
        study_basic_exception()
    except TypeError:
        print("输入的值非数字")


def exception_handing():
    #利用循环处理多个计算，并跳过异常
    X = list(input("请输入x矩阵，例如12!"))
    Y = list(input("请输入y矩阵"))
    for x,y in zip(X,Y):
        try:
            x = int(x)
            y = int(y)
            print(x/y)
        except ZeroDivisionError:
            print("exist zeroerror,skipped")
        except ValueError:
            print("exist value error，skipped")
        except TypeError:
            print("type error,skipped")
        except Exception as e:
            print(f"unkown error:{e}")


def exception_cycle():
    #输入异常时，展示异常并自动进入下次输入
    while True:
        try:
            x = int(input("请输入第一个数：") or "10")
            y = int(input("请输入第二个数：") or "2")
            print(x / y)
        except Exception as e:
            print(f"error:{e}")
        # except (TypeError, ValueError,ZeroDivisionError):
        #     print("error")
        else:break
        finally:print("clean up")


def exception_more_function():
    #1.替代if/else，代码可读性提高
    #2.提高效率，直接查询键，except keyerror
    #3.直接访问属性，except attributeerror
    #4.添加finally，清除数据（注意，赋值失败即从未存在）
    x = None #防止赋值失败，导致del x 失效
    try:
        x = 1 / 0  # 赋值失败，即从未存在
    except ZeroDivisionError:
        print('error')
    finally:
        print("clean up")
        del x

import warnings
def exception_warning():
    #尝试使用warn和filerwarn,并使用try捕获warning
    try:
        #warnings.warn('THIS function is too old', DeprecationWarning)
        warnings.filterwarnings('error', category=DeprecationWarning)
        warnings.warn('我会被忽略吗', DeprecationWarning)
    except  DeprecationWarning:
        print("捕获到升级为错误的警告")














if __name__=="__main__":
    # 不需要测试的注释掉
    # study_basic_exception()
    # study_muffled_class()
    # study_exception_transform()
    # much_except()
    # exception_handing()
    # exception_cycle()
    # exception_more_function()
    exception_warning()
    print("后续的异常转换代码")






# #尝试捕获异常，并以可视化异常
# try:
#     x=int(input("请输入第一个数：")or"10")
#     y=int(input("请输入第二个数：")or"2")
#     print(x/y)
# except ZeroDivisionError:
#     print("第二个数不可为0")
# except ValueError:
#     print("error:not a valid number")#用户输入a
# except Exception as e:
#     print(f"unkown error:{e}")
#
# #启用抑制功能
# class muffled:
#     muff=False
#     def calc(self,expr):
#         try:
#             return eval(expr)
#         except ZeroDivisionError:
#             if self.muff:
#                 print("ERROR")
#             else:
#                 raise
#
# c=muffled()
# c.calc('10/1')
#
# #异常转换
# try:
#     1/0
# except ZeroDivisionError:
#     raise ValueError