##
# @file todo.py
# @brief This file contains the Todo class which implements a simple to-do list management.

class Todo:
    ##
    # @brief Constructor for the Todo class.
    #
    # Initializes an empty list to store tasks.
    def __init__(self):
        self.tasks = []

    ##
    # @brief Adds a task to the to-do list.
    #
    # @param task The task to be added.
    # @return True if the task was added, False if the task already exists.
    def add_task(self, task):
        if task not in self.tasks:
            self.tasks.append(task)
            return True
        return False

    ##
    # @brief Removes a task from the to-do list.
    #
    # @param task The task to be removed.
    # @return True if the task was removed, False if the task does not exist.
    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            return True
        return False

    ##
    # @brief Lists all tasks in the to-do list.
    #
    # @return A list of all tasks.
    def list_tasks(self):
        return self.tasks

if __name__ == "__main__":
    todo = Todo()
    todo.add_task("Write code")
    todo.add_task("Test code")
    print("Tasks:", todo.list_tasks())
    todo.remove_task("Write code")
    print("Tasks after removal:", todo.list_tasks())
