import csv

def load_list():
    
    with open('file.csv', newline='') as f:
        reader = csv.reader(f)
        task_list = list(reader)

    return task_list
