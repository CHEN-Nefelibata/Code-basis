#面向对象之封装
class Phone:
    __is_5g_enable=False

    def __check_5g(self):
        if self.__is_5g_enable==True:
            print("5G已开启")
        else:
            print("5G关闭，4G开启")

    def call_by_5g(self):
        self.__check_5g()  #在类的内部可以调用私有成员方法
        print("正在通话中")

phone=Phone()
phone.call_by_5g()