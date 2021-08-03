from powerline_shell.utils import BasicSegment
import os


class Segment(BasicSegment):
    def add_to_powerline(self):
            self.powerline.append(" Terminal_Heat_Sink ",
                                  self.powerline.theme.CWD_FG,
                                  self.powerline.theme.PATH_BG)
