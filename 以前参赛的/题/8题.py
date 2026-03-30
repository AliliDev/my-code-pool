score = int(input())
if 100 >= score and score >= 0:
    if score>=80:
        print("优秀")
    elif score>=70:
        print("良好")
    elif score>-60:
        print("及格")
    else:
        print("不及格")
else:
    print("非法成绩")
