#类和对象
#类只是一种程序内的“设计图纸”,需要基于图纸生产实体(对象),才能正常工作
class Clock:
    id=None
    price=None

    def ring(self):
        import winsound
        winsound.Beep(2000,3000)#winsound.Beep(频率。持续时间)

clock1=Clock()#创建对象
clock1.id="001"
clock1.price=100
print(f"钟表编号:{clock1.id},价格:{clock1.price}")
clock1.ring()

clock2=Clock()#创建对象
clock2.id="002"
clock2.price=101
print(f"钟表编号:{clock2.id},价格:{clock2.price}")
clock2.ring()