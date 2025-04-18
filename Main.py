# Importa as bibliotecas necessárias do Selenium e outras auxiliares
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
# Inicializa o navegador Chrome com suporte do WebDriverManager (instala e configura o driver automaticamente)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

# Define a URL da página de login
try:
url = "https://www.hankeds.com.br/prova/login.html"
driver.get(url)
# Espera 2 segundos para garantir que a página esteja carregada
time.sleep(2)

# Define uma função que digita texto lentamente, letra por letra
def digitar_lento(elemento, texto, delay=0.25):
for letra in texto:
elemento.send_keys(letra)
time.sleep(delay)

# Espera até que o campo de usuário esteja presente na página
usuario = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
senha = driver.find_element(By.ID, "password")
botao = driver.find_element(By.XPATH, "//button[contains(text(), 'Entrar')]")

# Simula a digitação do usuário e senha com atraso
digitar_lento(usuario, "admin")
time.sleep(1)
digitar_lento(senha, "admin123456")
time.sleep(1)

botao.click()  # Clica no botão de login
time.sleep(4) # Aguarda o redirecionamento da página

if "destino.html" in driver.current_url:
print(" Teste passou: redirecionado corretamente.")
else:
print(" Teste falhou: redirecionamento não ocorreu.")

time.sleep(5)

 # Em caso de erro durante o teste, exibe mensagem no terminal
except Exception as e:
print(" Erro durante o teste:", str(e))

 # Fecha o navegador ao final do teste (independente se passou ou não)
finally:
driver.quit()