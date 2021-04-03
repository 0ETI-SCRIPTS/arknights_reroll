import pyautogui
import os
import time

from pathlib import Path

from ark_util import (
    coords_point,
    get_region,
    guarantee_click_img
)

from ark_email import get_recent_code

from ark_config import (
    FROM_EMAIL,
    USERNAME
)

DIR = os.path.abspath(
    os.path.dirname(__file__)
)

iteration = 103

EMAIL = f"{FROM_EMAIL}+ark{iteration:03}@gmail.com"
NAME = f"{USERNAME}{iteration:03}"

HH_1_SC_PATH = os.path.join(
    DIR, "screenshots", f"{iteration:03}", f"{iteration:03}-x1.png"
)

HH_10_SC_PATH = os.path.join(
    DIR, "screenshots", f"{iteration:03}", f"{iteration:03}-x10.png"
)

region = (0, 102, 2558, 1442)

pyautogui.click(
    coords_point(pyautogui.center(region))
)

########################################################################################

# Phase 0 - CALIBRATE

########################################################################################


def phase_0():

    print(pyautogui.size())

    region = get_region()

    pyautogui.click(
        coords_point(pyautogui.center(region))
    )

    print(coords_point(pyautogui.center(region)))

########################################################################################

# Phase 1 - NAVIGATE TITLE

########################################################################################


def phase_1():

    guarantee_click_img(
        os.path.join(
            DIR, "images", "01_navigate_title", "01_account_management.png"
        ), None, region
    )

    guarantee_click_img(
        os.path.join(
            DIR, "images", "01_navigate_title", "02_yostar.png"
        ), None, region
    )

    guarantee_click_img(
        os.path.join(
            DIR, "images", "01_navigate_title", "03_red_check.png"
        ), None, region
    )

########################################################################################

# Phase 2 - CREATE ACCOUNT

########################################################################################


def phase_2():

    guarantee_click_img(
        os.path.join(
            DIR, "images", "02_create_account", "04_mail_address_field.png"
        ),
        os.path.join(
            DIR, "images", "02_create_account", "07_form_verification.png"
        ), region
    )

    pyautogui.write(EMAIL)

    guarantee_click_img(
        os.path.join(
            DIR, "images", "02_create_account", "08_form_ok.png"
        ), None, region
    )

    guarantee_click_img(
        os.path.join(
            DIR, "images", "02_create_account", "05_send_verification.png"
        ), None, region
    )

    time.sleep(10)
    code = get_recent_code()

    guarantee_click_img(
        os.path.join(
            DIR, "images", "02_create_account", "06_verification_code_field.png"
        ),
        os.path.join(
            DIR, "images", "02_create_account", "07_form_verification.png"
        ), region
    )

    pyautogui.write(code)

    guarantee_click_img(
        os.path.join(
            DIR, "images", "02_create_account", "08_form_ok.png"
        ), None, region
    )

    guarantee_click_img(
        os.path.join(
            DIR, "images", "02_create_account", "09_login.png"
        ), None, region
    )


########################################################################################

# Phase 3 - AGREE TOS

########################################################################################

def phase_3():

    guarantee_click_img(
        os.path.join(
            DIR, "images", "03_agree_tos", "11_checkbox.png"
        ), None, region, 0.95
    )

    guarantee_click_img(
        os.path.join(
            DIR, "images", "03_agree_tos", "12_confirm.png"
        ), None, region
    )


########################################################################################

# Phase 4 - SET NAME

########################################################################################

def phase_4():

    guarantee_click_img(
        os.path.join(
            DIR, "images", "04_set_name", "13_i_am_field.png"
        ), os.path.join(
            DIR, "images", "04_set_name", "14_form_name.png"
        ), region
    )

    pyautogui.write(NAME)

    guarantee_click_img(
        os.path.join(
            DIR, "images", "04_set_name", "15_form_ok.png"
        ), None, region
    )

    guarantee_click_img(
        os.path.join(
            DIR, "images", "04_set_name", "16_confirm.png"
        ), None, region
    )


########################################################################################

# Phase 5 - TUTORIAL_1

########################################################################################

