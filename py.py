def add(a, b): # +
    c = (float(a) + float(b))
    print (c)
    return (c)

def myltiply(a, b): # * 
    c = (float(a) * float(b))
    print (c)
    return (c)

def divide (a, b): # /
    c = (float(a) / float(b))
    print (c)
    return (c)

def substract(a, b): # -
    c= (float(a) - float(b))
    print (c)
    return (c)

num = input("Введите выражение ")
if len(num) >= 4:
    num1 = num.split()
    match num1[1]:
        case "+":
            add(num1[0], num1[2])
        case "-":
            substract(num1[0], num1[2])
        case "*":
            myltiply(num1[0], num1[2])
        case "/":
            divide(num1[0], num1[2])
        case " ":
            print ("Неверное выражение")
else:
    match num[1]:
        case "+":
            add(num[0], num[2])
        case "-":
            substract(num[0], num[2])
        case "*":
            myltiply(num[0], num[2])
        case "/":
            divide(num[0], num[2])
        case " ":
            print ("Неверное выражение")
