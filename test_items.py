"""
Тесты напсианы и работают для FireFox
"""

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_buttom_dif_lang(browser,browser_lg):
    browser.get(link)
    button = browser.find_element_by_css_selector('button.btn-lg')
    if browser_lg == 'en':
        assert button.text == 'Add to basket'
    elif browser_lg == 'ru':
        assert button.text == 'Добавить в корзину'
    elif browser_lg == 'fr':
        assert button.text == 'Ajouter au panier'
    elif browser_lg == 'es':
        assert button.text == 'Añadir al carrito'

