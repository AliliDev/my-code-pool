user_sex = input("用户你好你的性别是什么呢（男/女）：")
user_sex_nan="先生"
user_sex_nv="女士"
while True:
    if user_sex not in ["男","女"]:
        print(print("性别格式输入错了哦要的格式是（男/女）而不是"+user_sex+"哟"))
        user_sex = input("用户你好你的性别是什么呢（男/女）：")
    else:
        if user_sex == "男":
            user_sex = user_sex_nan
        else:
            user_sex = user_sex_nv
        break

user_width = float(input("请输入您的体重(单位kg)："))
user_height = float(input("请输入您的身高(单位m)："))
user_bmi= user_width / user_height ** 2
if user_bmi <=18.5 :
    print(user_sex+"你好你有点偏廋哦")
elif 18.5 <= user_bmi <= 25 :
    print(user_sex+"你好你很正常喵")
elif 25 <= user_bmi <= 30 :
    print(user_sex+"你好你有点偏胖哟")
else:
    print(user_sex+"你好你胖的魔法")
