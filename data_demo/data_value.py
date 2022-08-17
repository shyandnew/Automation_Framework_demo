'''
这里实现测试数据类，只做演示，实现最基础的数据类（和关键字驱动区别不大）
'''

class Data_demo(object):

    def __init__(self):
        pass

    #基础数据类方法，参数为数据的属性和数据索引
    def data_input(self, *args):
        with open('data.txt', 'r', encoding='utf-8') as file:
            username = file.readline().split(',')
            password = file.readline().split(',')
        if args[0] == 'username' and args[1] != 'password':
            return username[args[1]-1]
        elif args[0] == 'password':
            return password[args[1]-1]
        elif args[0] == 'username' and args[1] == 'password':
            list_data = []
            if len(username) == len(password):
                for i in range(0, len(username)):
                    case_data = []
                    case_data.append(username[i])
                    case_data.append(password[i])
                    list_data.append(case_data)
                return list_data
            else:
                raise ValueError('测试数据设置错误，请检查！')
        else:
            print('参数有误！')




if __name__ == '__main__':
    a = Data_demo()
    print(a.data_input('username','password'))