def phase_5():

    guarantee_click_img(
        os.path.join(
            DIR, "images", "05_tutorial_1", "17_skip_dialogue.png"
        ), None, region
    )

    guarantee_click_img(
        os.path.join(
            DIR, "images", "05_tutorial_1", "18_check_circle.png"
        ), None, region
    )

    guarantee_click_img(
        os.path.join(
            DIR, "images", "05_tutorial_1", "19_guide_icon.png"
        ), None, region
    )

    # Check For Texas
    while True:

        texas_icon_coords = pyautogui.locateCenterOnScreen(
            os.path.join(
                DIR, "images", "05_tutorial_1", "20_texas_2.png"
            ), region=region, grayscale=True, confidence=0.50
        )

        if texas_icon_coords:
            texas_move_coords = pyautogui.locateCenterOnScreen(
                os.path.join(
                    DIR, "images", "05_tutorial_1", "21_texas_drag_location.png"
                ), region=region, grayscale=True, confidence=0.60
            )
            adjusted_move_coords = coords_point(texas_move_coords)

            pyautogui.moveTo(coords_point(texas_icon_coords))
            pyautogui.dragTo(
                adjusted_move_coords[0], adjusted_move_coords[1], 1, button="left")

            time.sleep(1)
            pyautogui.drag(500, 0, 1, button='left')
            time.sleep(1)

            # Confirm Action went through
            texas_icon_coords = pyautogui.locateCenterOnScreen(
                os.path.join(
                    DIR, "images", "05_tutorial_1", "20_texas_2.png"
                ), region=region, grayscale=True, confidence=0.50
            )

            if not texas_icon_coords:
                break

        else:
            for i in range(5):
                pyautogui.click(
                    coords_point(pyautogui.center(region))
                )
                time.sleep(1)

    # Idle while battle sequence
    time.sleep(10)
    for i in range(10):
        pyautogui.click(
            coords_point(pyautogui.center(region))
        )
        time.sleep(1)

    # Check For Exusiai
    while True:

        exusiai_icon_coords = pyautogui.locateCenterOnScreen(
            os.path.join(
                DIR, "images", "05_tutorial_1", "22_exusiai.png"
            ), region=region, grayscale=True, confidence=0.50
        )

        if exusiai_icon_coords:
            exusiai_move_coords = pyautogui.locateCenterOnScreen(
                os.path.join(
                    DIR, "images", "05_tutorial_1", "23_exusiai_drag_location.png"
                ), region=region, grayscale=True, confidence=0.60
            )
            adjusted_move_coords = coords_point(exusiai_move_coords)

            pyautogui.moveTo(coords_point(exusiai_icon_coords))
            pyautogui.dragTo(
                adjusted_move_coords[0], adjusted_move_coords[1], 1, button="left")

            time.sleep(1)
            pyautogui.drag(500, 0, 1, button='left')
            time.sleep(1)

            # Confirm Action went through
            exusiai_icon_coords = pyautogui.locateCenterOnScreen(
                os.path.join(
                    DIR, "images", "05_tutorial_1", "22_exusiai.png"
                ), region=region, grayscale=True, confidence=0.50
            )

            if not exusiai_icon_coords:
                print("exusiai fin")
                break

        else:
            for i in range(5):
                pyautogui.click(
                    coords_point(pyautogui.center(region))
                )
                time.sleep(1)


########################################################################################

# Phase 6 - TUTORIAL_2

########################################################################################

def phase_6():

    while True:

        texas_icon_coords = pyautogui.locateCenterOnScreen(
            os.path.join(
                DIR, "images", "06_tutorial_2", "24.5.png"
                # DIR, "images", "06_tutorial_2", "24_texas_skill_start.png"
            ), region=region, grayscale=True, confidence=0.60
        )

        print(texas_icon_coords)

        if texas_icon_coords:
            break

        else:
            for i in range(5):
                pyautogui.write(" ")
                time.sleep(0.5)

    for i in range(5):
        pyautogui.write(" ")
        time.sleep(0.5)

    guarantee_click_img(
        os.path.join(
            DIR, "images", "06_tutorial_2", "24.5.png"
            # DIR, "images", "06_tutorial_2", "24_texas_skill_start.png"
        ), None, region, 0.60
    )

    while True:

        skill_coords = pyautogui.locateCenterOnScreen(
            os.path.join(
                DIR, "images", "06_tutorial_2", "25_skill_ready.png"
            ), region=region, grayscale=True, confidence=0.75
        )

        if skill_coords:
            break

        else:
            for i in range(5):
                pyautogui.write(" ")
                time.sleep(0.5)

    guarantee_click_img(
        os.path.join(
            DIR, "images", "06_tutorial_2", "25_skill_ready.png"
        ), None, region
    )


########################################################################################

# Phase 7 - HEADHUNT

########################################################################################

