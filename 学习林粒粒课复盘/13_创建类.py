class student:
    def __init__(self,name,student_id,age):
        self.name=name
        self.student_id = student_id
        self.age=age
        self.grades = {"语文":0,"数学":0,"英语":0}
    def grades_if(self,grade ,grade_d):
        if grade in self.grades:
            self.grades[grade]=grade_d
    def print_grades(self):
        print("学生:{0}\n学号:{1}\n的成绩为：".format(self.name,self.student_id))
        for k,v in self.grades.items():
            print("{0}:{1}".format(k,v))
chen = student("小成","100618",18)
chen.grades_if("数学",95)

chen.print_grades() 