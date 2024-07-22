# #  table generator(ruchi) 
def table_generator():
    
    
     num=int(input("which number table do you want: "))
     
     for a in range(1,11):
          print(str(num) + "*" +str(a) + "=" + str(num*a))
    
 #   # # testing the coding
table_generator() 
         