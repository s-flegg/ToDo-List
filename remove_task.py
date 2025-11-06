def remove_task(task_list, title):
    """
    Removes a task from the list

    Args:
        task_list(list): The list of all tasks
        title(str): The title of the task to be removed

    Returns:
        list: Updated task list with the task removed
    """

    return [t for t in task_list if t["Title"] != title]