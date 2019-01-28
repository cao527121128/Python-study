#coding=utf-8

from Child import Child

def main():
    c = Child(200,100)
    print(c.money,c.faceValue,c.height)
    c.eat()
    c.play()
    #注意：父类中方法名相同，则优先调用在括号中排在最前面的父类的方法 这里优先调用Father中的func()
    c.func()




if __name__ == "__main__":
    main()
