#multiple inheretance
class Grandfather:
    def land(self):
        print("land")
class Father:
    def Animals(self):
        print("goats")
class Son(Grandfather,Father):
    def Company(self):
        print("company")
s=Son()
s.Company()
s.Animals()
s.land()
