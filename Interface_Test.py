import pyautogui
import unittest
import time

class TestLogin(unittest.TestCase):
    def test_login(self):
        time.sleep(5)
        email_box_coordinates = (1693, 575)

        email = 'dan.proca00@e-uvt.ro'
        password = 'parola'

        pyautogui.click(email_box_coordinates)
        pyautogui.write(email)
        time.sleep(1)

        pyautogui.press('tab')
        pyautogui.write(password)
        time.sleep(1)

        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('enter')
        time.sleep(3)

        button_coordinates = (1674, 475)
        pyautogui.click(button_coordinates)

if __name__ == "__main__":
    unittest.main()