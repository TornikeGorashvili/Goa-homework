import time

# start_fly = input("გსურთ ფრენის დაწყება? (დიახ/არა): ")
# if start_fly == "დიახ":
    
#  timer_duration = 1
#  print(timer_duration)
#  timer_duration = timer_duration + 1
#  time.sleep(1)
 
 
def minute_timer():
    timer = 60  
    while timer > 0:
     print(timer)
     time.sleep(1)
     timer -= 1
    
print("ფრენა დასრულებულია. გმადლობთ რომ გამოიყენათ ჩვენი ავიაკომპანია")
