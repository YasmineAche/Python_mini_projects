from math import floor

WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

class Model:
    def __init__(self):
        self.selected_time = WORK_MIN * 60
        self.initial_time = WORK_MIN * 60
        self.reps = 1

    @staticmethod
    def count_remaining_time(seconds:int) -> str:
        minutes = floor(seconds / 60)
        seconds = seconds % 60
        time = f"{minutes:02d}:{seconds:02d}"
        return time

    def get_session_type(self) -> str:
        """
        Return the type of session for current rep
        Logic Pomodoro :
             Reps 1, 3, 5, 7 -> WORK
             Reps 2, 4, 6    -> SHORT BREAK
             Rep 8           -> LONG BREAK
        """
        if self.reps % 8 == 0:
            return "Long Break"
        elif self.reps % 2 == 0:
            return "Short Break"
        else:
            return "Work"

    def manage_reps(self, session_type) -> None:
        """Determine session type and update selected_time"""

        if session_type == "Long Break":
            self.selected_time = LONG_BREAK_MIN * 60
        elif session_type == "Short Break":
            self.selected_time = SHORT_BREAK_MIN * 60
        else:
            self.selected_time = WORK_MIN * 60
