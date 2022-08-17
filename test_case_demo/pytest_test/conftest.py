'''
fixture前后置操作demo

conftest.py是固定文件名，fixture()前后置方法可以放到这个文件中供全局或部分用例使用，可以按照后续实际情况使用。

return和yield 都是返回的意思
return:在程序函数中返回某个值，返回之后函数不在继续执行，彻底结束。（通俗可以理解为return后面不能接代码，因为写了也不会继续运行）
yield:带有yield的函数是一个迭代器，函数返回某个值时，会停留在某个位置，返回函数值后，会在前面停留的位置继续执行，直到程序结束。（通俗可以理解为yield后面可以接代码，因为返回后会到之前的位置继续运行）
'''

import pytest

@pytest.fixture()
def test_fixture():
    print('\n这个是fixture前置方法，可以实现部分用例的前置，可以作用于类或者类方法！')
    # 部分前后置处理中的后置处理，可以和前后置一起使用，也可以单独拿出编辑函数使用
    yield
    print('\n这个是fixture后置方法，可以实现部分用例的后置，可以作用于类或者类方法！')


'''
@pytest.fixture()参数讲解：
1、scope：表示的是被@pytest.fixture标记的方法的作用域，function(默认作用域，作用域为类方法)，class(作用域为类)，module（作用域为模块，也就是一个py文件），package/session（作用域为package文件夹，也就是包，session不做赘述，作用域比包还大，很少用到！）
2、params：参数化(列表、元组、字典)
3、autouse：自动执行autouse=True（所有用例都执行）,默认是False
4、ids：当使用params参数化时,给每个值设置一个变量名，意义不是很大
5、name：表示被@pytest.fixture标记的方法取一个别名
'''
@pytest.fixture(scope='function', autouse=False, params=['Tom','Nike','Mac'], ids=['num 1','num 2','num 3'], name='test')
def test_fixture_two(request):
    print('\n这个是fixture前置方法2！')
    return request.param