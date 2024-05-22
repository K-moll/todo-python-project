# tests/test_todo.py
import unittest
from todo import Todo

class TestTodo(unittest.TestCase):
    def setUp(self):
        self.todo = Todo()

    def test_add_task(self):
        self.assertTrue(self.todo.add_task("Task 1"))
        self.assertFalse(self.todo.add_task("Task 1"))  # Task already exists

    def test_remove_task(self):
        self.todo.add_task("Task 1")
        self.assertTrue(self.todo.remove_task("Task 1"))
        self.assertFalse(self.todo.remove_task("Task 1"))  # Task doesn't exist

    def test_list_tasks(self):
        self.todo.add_task("Task 1")
        self.todo.add_task("Task 2")
        self.assertEqual(self.todo.list_tasks(), ["Task 1", "Task 2"])

if __name__ == "__main__":
    unittest.main()
