import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import os

driver = webdriver.Chrome()

login = "79900011654" #k.nbrjdf
password = "F5Zs6sNYpFBLu0T"
pasport = '6000000000'

# авторизуемся в VK..
driver.get("https://vk.com/app7299406") #test
textarea = driver.find_element_by_css_selector("#quick_email")
time.sleep(1)
textarea.send_keys(login)
time.sleep(1)
textarea = driver.find_element_by_css_selector("#quick_pass")
textarea.send_keys(password)
time.sleep(1)
submit_button = driver.find_element_by_css_selector("#quick_login_button")
submit_button.click()

"""как обойти капчу? """

# переходим на фрейм рассрочки

time.sleep(5)
wait = WebDriverWait(driver, 140)
element = wait.until(EC.visibility_of_element_located((By.ID,'app_7299406_container')))

driver.switch_to.default_content() # уже не помню для чего, но что-то оно делает на тему
iframe = driver.find_element_by_css_selector("#app_7299406_container>iframe") # находишь app_7299406_container
time.sleep(1)
driver.switch_to.frame(iframe) # переключаешься на него
time.sleep(1)
  # уже в нем действуешь
time.sleep(3)
submit_button = driver.find_element_by_css_selector("[class='Tappable Tappable--ios Button Button--ios gallery-button Button--sz-xl Button--lvl-primary Button--aln-center Tappable--inactive']")

submit_button.click()  # жмём кнопку "узнать лимит"

#ввод перс.данных ДР,  паспорт, почта, доход
#ждём загрузки

wait = WebDriverWait(driver, 140)
element = wait.until(EC.visibility_of_element_located((By.ID,'bd_date')))
#др  bd_date
textarea = driver.find_element_by_css_selector("#bd_date")
time.sleep(1)
textarea.send_keys("02")
time.sleep(1)
#др месяц
time.sleep(1)
textarea = driver.find_element_by_css_selector("#bd_month")
time.sleep(1)
textarea.send_keys("03")

#др год
time.sleep(1)
textarea = driver.find_element_by_css_selector("#bd_year").clear()
time.sleep(1)
textarea = driver.find_element_by_css_selector("#bd_year")
#time.sleep(2)
textarea.send_keys("1977")
# паспорт ident 6000000000

#
textarea = driver.find_element_by_css_selector("#email")
time.sleep(2)
textarea.send_keys("test@lost.ru")
#
textarea = driver.find_element_by_css_selector("#monthly_income")
time.sleep(2)
textarea.send_keys("210000")

#галочка согласия
option1 = driver.find_element_by_css_selector("[class='Tappable Tappable--ios Checkbox Checkbox--ios Tappable--inactive']")
option1.click()

#кнопка Подтвердить

submit_button = driver.find_element_by_css_selector("[class='Tappable Tappable--ios Button Button--ios Button--sz-xl Button--lvl-primary Button--aln-center Tappable--inactive']")
time.sleep(2)
submit_button.click()

# sms: password
#ждём загрузки
wait = WebDriverWait(driver, 35)
element = wait.until(EC.visibility_of_element_located((By.ID,'password')))

textarea = driver.find_element_by_css_selector("#password")
time.sleep(2)
textarea.send_keys("1111")

# переход на КЛ. чекаут в модалке  app_7756368_container_layer
time.sleep(5)

driver.switch_to.default_content() # уже не помню для чего, но что-то оно делает на тему
wait = WebDriverWait(driver, 60)
element = wait.until(EC.visibility_of_element_located((By.ID,'app_7756368_container_layer')))


time.sleep(5)

iframe = driver.find_element_by_css_selector("#app_7756368_container_layer>iframe")
time.sleep(1)
driver.switch_to.frame(iframe)
time.sleep(2)
#print("ok")

#issuing_unit
issuing_unit = 'РОВД района города '
textarea = driver.find_element_by_css_selector("[name='issuing_unit']")
textarea.clear()
time.sleep(1)
i = 0
while i < len(issuing_unit):
    time.sleep(0.5)
    textarea.send_keys(issuing_unit[i])
    i +=1

# [name='issue_date']
time.sleep(0.5)

issue_date = '02022020'
textarea = driver.find_element_by_css_selector("[name='issue_date']")
textarea.clear()
time.sleep(1)
i = 0
while i < len(issue_date):
    time.sleep(0.5)
    textarea.send_keys(issue_date[i])
    i +=1
# issuing_code
time.sleep(0.5)

