t95={3:4.30,4:3.18,5:2.78,6:2.57,7:2.45,8:2.36,9:2.31,10:2.26,15:2.14,20:2.09}
print("本程序能实现简单的不确定度计算\n")
n=int(input("测量次数:"))
if n not in t95.keys():
    tt95=float(input("没有内置的t0.95,请自行输入一个:"))
else:
    tt95=t95[n]
data=[]
for i in range(0,n):
    dd=float(input(f"第{i+1}次:"))
    data.append(dd)
dB=float(input("B类不确定度:"))

sum=0
for dd in data:
    sum+=dd
ave=sum/n
sum=0
for dd in data:
    sum+=pow((dd-ave),2)
delta=pow(sum/(n-1),1/2)
dA=delta*tt95/pow(n,1/2)
u=pow(pow(dA,2)+pow(dB,2),1/2)
ur=u/ave
ur*=100
urpercent=float(str(ur).split(".")[0] + "." + str(ur).split(".")[1][:2])+0.01

print(f"\nxbar={ave}\ndelta={delta}\nDeltaA={dA}\nDeltaB={dB}\nu={u:.1E}\nur={urpercent}%")
