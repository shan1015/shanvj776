wor=input()
tem=wor.strip()
tem2=2
for n in range (len(tem)):
    if(tem[n]==' ' and (tem[n]!=tem[n+1])):
        tem2=tem2+2
if(tem2>2):
    print(tem2)
