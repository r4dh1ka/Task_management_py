def task():
    list =[]
    print("--------WELCOME TO TASK MANAGEMENT SYSTEM--------")

    total_task= int(input("how many task you want to add = "))
    for i in range(0,total_task):
        task_name=input(f"enter task {i} =")
        list.append(task_name)

    print(f"Today's task are \n {list}")

    while True:
        operation=int(input("enter 1-add\nenter 2-update\nenter3-delete\nenter4-view\nenter5-exit"))

        if operation == 1:
            add=input("enter task you want to input =")
            list.append(add)
            print(f"task {add} has been sucessfully added ")

        elif operation == 2:
            update_val=input("enter task you want to update =")
            if update_val in list:
                up=input("enter new task =")
                ind=list.index(update_val)
                list[ind]=up
                print(f"task {up} updated sucessfully")

        elif operation == 3:
            del_val=input("enter task you want to delete =")
            if del_val in list:
                ind=list.index(del_val)
                del list[ind]
                print(f"task {del_val} sucessfully deleted ")

        elif operation == 4:
            print(f"total tasks = {list}")

        elif operation == 5:
            print("closing the program ")
            break

        else :
            print("invalid operation ")
task()


