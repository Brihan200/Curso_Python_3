# Sucesion Finobacci
x , y = 0, 1
while x < 1650:
    print(x, y, end=" ")
    x = x + y
    y = x + y
