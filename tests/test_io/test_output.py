import unittest

import pandas as pd
import pandas.testing as pd_testing

from app.io import input
from app.io import output


class TestOutput(unittest.TestCase):

    def test_read_file_pandas_file_not_found(self):
        """
        Test if file was found.
        """
        with self.assertRaises(FileNotFoundError):
            input.read_file_pandas("test_1.csv")

    def test_read_file_pandas(self):
        """
        Test that Pandas functionality reads file correctly
        """
        data_to_write = {'Hello': ['World', 'there']}
        df = pd.DataFrame(data_to_write)
        df.to_csv("test.csv", index=False)
        output_df = input.read_file_pandas("test.csv")
        pd_testing.assert_frame_equal(output_df, df)


if __name__ == '__main__':
    unittest.main()
