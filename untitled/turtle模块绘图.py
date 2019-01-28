#-*- coding: utf-8 -*-
'''
turtle 模块绘图：
是一个简单的绘图工具
提供一个小海龟，可以把它理解为一个机器人，只能听得懂有限的命令
绘图窗口的原点(0,0)在正中间 默认移动的朝向是向右
方法：
运动命令：
forward(d)  向前移动d长度
backward(d)  向后移动d长度
right(d)  向右转动d度
left(d)   向左转动d度
goto(x,y)  移动到坐标为(x,y)的位置
speed(speed) 笔画绘制的速度[0,10]
笔画控制命令：
up() 笔画抬起，在移动的时候不绘图
down() 笔画落下，在移动的时候绘图
setheading(d)  改变海龟的朝向
pensize(d)  笔画的宽度
circle(radius, extent)
绘制一个圆形，其中radius为半径，extent为度数，例如若extent为180，则画一个半圆；如要画一个圆形，可不必写第二个参数
begin_fill()  开始填充
fillcolor(colorstring) 绘制图形的填充颜色
end_fill()  结束填充
reset() 恢复所有设置

其他命令：
done  保持turtle程序不结束 程序继续执行 默认会开启一个画板
undo() 撤销上一次动作
hideturtle()  隐藏小海龟
showturtle()  显示小海龟


'''
#导入turtle库
import turtle
turtle.speed(5)
turtle.pensize(1)
turtle.forward(100)
turtle.backward(100)
turtle.right(100)
turtle.left(100)
turtle.goto(-100,-200)
turtle.up()
turtle.goto(-100,100)
turtle.down()
turtle.goto(100,-200)
#turtle.clear()
#turtle.circle(50,180)


turtle.begin_fill()
turtle.fillcolor("green")
turtle.circle(50)
turtle.end_fill()

turtle.forward(50)
turtle.undo()
turtle.hideturtle()
turtle.showturtle()


a=60
turtle.forward(a)
turtle.left(120)
turtle.forward(a)
turtle.left(120)
turtle.forward(a)
turtle.left(120)
turtle.hideturtle()

#turtle.done()

# 我的大花莽
def drawSnake(rad, angle, len, neckrad):
    for i in range(len):
        turtle.pencolor("red")
        turtle.circle(rad, angle)
        turtle.pencolor("black")
        turtle.circle(-rad, angle)
    turtle.pencolor("green")
    turtle.circle(rad, angle/2)
    turtle.pencolor("yellow")
    turtle.fd(rad)
    turtle.pencolor("purple")
    turtle.circle(neckrad+1, 180)
    turtle.pencolor("cyan")
    turtle.fd(rad*2/3)

def main():
    turtle.setup(1300, 700, 0, 0)
    pythonsize = 30
    turtle.pensize(pythonsize)
    turtle.pencolor("red")
    turtle.seth(-40)
    drawSnake(30, 80, 5, pythonsize/2)
    turtle.done()

main()
