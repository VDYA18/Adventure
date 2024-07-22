
# factorial
def factorial_giver():
    
    num=int(input("enter any number "))
    
    result=1
    while num > 0:
        result*=num
        num-=1
        
    return result


    
# testing code
a=factorial_giver()
print(a) 




    

   
