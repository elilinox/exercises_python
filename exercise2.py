def funktion(x,y) :
    funktion = x/y
    if x%y == 0:
        print("x ist durch y teilbar")
    elif x%y == 0 and x==y:
        print("x und y sind gleich")
    elif y == 0:
        print ("Es ist nicht möglich durch 0 zu teilen!")
    else: 
        print("x ist nicht durch y teilbar")

funktion(14,7)
funktion(13,7)
funktion(13,13)
funktion(13,0)

