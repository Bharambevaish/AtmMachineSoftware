class Fraction:

    def __init__(self, n, d):
        self.n = n
        self.d = d
    def __str__(self):
        return "{}/{}".format(self.n,self.d)

    def __add__(self, other):
        temp_num = self.n * other.d + self.d * other.n
        temp_deno = self.d * other.d
        return "{}/{}".format(temp_num, temp_deno)

    def __sub__(self, other):
        temp_num = self.n * other.d - self.d * other.n
        temp_deno = self.d * other.d
        return "{}/{}".format(temp_num, temp_deno)

    def __mul__(self, other):
        temp_num = self.n * other.n
        temp_deno = self.d * other.d
        return "{}/{}".format(temp_num, temp_deno)

    def __truediv__(self, other):
        temp_num = self.n * other.d
        temp_deno = self.d * other.n
        return "{}/{}".format(temp_num, temp_deno)
