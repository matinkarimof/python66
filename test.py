
#1)

def fibo(num) :

    if num == 0:
        return 0
    if num == 1 :
        return 1

    return fibo(num - 1) + fibo(num - 2)


print(fibo(10))


print("-" * 50)

#2)

class fraction :
    def __init__(self , a , b):
        self.a = a
        self.b = b

    def __add__(self, other):
        new_a = self.a * other.b + self.b * other.a
        new_b = self.b * other.b
        return fraction(new_a , new_b)

    def __mul__(self, other):
        new_a = self.a * other.a
        new_b = self.b * other.b
        return fraction(new_a , new_b)  

    def __truediv__(self, other):
        new_a = self.a * other.b 
        new_b = self.b * other.a
        return fraction(new_a , new_b)

    def __str__(self):
        return f"{self.a}/{self.b}"

h1 = fraction(1,2)
h2 = fraction(3,4)

print(h1 + h2)
print(h1 * h2)
print(h1 / h2)