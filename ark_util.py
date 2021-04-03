import pyautogui
import os
import time


DIR = os.path.abspath(
    os.path.dirname(__file__)
)

def coords_point(coords):
    return (
        int(coords[0] / 2),
        int(coords[1] / 2),
    )

def get_region():
    region = pyautogui.locateOnScreen(
        os.path.join(
            DIR, "images", "00_calibrate", "title_screen_0.png"
            # DIR, "images", "00_calibrate", "test.png"
        ), grayscale=True, confidence=0.90
    )

    return region


def guarantee_click_img(target_img_path, verification_img_path, region, confidence=0.90):
    
    target_img_found = False
    coords = None
    # First Confirm Image Exists
    while not target_img_found:
        coords = pyautogui.locateCenterOnScreen(
            target_img_path, region=region, grayscale=True, confidence=(confidence if confidence else 0.95)
        )
        if coords:
            target_img_found = True


    verified = False
    # Then confirm click
    while not verified:

        pyautogui.click(
            coords_point(coords)
        )

        # Takes Time for click to process
        time.sleep(0.5)

        # 2 Conf methods. 
        #   Img is gone
        #   Another img pops up

        if verification_img_path:
            confirm = pyautogui.locateCenterOnScreen(
                verification_img_path, region=region, grayscale=True, confidence=(confidence if confidence else 0.95)
            )

            if confirm:
                verified = True

        else:
            confirm = pyautogui.locateCenterOnScreen(
                target_img_path, region=region, grayscale=True, confidence=(confidence if confidence else 0.95)
            )

            # print(confirm)

            if not confirm:
                verified = True


        return True
