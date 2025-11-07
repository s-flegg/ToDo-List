def edit_task(task_list, title, new_title=None, description=None, due_date=None, completed=None, priority=None):
    """
    Edits the current list, specifically one task.

    This function edits a single task in the given task list and returns the updated list.
    It is assumed that the title element serves as a UID

    Parameters:
        task_list (list): The list of all tasks
        title (str): Title of the task to be changed
        new_title (str or None): The new title of the task
        description (str or None): The task description
        due_date (object or None): The datetime.datetime that the task is due
        completed (bool or None): True if the task is completed
        priority (int or None): Priority level from 1-5, 1 is most important

    Returns:
        list: Updated task list with the edited task
    """

    if len(task_list) == 0:
        return []

    # find specified task
    task = None
    for t in task_list:
        if t["Title"] == title:
            task = t
            break

    if task is None:
        raise ValueError("The given title is not in the task list")


    if new_title is not None:
        task["Title"] = new_title
    if description is not None:
        task["Description"] = description
    if due_date is not None:
        task["Due Date"] = due_date
    if completed is not None:
        task["Completed"] = completed
    if priority is not None:
        task["Priority"] = priority

    return task_list
