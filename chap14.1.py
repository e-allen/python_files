class Square():
    sqs = []


    def __init__(self, s):
        self.side = s
        self.sqs.append((self.side**2))

sq1 = Square(5)
sq2 = Square(64)
sq3 = Square(35)

print(Square.sqs)

