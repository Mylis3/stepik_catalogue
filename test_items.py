# Задание: запуск автотестов для разных языков интерфейса, передавая нужный язык в командной строке.

# 1. Напишите тест, который проверяет, что страница товара на сайте содержит кнопку добавления в корзину. Например, можно проверять товар, доступный по http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/.
# Тест должен запускаться с параметром language следующей командой:
# pytest --language=es test_items.py
# и проходить успешно. Достаточно, чтобы код работал только для браузера Сhrome.
# Ссылка и browser.get(link) должны быть в файле с тестом.

# проверить после выполнения теста может можно удалить импорт pytest (так как уже  есть в файле conftest)?

from selenium.webdriver.common.by import By
import time


def test_check_add_basket_button_is_displayed(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

    browser.get(link)
    time.sleep(30)
    add_button = browser.find_element(
        By.CSS_SELECTOR, ".btn.btn-add-to-basket")

    assert add_button.is_displayed(), "Кнопка добавления в корзину не найдена"
