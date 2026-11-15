#函数进阶之多种传参形式
def user_info(name,age,gender):
    print(f"名字是{name},年龄是{age},性别是{gender}")
#1、位置参数：调用函数时根据函数定义的参数位置来传递参数(需固定顺序)
user_info("小明",20,"男")
#2、关键字参数：函数调用时通过“键=值”形式传递参数(无需固定顺序，但必须放于位置参数后面)
user_info(name="小王",gender="男",age=18)

#3、缺省参数：用于定义函数,为参数提供默认值,调用函数时可不传该默认参数的值(函数调用时,如果为缺省参数传值则修改默认参数值,否则使用这个默认值)
def userinformation(name,age,gender="男"):#默认gender为男，可修改
    print(f"名字是{name},年龄是{age},性别是{gender}")
userinformation("小明",18)
userinformation("小红",19,"女")#修改为女

#4、不定长参数：用于不确定调用的时候会传递多少个参数(不传参也可以)的场景
#1.位置传递的不定长*利用元组传递
def user_set(*sets):
    print(sets)
user_set("hello")#输出元组

#2.关键字传递的不定长**利用字典的键值对传递
def user_dict(**dicts):
    print(dicts)
user_dict(name="小王",age=18,gender="男",addr="北京")#输出字典