def phase_7():

    while True:
        hh_coords = pyautogui.locateCenterOnScreen(
            os.path.join(
                DIR, "images", "07_headhunt", "25.5.png"
            ), region=region, grayscale=True, confidence=0.75
        )

        if hh_coords:
            break

        else:
            for i in range(5):
                pyautogui.write(" ")
                time.sleep(0.5)

    guarantee_click_img(
        os.path.join(
            DIR, "images", "07_headhunt", "25.5.png"
        ), None, region
    )

    guarantee_click_img(
        os.path.join(
            DIR, "images", "05_tutorial_1", "18_check_circle.png"
        ), None, region
    )

    while True:

        hh_coords = pyautogui.locateCenterOnScreen(
            os.path.join(
                DIR, "images", "07_headhunt", "26_headhunt_x1.png"
            ), region=region, grayscale=True, confidence=0.75
        )

        if hh_coords:
            break

        else:
            for i in range(5):
                pyautogui.write(" ")
                time.sleep(0.5)

    guarantee_click_img(
        os.path.join(
            DIR, "images", "07_headhunt", "26_headhunt_x1.png"
        ), None, region, 0.80
    )

    guarantee_click_img(
        os.path.join(
            DIR, "images", "07_headhunt", "27_skip.png"
        ), None, region
    )

    Path(os.path.dirname(HH_1_SC_PATH)).mkdir(parents=True, exist_ok=True)
    pyautogui.screenshot(HH_1_SC_PATH)

    while True:

        add_squad_coords = pyautogui.locateCenterOnScreen(
            os.path.join(
                DIR, "images", "07_headhunt", "28_add_squad.png"
            ), region=region, grayscale=True, confidence=0.75
        )

        if add_squad_coords:
            break

        else:
            for i in range(5):
                pyautogui.write(" ")
                time.sleep(0.5)

    guarantee_click_img(
        os.path.join(
            DIR, "images", "07_headhunt", "28_add_squad.png"
        ), None, region
    )

    guarantee_click_img(
        os.path.join(
            DIR, "images", "07_headhunt", "28.5.png"
        ), None, region
    )

    guarantee_click_img(
        os.path.join(
            DIR, "images", "07_headhunt", "29_add_squad_confirm.png"
        ), None, region
    )

    guarantee_click_img(
        os.path.join(
            DIR, "images", "07_headhunt", "30_return_home_1.png"
        ), os.path.join(
            DIR, "images", "07_headhunt", "30_return_home_2.png"
        ), region, 0.80
    )

    guarantee_click_img(
        os.path.join(
            DIR, "images", "07_headhunt", "30_return_home_2.png"
        ), None, region, 0.80
    )

    while True:

        et_coords = pyautogui.locateCenterOnScreen(
            os.path.join(
                DIR, "images", "07_headhunt", "31_evil_time.png"
            ), region=region, grayscale=True, confidence=0.75
        )

        if et_coords:
            break

        else:
            for i in range(5):
                pyautogui.click(
                    coords_point(pyautogui.center(region))
                )
                time.sleep(1)

    guarantee_click_img(
        os.path.join(
            DIR, "images", "07_headhunt", "31_evil_time.png"
        ), None, region
    )

    guarantee_click_img(
        os.path.join(
            DIR, "images", "07_headhunt", "32_0-1.png"
        ), None, region
    )

    guarantee_click_img(
        os.path.join(
            DIR, "images", "07_headhunt", "33_start.png"
        ), None, region
    )

    guarantee_click_img(
        os.path.join(
            DIR, "images", "07_headhunt", "34_mission_start.png"
        ), None, region
    )


########################################################################################

# Phase 8 - 0-1

########################################################################################

def phase_8():

    guarantee_click_img(
        os.path.join(
            DIR, "images", "08_0-1", "35_skip.png"
        ), None, region
    )

    guarantee_click_img(
        os.path.join(
            DIR, "images", "08_0-1", "36_skip_confirm.png"
        ), None, region
    )

    time.sleep(10)

    while True:

        et_coords = pyautogui.locateCenterOnScreen(
            os.path.join(
                DIR, "images", "08_0-1", "37_settings.png"
            ), region=region, grayscale=True, confidence=0.90
        )

        if et_coords:
            break

        else:
            for i in range(5):
                pyautogui.click(
                    coords_point(pyautogui.center(region))
                )
                time.sleep(1)

    guarantee_click_img(
        os.path.join(
            DIR, "images", "08_0-1", "37_settings.png"
        ), None, region
    )

    guarantee_click_img(
        os.path.join(
            DIR, "images", "08_0-1", "38_retreat_confirm.png"
        ), None, region
    )

