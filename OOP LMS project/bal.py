from UNi import university
from student import student
class lesson:
    def __init__(self,prof,kredit = None):
        self.prof = prof
        self.less = []
        self.kredit = kredit
        self.assessment = {}

    def set_prof(self):
        if self.prof == "Automation":
            self.less = ["Math","Fizika","Matlab"]
            self.kredit = 9
        elif self.prof == "IS":
            self.less = ["web program","discret math","ict"]
            self.kredit = 9
        elif self.prof == "Legal matter":
            self.less = ["legal","charizma","right"]
            self.kredit = 9

    def get_less(self):
        return self.less
    def get_prof(self):
        return "Студент выбрал профессию {}\n{} имеет в базе проф. предметы: {}\n {} - {} кредитов".format(self.prof,self.prof,self.less,self.less,self.kredit)


    def assessments(self,baga1,baga2,baga3):
        self.assessment[self.less[0]] = baga1
        self.assessment[self.less[1]] = baga2
        self.assessment[self.less[2]] = baga3
        return self.assessment

    def gpa(self):
        q = 0
        for i in self.assessment.values():
            q += i
        q *= 10
        g = q/self.kredit
        if g < 10:
            return "GPA - {} - не Зачет Вы не прошли, у вас нет гранта ".format(g)
        else:
            return "GPA - {}".format(g)

    def get_gpa(self):
        q = 0
        for i in self.assessment.values():
            q += i
        q *= 10
        g = q / self.kredit
        return g

u = university()
while True:
    name = input("Введите имя для студента: ")
    s = student(name)
    print(s.get_status())
    u.add_stud(s)


    a = input("Выберите профессию:\n1.Automation\n2.IS\n3.Legal matter\nВыберите по имену: ")

    l = lesson(a)

    l.set_prof()

    print(l.get_prof())

    baga1 = int(input("Оцените студента [2 - 5]] по уроку {} ".format(l.less[0])))
    baga2 = int(input("Оцените студента [2 - 5]] по уроку {} ".format(l.less[1])))
    baga3 = int(input("Оцените студента [2 - 5]] по уроку {} ".format(l.less[2])))

    print(l.assessments(baga1,baga2,baga3))


    print(l.gpa())

    if l.get_gpa() < 10:
        u.remove_stud(s)
        s.set_status(False)


    print(s.get_status())
    print(u.get_grant())
