import unittest
from app.io import input
from app.io import output


class TestInput(unittest.TestCase):
    def test_read_file_builtin_file_not_found(self):
        """
        Test if file was found.
        """
        with self.assertRaises(FileNotFoundError):
            input.read_file_builtin("test_1.txt")

    def test_read_file_builtin_found(self):
        """
        Test if file was found.
        """
        result = input.read_file_builtin("test.txt")
        self.assertIsNot(result, None)

    def test_read_file_builtin(self):
        """
        Test that built in functionality reads file correctly
        """
        data_to_write = "1234 ohhhh"
        output.write_file_builtin("test.txt", data_to_write)
        result = input.read_file_builtin("test.txt")
        self.assertEqual(result, data_to_write)

    def test_read_file_pandas(self):
        """
        Test that Pandas functionality reads file correctly
        """
        data_to_write = "1234 ohhhh"
        output.write_file_builtin("test.txt", data_to_write)
        result = input.read_file_pandas("data/built_in_file.txt")
        self.assertEqual(result, data_to_write)


if __name__ == '__main__':
    unittest.main()
