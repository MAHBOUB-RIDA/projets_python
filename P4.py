tasks=[]
print("📜 Welcome to The To-DO List App")

while True:
    print("---------------------------")
    print("choose an option : ")
    print("1: Add task ")
    print("2: View task ")
    print("3: Delete task ")
    print("4: Exit ")
    print("---------------------------")
    
    choice = input("Enter your choice (1-4) : ")
    
    # Add task
    if choice == "1": 
        
        # We ask the user to enter all the tasks
        value = input("Enter a task : ")
        tasks.append(value)
        print("✅ Task added")
    
    # View task   
    elif choice == "2":
        
        # If the list is emply
        if not tasks:
            print(" No tasks yet ❕")
        else:
            # 1 task1
            # 2 task2
            # 3 task3
            print("Your tasks 📑")
            
            # Show all tasks
            i=1
            for data in tasks:
                print(i,data)
                i+=1
    
    # delete task
    elif choice == "3":
        
        # Check if there are any tasks
        if not tasks:
            print("No tasks to delete ❕")
            
        else:
            # Display the tasks with numbers for the user to chooce from
            print("Your tasks 📑")
            i=1
            for data in tasks :
                print(i, data)
                i+=1
                
            # Ask the user for the number of the task they want to delete
            task_number = input("Enter task number to delete : ")
            task_number = int(task_number) # 1 : 0
            
            if task_number >= 1 and task_number <= len(tasks):
                
                deleted = tasks.pop(task_number)
                print(f"Deleted task is {deleted}")
                
            else:
                print("Invalid value ❕❕")
    
    # Exit
    elif choice == "4":
        print("GoodBuye 👋")
        break
    else:
        print("invalid choice : Try again 🔄")