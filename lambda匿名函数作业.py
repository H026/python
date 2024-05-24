# 函数作为参数传递
# 通过def关键字定义一个函数
def test_func(compute):
    result=compute(1,100)
    print(result)
def compute(x,y):
    return x+y
test_func(compute)
# lambda 匿名函数
# 也可以通过lambda关键字，传入一个一次性使用的lambda匿名函数
def test_func(compute):
    result=compute(1,100)
    print(result)
    test_func(lambda x,y:x+y)
    # 使用def和使用lambda，定义函数功能完全一致，只是lambda关键字定义函数是匿名的，无法二次使用
