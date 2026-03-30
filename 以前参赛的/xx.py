def qwq(x= None, y=None):
    if x>0 and y>0:
        ming="第一象限"
    elif x < 0 < y:
        ming="第二象限"
    elif x<0 and y<0:
        ming="第三象限"
    elif x > 0 > y:
        ming="第三象限"
    elif x==0 and y!=0:
        ming="Y轴上"
    elif x!=0 and y==0:
        ming="X轴上"
    else:
        ming="原点"
    print(ming)
    return
a=int(input(":::"))
b=int(input(":"))
qwq(a,b)


