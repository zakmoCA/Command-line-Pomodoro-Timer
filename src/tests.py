import unittest
from unittest.mock import patch, mock_open
from pomodoro_length import pomodoro_length
from run_pomodoro import run_pomodoro
from start_pomodoro import start


class TestPomodoroApp(unittest.TestCase):
    # test that my pomodoro_length function correctly handles user input
    def test_pomodoro_length(self):
        with patch('builtins.input', side_effect=['25', '5']):
            work_time, break_time = pomodoro_length()
            self.assertEqual(work_time, 25)
            self.assertEqual(break_time, 5)
    """"
    My second test checks that my start funciton correctly writes something to csv.
    I can't check the exact timestamps are 'corect' because assert_called_once_with doesn't support regex
    But I am happy in checking that;
      > the csv write method is called only once
      > the string that the write method is called with starts with the task name followed
        by a comma
      > the string ends with a newline character
    """
    @patch('start_pomodoro.run_pomodoro')
    @patch('builtins.input')
    @patch('builtins.open', new_callable=mock_open)
    def test_write_pomodoro_to_csv(self, mock_open, input_mock, run_pomodoro_mock):
        # Define the behavior of the mocks
        input_mock.side_effect = ['test_task', '25', '5']
        run_pomodoro_mock.return_value = None

        # Call the function to test
        start()

        # Check that the write method of the mock file object was called once
        # If it's not called or called more than once this will raise an error (AssertionError) 
        mock_open().write.assert_called_once()
        # Get the arguments that were passed to the 'write' method. call_args is a tuple ((positional args), {keyword dictionary})
        # String that was written to file is a positional arg, and only arg in that tuple
        # Can isolate the string by accessing first and only index of the tuple 
        call_args = mock_open().write.call_args[0][0]
        # Assert that the written string starts with our task name
        self.assertTrue(call_args.startswith('test_task,'))
        # Assert that the string ends with a newline character
        self.assertTrue(call_args.endswith('\n'))
        

if __name__ == '__main__':
    unittest.main()
