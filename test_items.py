from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_find_button_add_to_basket(browser):
    browser.get(link)
    try:
        button = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
    except NoSuchElementException:
        assert False, "Кнопка добавления в корзину НЕ найдена"

