#!/usr/bin/python3
""" console testing module"""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.stdout_patch = patch('sys.stdout', new_callable=StringIO)
        self.mock_stdout = self.stdout_patch.start()

    def tearDown(self):
        self.stdout_patch.stop()

    def test_quit_command(self):
        with patch('builtins.input', return_value='quit'):
            cmd = HBNBCommand()
            cmd.cmdloop()
            self.assertEqual(self.mock_stdout.getvalue().strip(), '')

    def test_create_command(self):
        with patch('builtins.input', side_effect=['create BaseModel', 'EOF']):
            cmd = HBNBCommand()
            cmd.cmdloop()
            output = self.mock_stdout.getvalue().strip()
            self.assertTrue(output.startswith('(hbnb) '))
            self.assertTrue(output.endswith('(hbnb)'))

    def test_all_command(self):
        with patch('builtins.input', side_effect=['all', 'EOF']):
            cmd = HBNBCommand()
            cmd.cmdloop()
            self.assertTrue('(hbnb) ' in self.mock_stdout.getvalue().strip())

    def test_count_command(self):
        with patch('builtins.input', side_effect=['count BaseModel', 'EOF']):
            cmd = HBNBCommand()
            cmd.cmdloop()
            self.assertTrue('(hbnb) ' in self.mock_stdout.getvalue().strip())

    def test_show_command(self):
        with patch('builtins.input', side_effect=['show BaseModel 123', 'EOF']):
            cmd = HBNBCommand()
            cmd.cmdloop()
            self.assertTrue('(hbnb) ' in self.mock_stdout.getvalue().strip())

    def test_destroy_command(self):
        with patch('builtins.input', side_effect=['destroy BaseModel 123', 'EOF']):
            cmd = HBNBCommand()
            cmd.cmdloop()
            self.assertTrue('(hbnb) ' in self.mock_stdout.getvalue().strip())

    def test_update_command(self):
        with patch('builtins.input', side_effect=['update BaseModel 123 name "John"', 'EOF']):
            cmd = HBNBCommand()
            cmd.cmdloop()
            self.assertTrue('(hbnb) ' in self.mock_stdout.getvalue().strip())

    def test_custom_count_command(self):
        with patch('builtins.input', side_effect=['BaseModel.count()', 'EOF']):
            cmd = HBNBCommand()
            cmd.cmdloop()
            self.assertTrue('(hbnb) ' in self.mock_stdout.getvalue().strip())

    def test_custom_all_command(self):
        with patch('builtins.input', side_effect=['BaseModel.all()', 'EOF']):
            cmd = HBNBCommand()
            cmd.cmdloop()
            self.assertTrue('(hbnb) ' in self.mock_stdout.getvalue().strip())

    def test_custom_show_command(self):
        with patch('builtins.input', side_effect=['BaseModel.show(123)', 'EOF']):
            cmd = HBNBCommand()
            cmd.cmdloop()
            self.assertTrue('(hbnb) ' in self.mock_stdout.getvalue().strip())

    def test_custom_destroy_command(self):
        with patch('builtins.input', side_effect=['BaseModel.destroy(123)', 'EOF']):
            cmd = HBNBCommand()
            cmd.cmdloop()
            self.assertTrue('(hbnb) ' in self.mock_stdout.getvalue().strip())

    def test_custom_update_command(self):
        with patch('builtins.input', side_effect=['BaseModel.update(123, name, "John")', 'EOF']):
            cmd = HBNBCommand()
            cmd.cmdloop()
            self.assertTrue('(hbnb) ' in self.mock_stdout.getvalue().strip())

if __name__ == '__main__':
    unittest.main()
