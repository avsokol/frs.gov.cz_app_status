import os
from time import sleep
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from inc.frsapp import constants
from inc.frsapp.ui import UI


def is_line_to_be_parsed(line):
    if line.strip() == "":
        return False

    if line[0] == "#":
        return False

    return True


def parse_app_line(line):
    seg1, seg2 = line.split("/")
    parts1 = seg1.split("-")
    app_number = parts1[1].strip().strip("0")
    part2 = seg2.split("-")
    app_type = part2[0].strip()
    app_year = part2[1].strip()
    return app_number, app_type, app_year


def process_file(browser, input_file_path, output_file_path=None):
    with open(input_file_path, "r") as f_in:
        for line in f_in:
            line = line.strip("\n")
            out_line = line
            if is_line_to_be_parsed(line):
                app_number, app_type, app_year = parse_app_line(line)
                sleep(1)
                result = get_status(browser, app_number, app_type, app_year)
                out_line = "{0} - {1}".format(line, result)
                print(out_line)

            if output_file_path is not None:
                with open(output_file_path, mode="a", encoding='utf-8') as f_out:
                    f_out.write(out_line)
                    f_out.write("\n")


def get_status(browser, app_number, app_type, app_year):
    browser.enter_app_number(app_number)
    browser.enter_app_type(app_type)
    browser.enter_app_year(app_year)
    browser.submit_form()
    browser.wait_for_submitted_result()
    WebDriverWait(browser.get_driver(), constants.DEFAULT_SHORT_TIMEOUT).until(
        expected_conditions.element_to_be_clickable(UI.get_app_submit_locator())
    )
    return browser.get_app_status()


def just_run(browser):
    browser.get_content()
    print("Title", browser.get_title())

    WebDriverWait(browser.get_driver(), constants.DEFAULT_SHORT_TIMEOUT).until(
        expected_conditions.element_to_be_clickable(UI.get_app_submit_locator())
    )

    cur_dir = os.path.dirname(__file__)
    infile = os.path.abspath(os.path.join(cur_dir, "..", "resources", "input_data.txt"))
    outfile = os.path.abspath(os.path.join(cur_dir, "..", "resources", "output_data.txt"))
    fw = open(outfile, "w+")
    fw.close()
    process_file(browser, infile, output_file_path=outfile)
