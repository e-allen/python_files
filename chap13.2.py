# Rect and Sq classes calculate_perimeter


class Square():
    def __init__(self, w, l, n):
        self.width = w
        self.len = l
        self.n = n

    def change_size(self):
        return ((self.width + self.n) + (self.len + self.n)) * 2
    