issuing_code = '123321'
textarea = driver.find_element_by_css_selector("[name='issuing_code']")
textarea.clear()
time.sleep(1)
i = 0
while i < len(issuing_code):
    time.sleep(0.5)
    textarea.send_keys(issuing_code[i])
    i +=1
# birth_place
birth_place = 'г Самара, ул Искровская, д 12, кв 8 '
textarea = driver.find_element_by_css_selector("[name='birth_place']")
textarea.clear()
time.sleep(1)
i = 0
while i < len(birth_place):
    time.sleep(0.5)
    textarea.send_keys(birth_place[i])
    i +=1

wait = WebDriverWait(driver, 120)
element = wait.until(EC.element_to_be_clickable((By.ID, 'react-autowhatever-1--item-0'))).click()

# registration_address
registration_address = 'г Самара, ул Искровская, д 12, кв 8 '
textarea = driver.find_element_by_css_selector("[name='registration_address']")
textarea.clear()
time.sleep(1)
i = 0
while i < len(registration_address):
    time.sleep(0.5)
    textarea.send_keys(registration_address[i])
    i +=1

wait = WebDriverWait(driver, 120)
element = wait.until(EC.element_to_be_clickable((By.ID, 'react-autowhatever-1--item-0'))).click()

# Tappable Tappable--android Button Button--android PersonalInfoForm_button__1ZYUh Button--sz-s Button--lvl-primary Button--aln-center Button--sizeY-regular Tappable--sizeX-compact Tappable--inactive Tappable--mouse
time.sleep(1)
submit_button = driver.find_element_by_css_selector("[class='Tappable Tappable--android Button Button--android PersonalInfoForm_button__1ZYUh Button--sz-s Button--lvl-primary Button--aln-center Button--sizeY-regular Tappable--sizeX-compact Tappable--inactive Tappable--mouse']")
time.sleep(1)
submit_button.click()


# screen 1.2
#ждём загрузки
wait = WebDriverWait(driver, 35)
element = wait.until(EC.visibility_of_element_located((By.ID,'registration_address')))

#adress
address = 'г Самара, ул 22 Партсъезда, д 13, кв 44 '
textarea = driver.find_element_by_css_selector("#registration_address")
textarea.clear()
time.sleep(1)
i = 0
while i < len(address):
    time.sleep(0.5)
    textarea.send_keys(address[i])
    i +=1

wait = WebDriverWait(driver, 120)
element = wait.until(EC.element_to_be_clickable((By.ID, 'react-autowhatever-1--item-0'))).click()


#выбор типа занятости
time.sleep(1)
driver.find_element_by_css_selector("[class='ik_select']").click()
drop_down = driver.find_element_by_css_selector('[data-value="COMMERCIAL_EMPLOYEE"]')
ActionChains(driver).move_to_element(drop_down).perform()
drop_down.click()

#кнопка продолжить
time.sleep(1)
submit_button = driver.find_element_by_css_selector("[class='Tappable Tappable--ios Button Button--ios Button--sz-xl Button--lvl-primary Button--aln-center Tappable--inactive']")
time.sleep(1)
submit_button.click()

#анкета 2.1
#ждём загрузки
wait = WebDriverWait(driver, 140)
element = wait.until(EC.visibility_of_element_located((By.ID,'ws_month')))

time.sleep(1)
textarea = driver.find_element_by_css_selector("#ws_month")
time.sleep(0.5)
textarea.send_keys("10")

time.sleep(1)
textarea = driver.find_element_by_css_selector("#ws_year")
time.sleep(0.5)
textarea.send_keys("2010")

#residential_address
residential_address = 'г Саратов, мкр Жасминный, ул Строителей, д 13, кв 777 '
textarea = driver.find_element_by_css_selector("#residential_address")
textarea.clear()
time.sleep(1)
i = 0
while i < len(residential_address):
    time.sleep(0.2)
    textarea.send_keys(residential_address[i])
    i +=1

wait = WebDriverWait(driver, 140)
element = wait.until(EC.element_to_be_clickable((By.ID, 'react-autowhatever-1--item-0'))).click()


#Семейное положение
time.sleep(1)
select = Select(driver.find_element_by_css_selector("#marital_status"))
select.select_by_value("SINGLE")

#Образование
time.sleep(1)
select = Select(driver.find_element_by_css_selector("#education"))
select.select_by_value("HIGHER")

#Контактное лицо
time.sleep(1)
select = Select(driver.find_element_by_css_selector("#contact_person"))
select.select_by_value("OMAY_Friend")

