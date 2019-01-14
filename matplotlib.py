import numpy as np
import matplotlib.pyplot as plt
list1=[1,2,3]
list2=[90,0,92]

x = np.array(list1)
y = np.array(list2)
#创建figure类
fig = plt.figure(figsize=(20,20))

left, bottom, width, height = 0.2, 0.2, 0.5, 0.7
ax = fig.add_axes([left, bottom, width, height])

#画柱状图
plt.bar(x, y)

#设置标题
ax.set_title('AI accelerators Performance')

#设置轴的标签
plt.ylabel('TERA-OP/SEC')
#plt.xlabel('Architecture')

#设置坐标轴区间
plt.ylim(85,95)

#设置x刻度
ticks = ax.set_xticks([1, 2,3])

#改刻度名
list = ['Branwave', '','TPU']
labels = ax.set_xticklabels(list, rotation=0, fontsize='medium') 
ticks = ax.set_yticks(np.arange(85,95))

plt.savefig('fig.png')
plt.show()