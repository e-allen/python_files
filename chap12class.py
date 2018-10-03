class Orange:
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        self.mold = 0
        print("Created!")


    def rot(self, days, temp):
        self.mold = days * temp

        


