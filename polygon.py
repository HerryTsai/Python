import random
import matplotlib.pyplot as plt

class Point:
    def __init__(self, x0 = 0, y0 = 0):
        self.x = x0
        self.y = y0
        self.order = 0

def randPoint(num):
    p = {}
    for i in range(num):
        p[i] = Point(random.randint(0,100),random.randint(0,100))
        for ii in range(i):
            if p[i].x == p[ii].x and p[i].y == p[ii].y:
                p[i] = Point(random.randint(0,10),random.randint(0,10))
                ii = 0
    return p

def sideLong(p0, p1):
    return (p0.x - p1.x)**2 + (p0.y - p1.y)**2

def cosValue(pLast, pNow, pi):
    a = sideLong(pLast, pNow)
    b = sideLong(pi, pNow)
    c = sideLong(pLast, pi)
    return (a + b - c)/(2*(a**(1/2))*(b**(1/2)))

p = randPoint(50)

last = nextOne = 0
now = mincos = 1
count = 0

while (p[now].order == 0):
      
        for i in range(50):
            if i == now:
                continue
            
            cos1 = cosValue(p[last], p[now], p[i])
            if cos1 == -1 and sideLong(p[last], p[i]) > sideLong(p[last], p[now]):
                now = i
                break
            else:
                if mincos > cos1:
                    mincos = cos1
                    nextOne = i

        count = count + 1
        p[now].order = count
        last = now
        now = nextOne
        mincos = 1
        i = 0

noworder = p[now].order
for i in range(50):
    minorder = i
    for j in range(i + 1, 50):
        if p[j].order < p[minorder].order :
            minorder = j
    if i != minorder :
        porder = p[i]
        p[i] = p[minorder]
        p[minorder] = porder
   
for i in range(50):
    if p[i].order >= noworder :
        print(i,p[i].x,p[i].y,p[i].order)
        plt.plot(p[i].x,p[i].y,"bo")
    else:
        plt.plot(p[i].x,p[i].y,"ro")

plt.show()

