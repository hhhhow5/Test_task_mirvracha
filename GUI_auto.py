import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import pyautogui

driver = webdriver.Chrome()
driver.maximize_window()
response = requests.get

driver.get("https://test.mirvracha.ru/")
print("Ответ от ресурса \"https://test.mirvracha.ru/\": ", response("https://test.mirvracha.ru/"))


wait = WebDriverWait(driver, 10)
find_e = driver.find_element

reg_email_field = find_e(By.CSS_SELECTOR, ".RegistrationForm_inputSh__xxwlI")
reg_email_field.send_keys("hhh7@gmail.com")


time.sleep(1)

reg_btn = find_e(By.CSS_SELECTOR, ".RegistrationForm_selectCustomSh__2wu8i")
reg_btn.click()
time.sleep(1)

status_select = find_e(By.CSS_SELECTOR, ".RegistrationForm_selectUl__3UgHC > li:nth-child(2)")
status_select.click()
print("Ответ от ресурса \"https://test.mirvracha.ru/auth/continueRegistration/student\": ",
      response("https://test.mirvracha.ru/auth/continueRegistration/student"))


lastName_field = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[name=\"lastName\"]")))
lastName_field.send_keys("Иванов")
pyautogui.press("Enter")

firstName_field = find_e(By.CSS_SELECTOR, "[name=\"firstName\"]")
firstName_field.send_keys("Иван")
pyautogui.press("Enter")

middleName_field = find_e(By.CSS_SELECTOR, "[name=\"middleName\"]")
middleName_field.send_keys("Иванович")
pyautogui.press("Enter")
time.sleep(1)

country_field = find_e(By.XPATH, "//div[@class =\"reg-info\"]/div[1]/div[1]//div[@class=\" css-1uccc91-singleValue\"]")
country_field_text = country_field.text
print(country_field_text)

if country_field_text == "Российская Федерация":
    print("Отлично, меньше действий")
else:
    country_field = find_e(By.XPATH,"//div[@class =\"reg-info\"]/div[1]/div[1]//div[@class=\" css-1uccc91-singleValue\"]")
    country_field.click()
    time.sleep(1)
    country_field_input = find_e(By.ID, "react-select-5-input")
    country_field_input.send_keys("Российская Федерация")
    # Не понимаю почему при заполнении поля по ID заполняется поле "Выберите ВУЗ"
    pyautogui.press("Enter")
    print("Так-то лучше")
time.sleep(2)

state_field = find_e(By.CSS_SELECTOR, ".reg-info :nth-child(2) .css-1uccc91-singleValue")
state_field_text = state_field.text
print(state_field_text)

if state_field_text == "Архангельская область":
    print("Отлично, меньше действий")
else:
    state_field.click()
    time.sleep(1)
    state_field_input = find_e(By.ID, "react-select-6-input")
    state_field_input.send_keys("Архангельская область")
    pyautogui.press("Enter")
    print("Так-то лучше")
    # Не понимаю почему при заполнении поля по ID заполняется поле "Год выпуска"
time.sleep(1)

city_field = find_e(By.CSS_SELECTOR, ".reg-info :nth-child(3) .css-1uccc91-singleValue")
city_field_text = city_field.text
print(city_field_text)

if city_field_text == "Северодвинс":
    print("Отлично, меньше действий")
else:
    city_field.click()
    time.sleep(1)
    city_field_input = find_e(By.XPATH, "//div[3][@class=\"open-select-box open\"]// input") #Работает через XPATH
# У поля ввода есть универсальный ID "react-select-7-input" и выдает ошибку "NoSuchElementException"
    city_field_input.send_keys("Северодвинск")
    pyautogui.press("Enter")
    print("Так-то лучше")

time.sleep(2)

university_field = find_e(By.CSS_SELECTOR, ".open-select-box.open:nth-child(1) .css-1wa3eu0-placeholder")
university_field_text = university_field.text


if university_field_text == "Выберите ВУЗ":
    university_field.click()
    time.sleep(1)
    university_field_input = find_e(By.XPATH, "//div[2][@class=\"box\"]/div[1]// input") #Через XPATH
# У поля ввода есть универсальный ID "react-select-8-input" и выдает ошибку "NoSuchElementException"
# Какая-то явная проблема при взаимодействии между блоками "box"
    university_field_input.send_keys("Крымский государственный медицинский университет")
    pyautogui.press("Enter")
    university = find_e(By.CSS_SELECTOR, "[name=\"university\"]")
    university_info = university.get_attribute("value")
    print("На самом деле я не заканчивал: " + str(university_info))

time.sleep(1)

finish_date_field = find_e(By.CSS_SELECTOR, ".open-select-box.open:nth-child(2) .css-1wa3eu0-placeholder")
finish_date_text = finish_date_field.text

if finish_date_text == "Год выпуска":
    finish_date_field.click()
    year_field_input = find_e(By.XPATH, "//div[2][@class=\"box\"]/div[2]// input")
# У поля ввода есть универсальный ID "react-select-8-input" и выдает ошибку "NoSuchElementException"
# Какая-то явная проблема при взаимодействии между блоками "box"

    year_field_input.send_keys(2023)
    pyautogui.press("Enter")
    finish_date = find_e(By.CSS_SELECTOR, "[name=\"finishDate\"]")
    finish_date_info = finish_date.get_attribute("value")
    print("Я закончу в: " + finish_date_info + ", но это не точно (=")

time.sleep(1)

test_btn = find_e(By.CSS_SELECTOR, "._role__btn__1ZVqS._role__btnGreen__1LPbR")
test_btn.click()

first_answer = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".Test_ulList__h_6j6 li:nth-child(2)")))
first_answer.click()
second_answer = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".Test_ulList__h_6j6 li:nth-child(3)")))
second_answer.click()
third_answer = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".Test_ulList__h_6j6 li:nth-child(1)")))
third_answer.click()
time.sleep(1)


file = ('C:\ListBoxer\pre.jpg')
upload = driver.find_element(By.CSS_SELECTOR, "div.MuiCollapse-root.MuiCollapse-hidden div._role__box__j3TmM input")
upload.send_keys(file)
time.sleep(7)

reg_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button._role__confirmBtn__14lU5")))
reg_btn.click()
time.sleep(5)

print("Ответ от ресурса \"https://test.mirvracha.ru/auth/afterRegistration/student\": ",
      response("https://test.mirvracha.ru/auth/afterRegistration/student"))

driver.quit()
