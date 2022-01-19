
# 1.Пользователь вводит два числа и операцию (+, -, *,/) в одну строку, а программа выдает результатэтой операции.

a, b, operation = map (str,input().split())

num_1 = int (a)
num_2 = int (b)

if operation == "+":
    
    print (num_1 + num_2)

  
elif operation == "-":
    print (num_1 - num_2)
    
elif operation == "*":
    print (num_1 * num_2)
    
elif operation == "/":
    if num_1 == 0 or num_2 == 0:
        print("На ноль делить нельзя!")
    else:
        
        print (num_1 / num_2)
