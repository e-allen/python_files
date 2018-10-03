class Fruit:
    def __init__(self):
        self.name = 'Apple'


apple = Fruit()
same_apple = apple
print(apple is same_apple)


orange = Fruit()
print(apple is orange)

