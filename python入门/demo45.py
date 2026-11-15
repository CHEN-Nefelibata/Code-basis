#2、pyecharts模块（百度旗下官网https://pyecharts.org/#/）
#pyecharts画廊gallery.pyecharts.org
from pyecharts.charts import Line#调用模块
from pyecharts.options import TitleOpts,LegendOpts,ToolboxOpts,VisualMapOpts
line=Line()#添加折线图
line.add_xaxis(['中国','美国','英国'])#设置x轴数据
line.add_yaxis("GDP",[30,20,10])#设置y轴数据
line.set_global_opts(#设置全局配置
    title_opts=TitleOpts(title="GDP对比图",pos_left="center"),#设置标题，改变位置使标题居中
    legend_opts=LegendOpts(is_show=True),#显示图例
    toolbox_opts=ToolboxOpts(is_show=True),#显示工具箱
    visualmap_opts=VisualMapOpts(is_show=True)#显示视觉映射
)
line.render("render.html")#生成html文件
#打开需要多刷新几次