x1=int(input("x1"))
x2=int(input("x2"))
x3=int(input("x3"))
x4=int(input("x4"))
x5=int(input("x5"))
y1=int(input("y1"))
y2=int(input("y2"))
y3=int(input("y3"))
y4=int(input("y4"))
y5=int(input("y5"))

son1=x1+x2+x3+x4+x5
print(f"x toplam {son1}")

son2=y1+y2+y3+y4+y5
print(f"y toplam {son2}")

son3=x1*x1+x2*x2+x3*x3+x4*x4+x5*x5
print(f"x2 toplam {son3}")

son4=y1*x1+y2*x2+y3*x3+y4*x4+y5*x5

print(f"x y carpım toplam {son4}")

son5 = (5*son4-(son1*son2)) / ((5*son3)-(son1*son1))
print(f"a zimbirtisi toplam {son5}")


