from selenium.webdriver.common.by import By
import os

"""environment"""
driver_chrome = os.path.abspath(os.curdir + '/drivers/chromedriver.exe')

"""urls"""
url_test_site = 'https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all'

"""params"""
timeout_page_sec = 40

"""elements"""
button_run_sql = '//*[@class="w3-green w3-btn"]'
result_text = '//*[@id="divResultSQL"]//*[@style=margin-bottom:10px;]'
name_Giovanni = "//*[contains(text(), 'Giovanni Rovelli')]"
name_Giovanni_next_element = "//td[contains(text(), 'Giovanni Rovelli')]/following-sibling::td"
number_of_records = "//*[contains(text(), 'Number of Records')]"
sql_table = "//table[@class='w3-table-all notranslate']"

"""test 1"""
adress_Giovanni = 'Via Ludovico il Moro 22'

"""test 2"""
sql_city_london = '"SELECT * FROM Customers WHERE City=\'London\';"'
recodrs_six = 'Number of Records: 6'

"""test 3"""
# used in test 5
records_ninety_one = 'Number of Records: 91'
sql_add_new_char = '"INSERT INTO Customers (CustomerName, ContactName, Address, City, PostalCode, Country) ' \
                   'VALUES (\'test\', \'test\' , \'test\', \'test\', 12345678, \'test\');"'
# used in test 4 and test 5
sql_all_char = '"SELECT * FROM Customers;"'
records_ninety_two = 'Number of Records: 92'
sql_last_char = '"SELECT * FROM Customers WHERE CustomerID = \'92\';"'

"""test 4"""
sql_new_table = '"UPDATE Customers SET CustomerName = \'test\', ContactName = \'test\', Address = \'test\', ' \
                'City = \'test\', PostalCode = \'test\', Country = \'test\';"'


"""test 5"""
sql_delete_mexico = '"DELETE FROM Customers WHERE City = \'México D.F.\';"'
records_eighty_six = 'Number of Records: 86'
