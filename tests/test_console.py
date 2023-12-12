#!/usr/bin/python3
""" console testing module"""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestConsole(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_all(self, mock_stdout):
        with patch('builtins.input', side_effect=['create BaseModel', 'all BaseModel', 'quit']):
            HBNBCommand().cmdloop()
        output = mock_stdout.getvalue().strip()
        self.assertTrue("[BaseModel]" in output)


if __name__ == '__main__':
    unittest.main()
