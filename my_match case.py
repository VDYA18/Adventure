# match case statement

num=(int(input("enter any number: ")))   

match num :
    
    case _ if num<0:
        print("num is negative")
        
    case _ if (num>0 and num<10):
        print("num is place between 11 to 20")
        
    case _ if (num>11 and num<20):
        print("num is place between 11 to 20")
        
    case _ if (num>21 and num<30):
        print("num is place between 21 to 30")
        
    case _ if (num>31 and num<40):
        print("num is place between 31 to 40")
        
    case _ if (num>41 and num<50):
        print("num is place between 41 to 50")
        
    case _ if (num>51 and num<60):
        print("num is place between 51 to 60")
        
    case _ if (num>61 and num<70):
        print("num is place between 61 to 70")
        
    case _ if (num>71 and num<80):
        print("num is place between 71 to 80")
        
    case _ if (num>81 and num<90):
        print("num is place between 81 to 90")
        
    case _ if (num>91 and num<100):
        print("num is place between 91 to 100")
    
