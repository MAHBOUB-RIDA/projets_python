import time
print("⏳ Welcome to the Pomodoro Time !")
mins = input("Enter time in minutes : ") # 20 min
mins = int(mins)

# Calculate total seconds
total_secend = mins*60      # 1200 : 1199 1198 1197

while total_secend > 0 :
    
    # calculate minutes
    mins = total_secend // 60
        
    # calculate remaining secends
    secs = total_secend % 60
    
    #03:20
    clock = f"{mins:02d}:{secs:02d}"
    print(f"\rTime Remaining : {clock}", end="")
    
    # sleep
    time.sleep(1)
    total_secend-=1

print("\ntime's UP , take a break  ")