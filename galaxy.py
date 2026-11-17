import turtle
import colorsys
import math
import random

random.seed(7)
TILT = 0.45
screen = turtle.Screen()
screen.setup(780, 480)
screen.bgcolor("#03030b")
screen.colormode(1.0)
screen.tracer(5, 0)  # 核心調整：每畫 25 個點才刷新一次畫面，兼顧流暢度與漸進感

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.penup()

def glow(h, v=1.0):
    return colorsys.hsv_to_rgb(h % 1, 0.7, v)

def place(x, y):
    y *= 0.55
    c, s = math.cos(TILT), math.sin(TILT)
    t.goto(x * c - y * s, y * c + x * s)

def stars():
    t.clear()
    for _ in range(140):
        x = random.randint(-385, 385)
        y = random.randint(-235, 235)
        t.goto(x, y)
        t.dot(random.randint(2, 4), glow(0.7, 0.3))

def dust():
    for _ in range(300):
        r = random.gauss(0, 120)
        a = random.uniform(0, math.tau)
        place(r * math.cos(a), r * math.sin(a))
        t.dot(random.randint(2, 4), glow(0.1, 0.25))

def arms(count):
    for i in range(count):
        for k in range(4):
            d = i / count
            a = k * math.pi / 2 + d * 5.5
            r = 10 + d * 290
            s = 8 + d * 22
            x = r * math.cos(a) + random.gauss(0, s)
            y = r * math.sin(a) + random.gauss(0, s)
            place(x, y)
            hue = 0.13 - d * 0.55
            v = random.uniform(0.6, 1.0)
            size = random.randint(2, 4)
            t.dot(size, glow(hue, v))

def core():
    for _ in range(260):
        r = random.gauss(0, 26)
        a = random.uniform(0, math.tau)
        place(r * math.cos(a), r * math.sin(a))
        t.dot(random.randint(2, 5), glow(0.12))

def sparkle():
    for _ in range(40):
        r = random.gauss(0, 150)
        a = random.uniform(0, math.tau)
        place(r * math.cos(a), r * math.sin(a))
        t.dot(random.randint(5, 8), "white")

def main():
    stars()
    dust()
    arms(900)
    core()
    sparkle()
    t.goto(0, 0)
    t.dot(26, "#fff3c4")
    screen.update()  # 把最後不足 25 個點的尾數也刷新顯示出來
    turtle.done()

if __name__ == "__main__":
    main()
