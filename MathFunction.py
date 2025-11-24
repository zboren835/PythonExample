def Add(X,Y):
    print(f"Add:{X+Y}")

def Sub(X,Y):
    print(f"Sub:{X-Y}")

def Miv(X,Y):
    print(f"Miv:{X*Y}")

def Division(X,Y):
    print(f"Division:{X/Y}")

def MathPrepare(Prepare,X,Y):
    match Prepare:
        case 1:
            Add(X,Y)
        case 2:
            Sub(X,Y)
        case 3:
            Miv(X,Y)
        case 4:
            Division(X,Y)