def add_task(tasks, task):
    tasks.append(task)
    print("Task Added!")

def display_tasks(tasks):
    if tasks:
        print("Tasks: ")
        for index,t in enumerate(tasks, start=1):
            print(f"{index}. {t}")
    else:
        print("Task list is empty!")
        

def remove_task(tasks):
    if not tasks:
        print("Task list is empty!")
    try:
        task_no = int(input("Enter the task u want to remove:\n"))
        if task_no not in range(1,len(tasks)+1):
            print(f"Please enter a task number between 1 and {len(tasks)}")
        else:
            tasks.pop(task_no-1)
            print("Task Removed!")
    except ValueError:
        print("Invalid Input! Enter a number")
            
    
print("Welcome to the Task Manager!\n")
tasks = []
while True:
    try:
        choice = int(input("Choose an action: \n1. Add a Task \n2. View Tasks \n3. Remove a task \n4. Quit\n"))
        if(choice==1):
            task = input("Enter the task: ")
            add_task(tasks, task)
        elif(choice==2):
            display_tasks(tasks)
        elif(choice==3):
            remove_task(tasks)
        elif(choice==4):
            break
        else:
            print("Input must be between 1-4! Try Again")
    except ValueError:
        print("Input must be a number!")
        continue
print("Task Manager closed!")
    
