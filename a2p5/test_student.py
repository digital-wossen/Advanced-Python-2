# JTSK-350112
# a2 5.py
# Wossen Hailemariam
# w.haillemarim@jacobs-university.de


from student import Student

obj = Student('Jhon', 3, 11)

Student.setScore(obj, 1,100)
Student.setScore(obj, 2,90)
Student.setScore(obj, 3,50)

print(obj)

Student.setName(obj, "Jack")
Student.setAge(obj, 17)
print(obj)

