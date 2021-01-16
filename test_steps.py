from helper import *
from time import sleep


def test_first():
    """ContactName == Giovanni Rovelli, Adress == Via Ludovico il Moro 22"""
    try:
        driver = chrome_driver(url_test_site)
        waiting(driver, button_run_sql)
        driver.find_element_by_xpath(button_run_sql).click()
        sleep(1)
        if driver.find_element_by_xpath(name_Giovanni):
            assert True
        else:
            assert False
        adress_Giovanni_in_table = driver.find_element_by_xpath(name_Giovanni_next_element).text
        assert adress_Giovanni_in_table == adress_Giovanni
        driver.quit()
    except BaseException as e:
        print('General exception!' + str(e))
        driver.quit()
        assert False


def test_second():
    """Total six entries"""
    try:
        driver = chrome_driver(url_test_site)
        waiting(driver, button_run_sql)
        js_request(driver, sql_city_london)
        driver.find_element_by_xpath(button_run_sql).click()
        sleep(1)
        assert driver.find_element_by_xpath(number_of_records).text == recodrs_six
        driver.quit()
    except BaseException as e:
        print('General exception!' + str(e))
        driver.quit()
        assert False


def test_third():
    """Added new entry"""
    try:
        driver = chrome_driver(url_test_site)
        waiting(driver, button_run_sql)
        driver.find_element_by_xpath(button_run_sql).click()
        sleep(1)
        assert driver.find_element_by_xpath(number_of_records).text == records_ninety_one
        js_request(driver, sql_add_new_char)
        driver.find_element_by_xpath(button_run_sql).click()
        sleep(1)
        js_request(driver, sql_all_char)
        driver.find_element_by_xpath(button_run_sql).click()
        sleep(1)
        assert driver.find_element_by_xpath(number_of_records).text == records_ninety_two
        js_request(driver, sql_last_char)
        driver.find_element_by_xpath(button_run_sql).click()
        sleep(1)
        table = driver.find_element_by_xpath(sql_table)
        for row in table.find_elements_by_xpath(".//tr")[1:]:
            real_row = [td.text for td in row.find_elements_by_xpath(".//td")]
            true_row = ['92', 'test', 'test', 'test', 'test', '12345678', 'test']
            if str(real_row) == str(true_row).replace('"', ''):
                assert True
            else:
                assert False
        driver.quit()
    except BaseException as e:
        print('General exception!' + str(e))
        driver.quit()
        assert False


def test_fourth():
    """Change all data in a table"""
    try:
        driver = chrome_driver(url_test_site)
        waiting(driver, button_run_sql)
        js_request(driver, sql_new_table)
        driver.find_element_by_xpath(button_run_sql).click()
        sleep(1)
        js_request(driver, sql_all_char)
        driver.find_element_by_xpath(button_run_sql).click()
        sleep(1)
        table = driver.find_element_by_xpath(sql_table)
        n = 0
        for row in table.find_elements_by_xpath(".//tr")[1:]:
            n = n + 1
            real_row = [td.text for td in row.find_elements_by_xpath(".//td")]
            st = str('\'' + str(n) + '\'')
            true_row = [st, 'test', 'test', 'test', 'test', 'test', 'test']
            if str(real_row) == str(true_row).replace('"', ''):
                assert True
            else:
                assert False
        driver.quit()
    except BaseException as e:
        print('General exception!' + str(e))
        driver.quit()
        assert False


def test_fifth():
    """Delete all city == México D.F."""
    try:
        driver = chrome_driver(url_test_site)
        waiting(driver, button_run_sql)
        driver.find_element_by_xpath(button_run_sql).click()
        sleep(1)
        assert driver.find_element_by_xpath(number_of_records).text == records_ninety_one
        js_request(driver, sql_delete_mexico)
        driver.find_element_by_xpath(button_run_sql).click()
        sleep(1)
        js_request(driver, sql_all_char)
        driver.find_element_by_xpath(button_run_sql).click()
        sleep(1)
        assert driver.find_element_by_xpath(number_of_records).text == records_eighty_six
        driver.quit()
    except BaseException as e:
        print('General exception!' + str(e))
        driver.quit()
        assert False
