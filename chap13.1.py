# Rect and Sq classes calculate_perimeter


class Square():
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def calculate_perimeter(self):
        return (self.width + self.len) * 2

class Rectangle(Square):
    def __init__(self, w, l):
        self.width = w
        self.len = l

