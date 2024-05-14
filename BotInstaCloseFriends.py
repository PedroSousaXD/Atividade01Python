from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()

    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com')
        sleep(5)

        username_element = driver.find_element(By.NAME, 'username')
        username_element.clear()
        sleep(2)
        username_element.send_keys(self.username)
        sleep(2)
        password_element = driver.find_element(By.NAME, 'password')
        password_element.clear()
        password_element.send_keys(self.password)
        password_element.send_keys(Keys.RETURN)
        sleep(10)

    def go_to_followers_page(self):
        driver = self.driver
        driver.get('https://www.instagram.com/' + self.username)
        sleep(5)
        followers_button = driver.find_element(By.XPATH, '//a[contains(@href, "/followers/")]')
        followers_button.click()
        sleep(5)

    def add_to_close_friends(self):
        driver = self.driver
        follower_list = driver.find_elements(By.XPATH, '//button[text()="Seguir"]')

        for follower in follower_list:
            try:
                follower.click()
                sleep(2)
                add_to_close_friends_button = driver.find_element(By.XPATH, '//button[text()="Adicionar aos amigos próximos"]')
                add_to_close_friends_button.click()
                sleep(2)
            except Exception as e:
                print(f"Erro ao adicionar o seguidor aos amigos próximos: {str(e)}")
                continue

        print("Todos os seguidores foram adicionados aos amigos próximos.")

Bot = InstagramBot(username='loja590st.vilanova', password='202208704298')
Bot.login()
Bot.go_to_followers_page()
Bot.add_to_close_friends()
