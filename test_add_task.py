from add_task import add_task
import datetime

def test_add_task():
    task_list = []
    date = datetime.datetime(2025, 11, 5, 15)
    assert add_task(
        task_list,
        "aaa",
        "bbb",
        date,
        False,
        3,
    ) == [
        {
            "Title": "aaa",
            "Description": "bbb",
            "Due Date": date,
            "Completed": False,
            "Priority": 3
        }
    ]