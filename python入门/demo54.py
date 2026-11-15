#继承之复写
class Phone:
    IMEI=None
    Producer= "Itcast"

    def call_by_5g(self):
        print("5G通话")

class newPhone(Phone):
    Producer= "ITheima"#复写父类属性

    def call_by_5g(self):#复写父类方法
        print("开启cpu单核模式，确保省电")
        print("5G通话")
        #调用父类方法
        super().call_by_5g()
        #调用父类名称
        print(f"父类名为: {Phone.Producer}")
        print("关闭cpu单核模式，确保性能")

phone=newPhone()
print(phone.Producer)
phone.call_by_5g()