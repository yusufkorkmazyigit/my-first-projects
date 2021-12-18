class Circle:
    #Class object attribute
    pi=3.14
    def __init__(self,yaricap=1):
        self.yaricap=yaricap

    #methods

    def cevre_hesap(self):
        return 2 * self.pi * self.yaricap

    def alan_hesap(self):
        return (self.pi) * (self.yaricap**2)


c1 = Circle() # yaricap=1
c2 = Circle(5) # yaricap = 5 yaptık

print(f"c1: alan {c1.alan_hesap()}, çevre = {c1.cevre_hesap()}")
print(f"c2: alan {c2.alan_hesap()}, çevre = {c2.cevre_hesap()}")


