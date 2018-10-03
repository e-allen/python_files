class Square():


    def __init__(self, s):
        self.side = s


    def print_side(self):
        print("""{} by {} by {} by {}
              """.format(self.side, self.side, self.side, self.side))

s1 = Square(29)
s1.print_side()

