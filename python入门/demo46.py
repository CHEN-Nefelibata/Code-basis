#数据可视化之地图可视化
from pyecharts.charts import Map#导入map功能
from pyecharts.options import VisualMapOpts#导入视觉映射组件
map=Map()#创建初始map
data=[
    ("北京市",99),
    ("上海市",199),
    ("安徽省",299),
    ("台湾省",399),
    ("广东省",499)
]
#添加数据
map.add("测试地图",data,"china")#("名称",数据,"地图类型")默认地图为中国地图
map.set_global_opts(#设置全局选项
    visualmap_opts=VisualMapOpts(
        is_show=True, #是否显示视觉映射组件
        is_piecewise=True,#是否手动校准
        pieces=[
            {"min": 1, "max": 9, "label": "1-9", "color":"#CCFFFF"},
            {"min": 10, "max": 99, "label": "10-99", "color": "#FF6666"},
            {"min": 100, "max": 500, "label": "100-500", "color": "#990033"}#设置颜色
        ]
    )
)
map.render()#生成html图表