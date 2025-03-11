from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('que eu estou na página de login')
def step_impl(context):
    context.driver = webdriver.Chrome()  
    context.driver.get("http://www.automationpractice.pl/")

@when('eu insiro um nome de usuário válido e uma senha válida')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "a.login").click()

    email_field = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, "email"))
    )
    email_field.send_keys("vemser.sala2@teste.com")

    password_field = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, "passwd"))
    )
    password_field.send_keys("123456")

    login_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "SubmitLogin"))
    )
    login_button.click()

@then('eu devo ser redirecionado para a página inicial')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.url_contains("controller=my-account")  
    )
    
    context.driver.quit()