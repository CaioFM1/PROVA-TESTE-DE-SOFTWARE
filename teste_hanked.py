from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

url = "https://the-internet.herokuapp.com/login"

try:
    driver.get(url)
    time.sleep(2)

    def digitar_lento(elemento, texto, delay=0.25):
        for letra in texto:
            elemento.send_keys(letra)
            time.sleep(delay)

    usuario = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
    senha = driver.find_element(By.ID, "password")

    # ⛳ Aqui está a correção do botão:
    botao = driver.find_element(By.CSS_SELECTOR, "button.radius")

    digitar_lento(usuario, "tomsmith")
    time.sleep(1)
    digitar_lento(senha, "SuperSecretPassword!")
    time.sleep(1)

    botao.click()
    time.sleep(3)

    mensagem = driver.find_element(By.ID, "flash").text
    if "You logged into a secure area!" in mensagem:
        print("✅ Teste passou: login realizado com sucesso.")
    else:
        print("❌ Teste falhou: mensagem inesperada.")

except Exception as e:
    print("❌ Erro durante o teste:", str(e))

finally:
    driver.quit()
