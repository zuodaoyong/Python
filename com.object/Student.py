class Student:
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_name(self, name):
        self.__name = name

    def set_score(self, score):
        self.__score = score

    def print_info(self):
        print('name=%s,score=%d' % (student.__name, student.__score))

    def get_grade(self):
        if self.__score >= 90:
            return "A"
        elif self.__score >= 80:
            return "B"
        elif self.__score >= 70:
            return "C"
        else:
            return "D"


student = Student("neo", 70)
student.set_name("zuo")
student.print_info()
# print(student.get_grade())
