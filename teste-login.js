// Importa as funções necessárias do Selenium WebDriver
const { Builder, By, until } = require('selenium-webdriver');

// Função auxiliar que simula digitação lenta, letra por letra, com um pequeno delay
async function digitarLento(elemento, texto, delay = 250) {
  for (const letra of texto) {
    await elemento.sendKeys(letra); // Digita uma letra no elemento
    await new Promise((res) => setTimeout(res, delay)); // Espera antes da próxima letra
  }
}

// Função que realiza o teste de login na página do Hankeds
async function testarHankeds(driver) {
  const url = 'https://www.hankeds.com.br/prova/login2.html';
  await driver.get(url); // Abre a página de login do Hankeds
  await driver.sleep(2000); // Espera 2 segundos para garantir que a página carregue

  // Localiza os campos e o botão de login
  const username = await driver.findElement(By.id('username'));
  const password = await driver.findElement(By.id('password'));
  const botao = await driver.findElement(By.xpath("//button[contains(text(),'Entrar')]"));

  // Digita o nome de usuário lentamente
  await digitarLento(username, 'admin');
  await driver.sleep(500); // Pausa curta

  // Digita a senha lentamente
  await digitarLento(password, 'admin123456');
  await driver.sleep(500); // Pausa curta

  await botao.click(); // Clica no botão de login
  await driver.sleep(4000); // Espera 4 segundos para redirecionamento

  // Captura a URL atual após o clique
  const urlAtual = await driver.getCurrentUrl();

  // Verifica se houve redirecionamento esperado
  if (urlAtual.includes('destino.html')) {
    console.log('✅ [HANKEDS] Teste passou: redirecionado corretamente.');
  } else {
    console.log('❌ [HANKEDS] Teste falhou: redirecionamento não ocorreu.');
  }
}

// Função que realiza o teste de login na página de testes do HerokuApp
async function testarHeroku(driver) {
  const url = 'https://the-internet.herokuapp.com/login';
  await driver.get(url); // Abre a página de login do HerokuApp
  await driver.sleep(2000); // Espera a página carregar

  // Localiza os campos e botão
  const username = await driver.findElement(By.id('username'));
  const password = await driver.findElement(By.id('password'));
  const botao = await driver.findElement(By.css('button.radius'));

  // Digita o usuário e senha com delay
  await digitarLento(username, 'tomsmith');
  await driver.sleep(500);
  await digitarLento(password, 'SuperSecretPassword!');
  await driver.sleep(500);

  await botao.click(); // Clica no botão de login

  // Espera até que a mensagem de sucesso apareça
  const mensagem = await driver.wait(until.elementLocated(By.id('flash')), 5000);
  const texto = await mensagem.getText();

  // Verifica se a mensagem de sucesso foi exibida
  if (texto.includes('You logged into a secure area')) {
    console.log('✅ [HEROKU] Teste passou: login realizado com sucesso.');
  } else {
    console.log('❌ [HEROKU] Teste falhou: mensagem inesperada.');
  }
}

(async function rodarTestes() {
  const { Builder } = require('selenium-webdriver');
  const driver = await new Builder().forBrowser('chrome').build(); // Abre o Chrome com Selenium

  try {
    await testarHankeds(driver);  // ✅ Só o teste Hankeds vai rodar aqui
    // await driver.sleep(2000);
    // await testarHeroku(driver); // ❌ Comentado, não será executado

  } catch (err) {
    console.error('❌ Erro durante execução:', err);
  } finally {
    await driver.quit();
  }
})();
