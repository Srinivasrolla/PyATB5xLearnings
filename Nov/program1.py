from random import *
jsp=0
tdp=0
ycp=0
for i in range(1,1000):
    rand=randint(1,76)
    if rand>0 and 25>=rand:
        jsp=jsp+1
    elif rand>25 and 50>=rand:
        tdp=tdp+1
    else:
        ycp=ycp+1
print("No.of votes for jsp :",jsp)
print("No.of votes for ycp :",ycp)
print("No.of votes for tdp :",tdp)
if jsp>ycp and tdp<jsp:
    print("jsp is winner",jsp)
elif jsp<ycp and ycp>tdp:
    print("ycp is winner",ycp)
else:
    print("tdp is winner",tdp)
