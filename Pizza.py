import random
import turtle
import math
from turtle import *
turtle.speed(0)
turtle.speed(0)

print('''
Pizza menu:

Pizza sizes:
    Small - £8.00
    Medium - £10.00
    Large - £12.00
    Extra large - £14.00
   
Base types:
    Thin crust
    Thick crust
    Stuffed crust (+50p)
   
Sauces:
    Tomato
    BBQ

Cheeses:
    Regular
    Vegan
    Three Cheese (+50p)

Toppings:

    Regular toppings(+50p each):
    - Basil
    - Sweetcorn
    - Pineapple
   
    Premium toppings(+ £1 each):
    - Pepperoni
    - Ham
    - Beef
''')
#draws pizza base
def base(size):
    color('black', 'tan')
    penup()
    right(90)
    forward(size)
    left(90)
    pendown()
    begin_fill()
    turtle.circle(size, extent=None, steps=None)
    end_fill()
    penup()
    left(90)
    forward(size)
    right(90)
    pendown()
   
#Draws pizza sauce    
def sauce(size,colour):
    color('black', colour)
    penup()
    right(90)
    forward(size)
    left(90)
    begin_fill()
    turtle.circle(size)
    end_fill()

   
#Draws a splatter of cheese
def cheese(cheesetype,r):
    color(cheesetype, cheesetype)
    for i in range(12):
        begin_fill()
        circle(r/2-2)
        end_fill()
        right(30)

   
#Asks a series of questions to determine the sizxe and type of pizza base
def choosesize():
    sizename = input("Would you like small(S),medium(M),large(L), or extra large(XL)")
    ss = sizename[0]
    if ss.upper() == "S":
        s = 250
        p = 8.00
    elif ss.upper() == "M":
        s = 300
        p = 10.00
    elif ss.upper() == "L":
        s = 350
        p = 12.00
    else:
        s = 400
        p = 14.00
    crustname = 4
    stuffed = input("Type (S) for stuffed crust or (R) for regular: ")
    sc = stuffed[0]
    if sc.upper() == "S":
        crustname = "2"
        c = s * 0.1
        p = p + 0.50
    while crustname != "1" and crustname != "2":
        crustname = str(input("Would you like (1) - Thin crust or (2) - thick crust?"))
        if crustname == "1":
            c = s * 0.05
        elif crustname == "2":
            c = s * 0.1
        else:
            print("Please choose between 1 & 2")
    return (s,c,p)

def sauceandcheese(p):
    saucetype = input("Do you want (T)- Tomato sauce or (B)- BBQ sauce? ")
    st = saucetype[0]
    if st.upper() == "B":
        saucecolour = 'saddlebrown'
    else:
        saucecolour = 'brown'
    cheesetype = str(input("Would you like regular cheese (C) Vegan cheese (V) or three cheese(T)"))
    cht = cheesetype[0]
    if cht.upper() == "V":
        cheesecolour = 'khaki'
    elif cht.upper() == "T":
        cheesecolour = 'orange'
        p = p + 0.50
    else:
        cheesecolour = 'gold'
    return saucecolour,cheesecolour,p

def chunks(min,max,outsidecolour,insidecolour):
    color(outsidecolour,insidecolour)
    x = random.randint(min,max)
    begin_fill()
    for i in range (4):
        forward(x)
        right(90)
    end_fill()

#lets them choose the type of pizza    
def toppings(radius,price):
    print("A list of toppings will now show. If you would like the topping, type (Y) ")
    basil = input("Basil? ")
    p = basil[0]
    if p.upper() == "Y":
        scatter(2,10,'green','dark green',radius)
        price = price + 0.50
    corn = input("Sweetcorn? ")
    p = corn[0]
    if p.upper() == "Y":
        scatter(10,10,'yellow','orange',radius)
        price = price + 0.50
    pineapple = input("Pineapple? ")
    p = pineapple[0]
    if p.upper() == "Y":
        scatter(15,30,'orange','yellow',radius)
        price = price + 0.50
    pepperoni = input("Pepperoni? ")
    p = pepperoni[0]
    if p.upper() == "Y":
        ron(radius)
        price = price + 1.00
    ham = input("Ham? ")
    p = ham[0]
    if p.upper() == "Y":
        scatter(20,30,'red','pink',radius)
        price = price + 1.00
    Beef = input("Beef? ")
    p = Beef[0]
    if p.upper() == "Y":
        scatter(10,30,'brown','saddlebrown',radius)
        price = price + 1.00
    return price
       
   

def ron(R):
    penup()
    right(60)
    x = R/3
    color('maroon','brown')
    begin_fill()
    dot(x)
    end_fill()
    penup()
    for i in range (6):
        right(60)
        y = 2 * x - 15
        forward (y)
        pendown()
        right(270)
        color('brown','maroon')
        begin_fill()
        circle(x/2)
        left(270)
        end_fill()
        penup()
        forward(-y)
    for i in range (10):
        right(36)
        y = 3 * x - 10
        forward (y)
        pendown()
        right(270)
        color('brown','maroon')
        begin_fill()
        circle(x/2)
        left(270)
        end_fill()
        penup()
        forward(-y)
    left(60)

# Scatters toppings across the pizza
def scatter(minimum,maximum,out,ins,radius):
    q = 2*360/(int(radius/minimum))
    for i in range(int(radius/minimum)):
        R = radius
        R = int(math.sqrt(R-maximum))
        X = random.randint(7,R)
        X = X * X
        right(q)
        forward(X)
        offset = random.randint(0,360)
        right(offset)
        pendown()
        chunks(minimum,maximum,out,ins)
        penup()
        left(offset)
        forward(-X)
    for i in range (6):
        right(60)
        X = random.randint(1,int(radius-maximum))
        forward(X)
        offset = random.randint(0,360)
        right(offset)
        pendown()
        chunks(minimum,maximum,out,ins)
        penup()
        left(offset)
        forward(-X)


       
def pizza():
    s,c,price = choosesize()
    print(price)
    base(s)
    radius = s - c
    scolour,ccolour,price = sauceandcheese(price)
    print(price)
    sauce(radius,scolour)
    print(price)
    penup()
    left(90)
    forward(radius)
    right(90)
    pendown()
    cheese(ccolour,radius)
    price = toppings(radius,price)
    price = float(price)
    x = round(price, 1)
    print("Total cost of the pizza is £",str(x)+"0")
pizza()

done()
