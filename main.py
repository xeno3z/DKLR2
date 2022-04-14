import math

sides = [3, 2, 4, 7, 5, 12, 11, 13, 15, 16, 14, 14]
sides = sorted(sides, reverse=True)
smax = 0
for i in range(len(sides)):
    for j in range(i + 1, len(sides)):
        for k in range(j + 1, len(sides)):
            a = sides[i]
            b = sides[j]
            c = sides[k]
            if a + b > c and a + c > b and b + c > a:
                p = (a + b + c) / 2
                s = (p * (p - a) * (p - b) * (p - c)) ** (1 / 2)
                if s > smax:
                    smax = s

print("MAX S TRIANGLE", smax)

a2 = int(input("FirstC = "))
b2 = int(input("SecondC = "))
c2 = int(input("ThirdC = "))
D = b2**2 - 4 * a2 * c2
if D > 0:
    x1 = (-b2 + math.sqrt(D)) / (2 * a2)
    x2 = (-b2 - math.sqrt(D)) / (2 * a2)
    print("x1 = " + str(x1))
    print("x2 = " + str(x2))
elif D == 0:
    x = (-b2 / (2 * a2))
    print("x = " + str(x))
else:
    print("No answer")
