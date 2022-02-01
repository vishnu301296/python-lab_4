num = int(input("enter the number of the positive integers : "))

def fractional(x):
    if x <= 0:
        return 0 

    else:
       return  x + fractional(x-2)

     
print("the number of the positive integers ",fractional(num))