time.sleep(1)
contact_person_phone = '9276665544'
textarea = driver.find_element_by_css_selector("#contact_person_phone")
textarea.clear()
time.sleep(0.1)
i = 0
while i < len(contact_person_phone):
    time.sleep(0.1)
    textarea.send_keys(contact_person_phone[i])
    i +=1

#кнопка продолжить
time.sleep(1)
submit_button = driver.find_element_by_css_selector("[class='Tappable Tappable--ios Button Button--ios Button--sz-xl Button--lvl-primary Button--aln-center Tappable--inactive']")
time.sleep(1)
submit_button.click()

#анкета 2.2
#ждём загрузки
wait = WebDriverWait(driver, 140)
element = wait.until(EC.visibility_of_element_located((By.ID,'position')))
time.sleep(0.5)

V_position = 'Врач-стоматолог'
textarea = driver.find_element_by_css_selector("#position")
textarea.clear()
time.sleep(0.1)
i = 0
while i < len(V_position):
    time.sleep(0.1)
    textarea.send_keys(V_position[i])
    i +=1
time.sleep(0.5)

#wait = WebDriverWait(driver, 35)
#element = wait.until(EC.element_to_be_clickable((By.ID, 'react-autowhatever-1--item-0'))).click()

organization_name = 'Работа'
textarea = driver.find_element_by_css_selector("#organization_name")
textarea.clear()
time.sleep(0.1)
i = 0
while i < len(organization_name):
    time.sleep(0.1)
    textarea.send_keys(organization_name[i])
    i +=1
time.sleep(0.5)

organization_phone = '9278889900'
textarea = driver.find_element_by_css_selector("#organization_phone")
textarea.clear()
time.sleep(0.1)
i = 0
while i < len(organization_phone):
    time.sleep(0.1)
    textarea.send_keys(organization_phone[i])
    i +=1
time.sleep(0.5)

employment_address = 'г Тула, пр-кт Ленина, д 33 '
textarea = driver.find_element_by_css_selector("#employment_address")
textarea.clear()
time.sleep(0.1)
i = 0
while i < len(employment_address):
    time.sleep(0.2)
    textarea.send_keys(employment_address[i])
    i +=1
time.sleep(0.5)
wait = WebDriverWait(driver, 135)
element = wait.until(EC.element_to_be_clickable((By.ID, 'react-autowhatever-1--item-0'))).click()
time.sleep(0.5)

#кнопка продолжить
time.sleep(1)
submit_button = driver.find_element_by_css_selector("[class='Tappable Tappable--ios Button Button--ios Button--sz-xl Button--lvl-primary Button--aln-center Tappable--inactive']")
time.sleep(1)
submit_button.click()

#ИНН
#анкета 2.2
#ждём загрузки

#wait = WebDriverWait(driver, 140)
#element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'Input__el')))

"""тут не работает нормальное ожидание. нет элементов с ID, а по CLASS_NAME не находит """

time.sleep(25)

v_inn = '175255503173'
textarea = driver.find_element_by_css_selector("[class='Input__el']")
textarea.clear()
time.sleep(0.1)
i = 0
while i < len(v_inn):
    time.sleep(0.1)
    textarea.send_keys(v_inn[i])
    i +=1
time.sleep(0.5)

#кнопка продолжить
time.sleep(2)
submit_button = driver.find_element_by_css_selector("[class='Tappable Tappable--ios Button Button--ios inn_form-button Button--sz-l Button--lvl-primary Button--aln-center Tappable--inactive']")
time.sleep(1)
submit_button.click()

#лимит
#кнопка продолжить
time.sleep(2)
submit_button = driver.find_element_by_css_selector("[class='Tappable Tappable--ios Button Button--ios Button--sz-xl Button--lvl-primary Button--aln-center Tappable--inactive']")
time.sleep(1)
submit_button.click()

#чекбокс согласие
time.sleep(1)
option1 = driver.find_element_by_css_selector("[class='Tappable Tappable--ios Checkbox Checkbox--ios Tappable--inactive']")
option1.click()
time.sleep(1)
submit_button = driver.find_element_by_css_selector("[class='Tappable Tappable--ios Button Button--ios Button--sz-xl Button--lvl-primary Button--aln-center Tappable--inactive']")
time.sleep(1)
submit_button.click()

#sms sugest passcode
wait = WebDriverWait(driver, 35)
element = wait.until(EC.visibility_of_element_located((By.ID,'passcode')))

textarea = driver.find_element_by_css_selector("#passcode")
time.sleep(2)
textarea.send_keys("1111")



"""
# После выполнения всех действий мы должны не забыть закрыть окно браузера.
#driver.quit()

"""

