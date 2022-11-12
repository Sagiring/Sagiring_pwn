
a = 2947
b = 3772
s = 100
t = 100
while True:
    print(f"s = {s},t = {t}")
    if (abs(s*a - t*b) == 1) :
        print(f"已找到s = {s},t = {t}")
        break
    if(s >= 1000):
        t += 1
        s = 100
    if(t >= 1000):
        print("没找到")
        break
    s += 1