class student:
    def __init__(self,student_name):
        self.student_name = student_name

        self.status = True


    def get_status(self):
        if self.status == True:
            return "{} на гранте".format(self.student_name)
        else:
            return "{} отчислился".format(self.student_name)

    def set_status(self,new_status):
        self.status = new_status

    def __repr__(self):
        return self.student_name