import datetime

def get_date():
    """
    Has the user enter the datetime and converts to a datetime.datetime object

    Return:
        obj: datetime.datetime
    """
    y = None
    m = None
    d = None
    h = None

    run = True # used to ensure a valid input is gotten from the user
    while run:
        try:
            y = int(input("Enter the year the task is due: "))
            m = int(input("Enter the month the task is due: "))
            d = int(input("Enter the day the task is due: "))
            h = int(input("Enter the hour the task is due: "))
            run = False
        except:
            print("Please only enter numbers.")

    return datetime.datetime(y, m, d, h)