# Physics_Experiment_in_PY

我为了便利实现大物实验所写的一些脚本

## 不确定度
  便利实现不确定度计算，内置t0.95，可手动加入B类不确定度。
  
## 线性拟合
  输入x,y轴数据，生成线性拟合图像，并生成拟合的截距、斜率、拟合度、残差平方和等（ORIGIN有的它都有，完美满足大物实验要求）。
  可以手动输入，也可以excel导入。
  evil check功能可以给出数据修改建议，解决实验数据不够精确导致的拟合度不够的问题。
      本人曾经因为一个r=0.9998的实验数据被助教扣了分，理由是拟合度不够。如此实验器材每组数据都想要那么高精度简直是吹毛求疵，且三个9在一般的实验报告中也完全不算是误差大，于是乎本人萌生了做一个数据篡改工具的想法。
      evil check可以实现你想要的任意个9的拟合度，并且支持把修改后的数据导出到excel
      
      
## 落球法
  专门针对“落球法测粘滞系数”的实验，该实验的数据处理极为离谱，公式极长，且不确定度计算要写小过程。
    本人第一次做的时候用卡西欧计算器，结果最长的一个公式直接超出计算器能输出的最大长度。
  该脚本只需要把你的数据输进来，数据处理好的数据就能直接返回。
  
## 霍尔
  专门针对“集成霍尔传感器的研究”实验，该实验要画一个ORIGIN不方便画的图，而python可以实现。
  同样支持从excel导入。
