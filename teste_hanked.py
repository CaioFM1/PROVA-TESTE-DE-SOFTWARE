# Importa as bibliotecas necessárias do Selenium e outras
from selenium import webdriver  
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service  
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC 
from webdriver_manager.chrome import ChromeDriverManager  
import time 

# Cria o driver do Chrome com o ChromeDriver instalado automaticamente
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Maximiza a janela do navegador para melhor visualização
driver.maximize_window()

# Define a URL da página de login que será testada
url = "https://the-internet.herokuapp.com/login"

try:
    # Acessa a página
    driver.get(url)

    # Aguarda 2 segundos para garantir que a página carregou
    time.sleep(2)

    # Define uma função que simula digitação lenta (letra por letra)
    def digitar_lento(elemento, texto, delay=0.25):
        for letra in texto:
            elemento.send_keys(letra)  # Envia uma letra
            time.sleep(delay)  # Aguarda um pouco antes de enviar a próxima

    # Espera até que o campo de usuário esteja presente na página
    usuario = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
    
    # Localiza o campo de senha diretamente
    senha = driver.find_element(By.ID, "password")

    # Localiza o botão de login usando seletor CSS
    botao = driver.find_element(By.CSS_SELECTOR, "button.radius")

    # Digita o nome de usuário lentamente
    digitar_lento(usuario, "tomsmith")
    time.sleep(1)  # Pausa antes de digitar a senha

    # Digita a senha lentamente
    digitar_lento(senha, "SuperSecretPassword!")
    time.sleep(1)  # Pausa antes de clicar

    # Clica no botão de login
    botao.click()
    time.sleep(3)  # Aguarda a resposta da página

    # Captura a mensagem que aparece após o login
    mensagem = driver.find_element(By.ID, "flash").text

    # Verifica se a mensagem de sucesso está presente no texto
    if "You logged into a secure area!" in mensagem:
        print("✅ Teste passou: login realizado com sucesso.")
    else:
        print("❌ Teste falhou: mensagem inesperada.")

# Caso aconteça algum erro no processo, exibe a mensagem de erro
except Exception as e:
    print("❌ Erro durante o teste:", str(e))

# Encerra o navegador, independente de sucesso ou falha
finally:
    driver.quit()
