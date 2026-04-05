wan = []
while True :
    user_input = input("请输入数字可以计算平均值（输入q终止）：")
    if user_input == "q":
        break
    else :
        wan.append(user_input)

if len(wan)==0 :
    print("平均值为：0")
else:
    sum1 = 0
    for i in wan :
        sum1 = sum1 + float(i)
    print(str(wan)+"\n的平均值为：\n"+str(sum1/len(wan)))