########################################################################################

# Phase 9 - Headhunt_10

########################################################################################


def phase_9():

    while True:

        et_coords = pyautogui.locateCenterOnScreen(
            os.path.join(
                DIR, "images", "09_headhunt_10", "39_home_1.png"
            ), region=region, grayscale=True, confidence=0.90
        )

        if et_coords:
            break

        else:
            for i in range(5):
                pyautogui.click(
                    coords_point(pyautogui.center(region))
                )
                time.sleep(1)

    guarantee_click_img(
        os.path.join(
            DIR, "images", "09_headhunt_10", "39_home_1.png"
        ), None, region
    )

    guarantee_click_img(
        os.path.join(
            DIR, "images", "09_headhunt_10", "40_home_2.png"
        ), None, region
    )

    for i in range(5):
        pyautogui.click(
            coords_point(
                (pyautogui.center(region)[0] +
                 500, pyautogui.center(region)[1])
            )
        )
        time.sleep(1)

    guarantee_click_img(
        os.path.join(
            DIR, "images", "09_headhunt_10", "41_close_monthly.png"
        ), None, region
    )

    guarantee_click_img(
        os.path.join(
            DIR, "images", "09_headhunt_10", "42_close_sign_in.png"
        ), None, region
    )

    guarantee_click_img(
        os.path.join(
            DIR, "images", "09_headhunt_10", "43_inbox.png"
        ), None, region
    )

    guarantee_click_img(
        os.path.join(
            DIR, "images", "09_headhunt_10", "44_collect_all.png"
        ), None, region
    )

    for i in range(5):
        pyautogui.click(
            coords_point(
                (pyautogui.center(region)[0] +
                 500, pyautogui.center(region)[1])
            )
        )
        time.sleep(1)

    guarantee_click_img(
        os.path.join(
            DIR, "images", "09_headhunt_10", "45_back.png"
        ), None, region
    )

    guarantee_click_img(
        os.path.join(
            DIR, "images", "09_headhunt_10", "46_headhunt.png"
        ), None, region
    )

    guarantee_click_img(
        os.path.join(
            DIR, "images", "09_headhunt_10", "47_headhunt_10.png"
        ), None, region
    )

    guarantee_click_img(
        os.path.join(
            DIR, "images", "09_headhunt_10", "48_headhunt_10_confirm.png"
        ), None, region
    )

    guarantee_click_img(
        os.path.join(
            DIR, "images", "09_headhunt_10", "49_headhunt_10_skip_2.png"
        ), None, region
    )

    time.sleep(2)

    Path(os.path.dirname(HH_10_SC_PATH)).mkdir(parents=True, exist_ok=True)
    pyautogui.screenshot(HH_10_SC_PATH)

    for i in range(10):
        pyautogui.write(" ")
        time.sleep(0.5)

    guarantee_click_img(
        os.path.join(
            DIR, "images", "09_headhunt_10", "39_home_1.png"
        ), None, region, 0.80
    )

    guarantee_click_img(
        os.path.join(
            DIR, "images", "09_headhunt_10", "40_home_2.png"
        ), None, region, 0.80
    )

    guarantee_click_img(
        os.path.join(
            DIR, "images", "09_headhunt_10", "50_settings.png"
        ), None, region, 0.80
    )

    guarantee_click_img(
        os.path.join(
            DIR, "images", "09_headhunt_10", "51_settings_account.png"
        ), None, region
    )

    guarantee_click_img(
        os.path.join(
            DIR, "images", "09_headhunt_10", "52_logout.png"
        ), None, region
    )

    guarantee_click_img(
        os.path.join(
            DIR, "images", "09_headhunt_10", "53_logout_confirm.png"
        ), None, region
    )


def main():

    global iteration
    global EMAIL
    global NAME
    global HH_1_SC_PATH
    global HH_10_SC_PATH

    while True:

        EMAIL = f"{FROM_EMAIL}+ark{iteration:03}@gmail.com"
        NAME = f"{USERNAME}{iteration:03}"

        HH_1_SC_PATH = os.path.join(
            DIR, "screenshots", f"{iteration:03}", f"{iteration:03}-x1.png"
        )
        HH_10_SC_PATH = os.path.join(
            DIR, "screenshots", f"{iteration:03}", f"{iteration:03}-x10.png"
        )

        phase_1()
        phase_2()
        phase_3()
        phase_4()
        phase_5()
        phase_6()
        phase_7()
        phase_8()
        phase_9()

        iteration = iteration + 1


main()
