print("输入请使用国际单位,可以用科学计数法e输入")
d=float(input("d="))
ud=float(input("ud="))
D=float(input("D="))
uD=float(input("uD="))
m=float(input("m="))
um=float(input("um="))
s=float(input("s="))
us=float(input("us="))
t=float(input("t="))
ut=float(input("ut="))
rho=float(input("rho="))
urho=float(input("urho="))
g=float(input("g="))
pi=3.141592
A=6*m/(pi*d)-rho*pow(d,2)
B=D/(D+2.4*d)
pd=abs(-g*D/18*(6*m/pi*(D+4.8*d)/(pow(d*(D+2.4*d),2))+rho*(2*D*d+2.4*d*d)/(pow(D+2.4*d,2)))*t/s)
pD=abs(g/18*A*t/s*2.4*d/pow(D+2.4*d,2))
pt=abs(g/18*A/s*B)
ps=abs(-g/18*A*t/s/s*B)
prho=abs(-g/18*t*d*d/s*B)
pm=abs(g/18*6/(pi*d)*t/s*B)
pud=pd*ud
puD=pD*uD
put=pt*ut
pus=ps*us
purho=prho*urho
pum=pm*um
eta=g/18*A*t/s*B
ueta=pow(pow(pud,2)+pow(puD,2)+pow(put,2)+pow(pus,2)+pow(purho,2)+pow(pum,2),1/2)
ureta=ueta/eta
ureta*=100
urpercent=float(str(ureta).split(".")[0] + "." + str(ureta).split(".")[1][:2])+0.01
print(f"\neta={eta},ueta={ueta:.1E},ureta={urpercent}%")
print(f"\n\
      pd={pd},\tpd*ud={pud}\n\
      pD={pD},\tpD*uD={puD}\n\
      pt={pt},\tpt*ut={put}\n\
      ps={ps},\tps*us={pus}\n\
      prho={prho},\tprho*urho={purho}\n\
      pm={pm},\tpm*um={pum}\n")

