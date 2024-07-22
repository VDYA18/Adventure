import time

current_time=time.strftime("%H:%M")

if current_time>="06:00" and current_time<="11:59":
    print("good morning sir/ma'am")  
    
if current_time>="12:00" and current_time<="17:00":
    print("good afternoon sir/ma'am") 
    
else:
    print("good evening sir/ma'am")
