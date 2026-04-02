user_width = float(input("请输入您的体重(单位kg)："))
user_height = float(input("请输入您的身高(单位m)："))
user_bmi= user_width / user_height ** 2
print("你的BMI为"+str(user_bmi))