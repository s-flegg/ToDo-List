from edit_task import edit_task

def test_populated_list():
    tasks = [ 
        {
            "Title": "1",
            "Description": "bbbbbb",
            "Due Date": 'example',
            "Completed": False,
            "Priority": 1,
        },
        {
            "Title": "2",
            "Description": "bbbbbb",
            "Due Date": 'example',
            "Completed": False,
            "Priority": 1,
        },
        {
            "Title": "3",
            "Description": "bbbbbb",
            "Due Date": 'example',
            "Completed": False,
            "Priority": 1,
        },
    ]

    assert edit_task(tasks, '2', 'n', 'desc', 'example2', True, 5) == [
        {
            "Title": "1",
            "Description": "bbbbbb",
            "Due Date": 'example',
            "Completed": False,
            "Priority": 1,
        },
        {
            "Title": "n",
            "Description": "desc",
            "Due Date": 'example2',
            "Completed": True,
            "Priority": 5,
        },
        {
            "Title": "3",
            "Description": "bbbbbb",
            "Due Date": 'example',
            "Completed": False,
            "Priority": 1,
        },
    ]
    assert edit_task(tasks, '3', priority=3) == [
        {
            "Title": "1",
            "Description": "bbbbbb",
            "Due Date": 'example',
            "Completed": False,
            "Priority": 1,
        },
        {
            "Title": "n",
            "Description": "desc",
            "Due Date": 'example2',
            "Completed": True,
            "Priority": 5,
        },
        {
            "Title": "3",
            "Description": "bbbbbb",
            "Due Date": 'example',
            "Completed": False,
            "Priority": 3,
        },
    ]


def test_empty_list():
    tasks = []

    assert edit_task(tasks, 'f', 'd') == []
