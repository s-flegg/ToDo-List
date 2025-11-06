def sort_by(task_list, sort_by, ascending):
    #what to sort by (this might work)
    if sort_by == "Title":
        index = 0
    if sort_by == "Description":
        index = 1
    if sort_by == "Due Date":
        index = 2
    if sort_by == "Completed":
        index = 3
    if sort_by == "Priority":
        index = 4
        #bubble sort
    if ascending = True:
        n = len(task_list)
        for i in range(n-1):
            swapped = False
        for j in range(n-i-1):
            if mylist[j][index] > mylist[j+1][index]:
                mylist[j][index], mylist[j+1][index] = mylist[j+1][index], mylist[j][index]
                swapped = True
        if not swapped:
            break
    if ascending == False
        n = len(task_list)
        for i in range(n-1):
            swapped = False
        for j in range(n-i-1):
            if mylist[j][index] < mylist[j+1][index]:
                mylist[j][index], mylist[j+1][index] = mylist[j+1][index], mylist[j][index]
                swapped = True
        if not swapped:
            break
    return task_list
