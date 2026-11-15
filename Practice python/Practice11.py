#函数初步练习
def check_age(age):
    if age>=18:
        return "Success"
    else:
        return None

result=check_age(13)
if result==None:
    print("未成年")