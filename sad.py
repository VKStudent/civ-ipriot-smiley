import time
from smiley import Smiley


class Sad(Smiley):
    BLUE = (0, 0, 255)

    def __init__(self):
        super().__init__(complexion=self.BLUE)

        self.draw_mouth()
        self.draw_eyes()

    def draw_mouth(self):
        """
        Method that draws the mouth on the standard faceless smiley.
        """
        mouth = [49, 54, 42, 43, 44, 45]
        for pixel in mouth:
            self.pixels[pixel] = self.BLANK

    def draw_eyes(self, wide_open=True):
        """
        Method that draws the eyes (open or closed) on the standard smiley.
        :param wide_open: True if eyes opened, False otherwise
        """
        eyes = [10, 13, 18, 21]
        for pixel in eyes:
            self.pixels[pixel] = self.BLANK if wide_open else self.YELLOW

    def blink(self, delay=0.25):

        """
        Makes the sad smiley blink once for a certain time.
        It closes its eyes briefly and then opens them again after the delay.

        :param delay: The time in seconds for how long the blink lasts.
        """
        self.draw_eyes(wide_open=False)  # Close the eyes
        self.show()
        time.sleep(delay)
        self.draw_eyes(wide_open=True)  # Open the eyes again
        self.show()
