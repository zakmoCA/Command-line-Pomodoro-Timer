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
      > the headers and pomodoro are written correctly
      > the string that the write method is called with starts with the task name, and has the structure we expect
    """
    @patch('start_pomodoro.run_pomodoro')
    @patch('builtins.input')
    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.isfile')
    def test_write_pomodoro_to_csv(self, isfile_mock, mock_open, input_mock, run_pomodoro_mock):
        # Define the behavior of the mocks
        input_mock.side_effect = ['test_task', '25', '5']
        run_pomodoro_mock.return_value = None
        isfile_mock.return_value = False  # mock isfile should return False, to simulate non-existent csv file (first pomodoro) 


        # Call the function to test
        start()

        # Get all calls to write
        write_calls = mock_open().write.call_args_list

        # The first call should be writing the headers
        call_args = write_calls[0][0][0]
        print(call_args)
        # Check that first call writes headers, or statement for checking newline characters in unix-based systems vs windows
        self.assertTrue(call_args == 'Task Name,Start Time,End Time,Duration\n' or call_args == 'Task Name,Start Time,End Time,Duration\r\n')

        # The second call should be writing the pomodoro
        call_args = write_calls[1][0][0]
        self.assertTrue(call_args.startswith('test_task,'))
        self.assertTrue(call_args.endswith('\n'))
        

if __name__ == '__main__':
    unittest.main()
