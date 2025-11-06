from remove_task import remove_task

def test_remove_missing_task():
    """Assumes that a missing task should not raise an error"""
    task_list = []
    assert remove_task(task_list, "a") == []

def test_remove_task():
    assert remove_task(
        [
            {
                "Title": "aaa",
                "Description": "bbb",
                "Due Date": "Example datetime",
                "Completed": False,
                "Priority": 3
            }
        ],
        "aaa"
    ) == []