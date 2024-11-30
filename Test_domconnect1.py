from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url = "https://proxy6.net/"

def get_chromedriver(use_proxy=False, user_agent=None):
    chrome_options = webdriver.ChromeOptions()
    # Использование прокси, нужно ввести действующий адрес прокси
    if use_proxy:
        chrome_options.add_argument('--proxy-server=3.229.228.77:3128')

    if user_agent:
        chrome_options.add_argument(f'--user-agent={user_agent}')
    driver = webdriver.Chrome(executable_path="C:\\chromedriver\\chromedriver.exe", options=chrome_options)

    return driver


def is_valid_ip(ip):
    parts = ip.split('.')
    return len(parts) == 4 and all(part.isdigit() and 0 <= int(part) <= 255 for part in parts)


def main():
    try:
        # Использование прокси для открытия сайта=True, не использовать=False
        driver = get_chromedriver(use_proxy=False, user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                                                             'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6595.190 Safari/537.36')
        driver.get(url)
        time.sleep(5)
        driver.find_element_by_xpath('//html/body/div[1]/header/div/ul[2]/li[2]/a').click()
        time.sleep(5)
        login_input = driver.find_element_by_xpath('//*[@id="form-login"]/div[1]/div/input')
        # Тут можно вынести логин и пароль в отдельный файлик например, а не вписывать в коде
        login_input.send_keys("tzpythondemo@domconnect.ru")
        pass_input = driver.find_element_by_xpath('//*[@id="login-password"]')
        pass_input.send_keys("kR092IEz")
        # Ждем ввод капчи 60сек
        time.sleep(60)
        driver.find_element_by_xpath('//*[@id="form-login"]/div[7]/button')
        q = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div/div[2]/table/tbody')
        w = q.find_elements_by_tag_name('li')
        # Лучше было бы использовать регулрные выражения для поиска ip-адреса, но т.к в задании про них не было
        # указано, решаем в лоб, через поиск трех точек и одного двоеточия.
        # И поиск даты тоже в лоб поиск двух точек, запятой, и двоеточия и отсечением остатка дней до кончания
        # действия самого ip-адреса

        for i in w:
            i.find_element_by_class_name('right')
            ip = i.find_element_by_class_name('right').text.split(':')
            # Проверка валидности ip адреса
            if is_valid_ip(ip[0]):
                print(i.find_element_by_class_name('right').text, end=' -')
            # Проверка валидности даты
            if (i.find_element_by_class_name('right').text).count('.') == 2 and ":" in i.find_element_by_class_name(
                    'right').text:
                print((i.find_element_by_class_name('right').text)[
                      (i.find_element_by_class_name('right').text).find(' '):])

        driver.quit()
    except Exception:
        pass


if __name__ == '__main__':
    main()
