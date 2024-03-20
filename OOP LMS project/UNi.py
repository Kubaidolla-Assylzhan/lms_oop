class university:
    def __init__(self):
        self.grant = []

    def add_stud(self,new):
        self.grant.append(new)

    def remove_stud(self,old):
        self.grant.remove(old)

    def get_grant(self):
        return self.grant











