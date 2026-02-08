import os
import sys


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.timer = None
        self.setup_events()

    def setup_events(self) -> None:
        self.view.start_timer(command=self.start_count_down)
        self.view.reset_timer(command=self.init_timer)

    def start_count_down(self, seconds=None) -> None:
        if seconds is None:
            seconds = self.model.selected_time
            self.update_session_title()

        self.view.disable_activate_start_button(state="disabled")

        display_time = self.model.count_remaining_time(seconds=seconds)
        self.view.update_timer_text(display_time)

        if seconds > 0:
            # Save timer ID
            self.timer = self.view.window.after(ms=1000, func=self.start_count_down, seconds=seconds - 1)
        if seconds == 0:
            self.model.reps += 1
            self.update_session_title()

            if self.model.reps % 2 == 0:
                nbr_work_session = int(self.model.reps / 2)
                self.view.update_check_marks_text("✔︎" * nbr_work_session)

            self.play_mac_beep()
            self.view.disable_activate_start_button(state="normal")

    def init_timer(self) -> None:
        if self.timer:
            self.view.window.after_cancel(self.timer)

        self.view.update_check_marks_text("")
        self.view.update_title_text("Timer")
        self.view.disable_activate_start_button(state="normal")

        self.model.reps = 1
        self.model.selected_time = self.model.initial_time
        display_time = self.model.count_remaining_time(seconds=self.model.initial_time)
        self.view.update_timer_text(display_time)

    def update_session_title(self) -> None:
        session_type = self.model.get_session_type()
        self.model.manage_reps(session_type)
        self.view.update_title_text(session_type)

    def loop(self):

        self.view.window.mainloop()

    @staticmethod
    def play_mac_beep():
        """Play a simple sound notification based on platform"""
        platform = sys.platform

        if platform == "win32":
            try:
                import winsound
                winsound.Beep(frequency=1000, duration=300)  # 1000Hz for 300ms
            except ImportError:
                pass
        elif platform == "darwin":
            #os.system('osascript -e "beep"')
            os.system('afplay /System/Library/Sounds/Ping.aiff')
        else:
            pass