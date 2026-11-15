#面向对象之封装
#封装：将现实世界的事物的属性和行为在类中描述为成员变量、成员方法
#私有成员变量、私有成员方法：在变量名或方法名前加双下划线 "__"
#私有成员变量和私有成员方法只能在类的内部访问，外部无法直接访问。（即无法被赋值或调用）

#定义一个类，包含私有成员变量及方法
class Phone:
    __current_voltage=0.5  #私有成员变量


    def __keep_single_core(self):  #私有成员方法
        print("保持单核运行")

    def call_by_5g(self):
        if self.__current_voltage>=1:  #在类的内部可以调用私有成员方法
            print("5G通话")
        else:
            self.__keep_single_core()
            print("电量不足")  #在类的内部可以调用私有成员方法

phone=Phone()
phone.call_by_5g()