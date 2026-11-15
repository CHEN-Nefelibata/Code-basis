#union定义联合类型注解
from typing import Union
my_list:list[Union[int,str]]=[1,2,3,'a','b','c']

my_dict:dict[str,Union[int,str]]={'a':1,'b':2,'c':'3'}

def func(data:Union[int,str])->Union[int,str]:
    pass
func()