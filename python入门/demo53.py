#面向对象之继承
#单继承
class Phone:
    IMEI= None
    Producer= "HM1"

    def call_by_4g(self):
        print("4G通话")

class Phonenew(Phone):#继承父类Phone
    face_id=None

    def call_by_5g(self):
        print("新功能：5G通话")

phone=Phonenew()
print(phone.Producer)
phone.call_by_4g ()
phone.call_by_5g()

#多继承
class NFCreader:
    nfc_type=5
    Producer="HM2"

    def read_card(self):
        print("读取NFC卡")

    def write_card(self):
        print("写入NFC卡")

class RemoteControl:
    rc_type="红外遥控"

    def control_tv(self):
        print("遥控开启了")

class newPhone(Phone,NFCreader,RemoteControl):#继承父类Phone、NFCreader、RemoteControl
    pass#补全语法，防止报错

phone=newPhone()
print(phone.Producer)
phone.call_by_4g()
phone.read_card()
phone.write_card()
phone.control_tv()
print(phone.Producer)#以Phone类的Producer为准，NFCreader类的Producer被覆盖