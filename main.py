from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
PATH = "C:\Program Files (x86)\chromedriver.exe"


def get_min_specs(game):
    driver = webdriver.Chrome(PATH)

    driver.get("https://store.steampowered.com/")

    search = driver.find_element_by_id("store_nav_search_term")
    search.clear()
    search.send_keys(game)
    search.send_keys(Keys.RETURN)

    try:
        games_links = driver.find_elements_by_partial_link_text(game)
        games_links[0].click()
        print(driver.find_element_by_id("appHubAppName").text)
        print(driver.find_element_by_class_name("game_area_sys_req_leftCol").text)
    except:
        print(game + " not found.")
    driver.quit()


def cookie_clicker():
    driver = webdriver.Chrome(PATH)
    driver.get("https://orteil.dashnet.org/cookieclicker/")

    driver.implicitly_wait(5)

    cookie = driver.find_element_by_id("bigCookie")
    items = [driver.find_element_by_id("product"+str(i)) for i in range(17, -1, -1)]
    counter = driver.find_element_by_id("cookies")

    while True:
        for item in items:
            cookie.click()
            count = int(counter.text.split()[0])
            if item.text != '' and count >= int(item.text.split('\n')[1].replace(',', '')):
                item.click()



if __name__ == '__main__':
    # get_min_specs("Enderal")
    cookie_clicker()
