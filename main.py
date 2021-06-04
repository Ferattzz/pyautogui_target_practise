import pyautogui as pt


class Clicker:
    def __init__(self, target_png, speed=.1):
        self.target_png = target_png
        self.speed = speed
        pt.FAILSAFE = True

    def nav_to_image(self):
        try:
            position = pt.locateOnScreen(self.target_png, confidence=.6, region=(0, 84, 1277, 793))
            pt.moveTo(position[0] + 15, position[1] + 15, duration=self.speed)
            pt.doubleClick()

        except:
            print('No image found...')
            return 0


if __name__ == '__main__':
    # Initialises the clicker
    clicker = Clicker('images/circle.png', speed=.001)

    end = 0
    while True:

        # Checks whether there are still circles
        if clicker.nav_to_image() == 0:
            end += 1

        # End the loop
        if end > 5:
            break
