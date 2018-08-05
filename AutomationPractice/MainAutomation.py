from selenium import webdriver
from selenium.webdriver.common.by import By
from classes import Fazer
from classes import Preenchimento_de_dados

# Cria uma nova instância para o Firefox driver
driver = webdriver.Firefox()

# Acessa a pagina "automationpractice.com"
print(" Abrindo o navegador e acessando a pagina desejada")
driver.get("http://automationpractice.com/index.php")

# Cria o objeto "ObjetoFazer" para realizar os métodos da classe "Açoes"
print(" Selecionando o produto")
ObjetoFazer = Fazer.Açoes(driver)
ObjetoFazer.Encontrar(By.CSS_SELECTOR, "#homefeatured > li:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1) > img:nth-child(1)").click()

# Guarda o nome do produto em uma string para futura validação
NomeProduto = ObjetoFazer.Encontrar(By.CSS_SELECTOR, ".pb-center-column > h1:nth-child(1)").text

# Adiciona ao carrinho
ObjetoFazer.Encontrar(By.CSS_SELECTOR, "button.exclusive").click()

# Validar se o produto foi corretamente adicionado ao carrinho
if ObjetoFazer.Esperar(By.XPATH, "/html/body/div/div[1]/header/div[3]/div/div/div[4]/div[1]/div[1]/h2").text != "Product successfully added to your shopping cart":
        print(" O produto não foi corretamente adicionado ao carrinho")
        driver.quit()

else:

    # Espera o botão de checkout aparecer para poder prosseguir
    print(" Prosseguindo para o checkout")
    ObjetoFazer.Esperar(By.CSS_SELECTOR, "a.btn:nth-child(2) > span:nth-child(1)").click()

    # Faz a validação do nome do produto que foi adicionado ao carrinho
    if ObjetoFazer.Encontrar(By.CSS_SELECTOR, "td.cart_description > p:nth-child(1) > a:nth-child(1)").text != NomeProduto:
        print(" O produto não foi adicionado corretamente ao carrinho")
        driver.quit()

    else:

        # Guarda o valor total da compra em uma string para futura validação
        ValorTotal = ObjetoFazer.Encontrar(By.ID, "total_price").text

        # Continua prosseguindo para o checkout
        ObjetoFazer.Encontrar(By.CSS_SELECTOR, ".standard-checkout > span:nth-child(1)").click()

        # Usa o gerador de caracteres para criar um email
        print(" Inserindo o email para criação de conta")
        inputEmail = ObjetoFazer.Encontrar(By.NAME, "email_create")
        email = ObjetoFazer.gerador_de_caracteres(6)
        inputEmail.send_keys(email, "@email.com")
        inputEmail.submit()

        # Cria o objeto "Preencher" para fazer o preenchimento de dados
        Preencher = Preenchimento_de_dados.Dados(driver)
        Preencher.Cadastro(ObjetoFazer)

        # Valida se o endereço de entrega está correto
        if ObjetoFazer.Esperar(By.XPATH, "/html/body/div/div[2]/div/div[3]/div/form/div/div[2]/div[1]/ul/li[3]").text != Preencher.Rua:
            print(" O endereço de entrega está errado")
            driver.quit()

        else:

            print(" O endereço de entrega está correto")

            #Valida se o endereço de cobrança está correto
            if ObjetoFazer.Encontrar(By.XPATH, "/html/body/div/div[2]/div/div[3]/div/form/div/div[2]/div[2]/ul/li[3]").text != Preencher.Rua:
                print(" O endereço de cobrança está errado")
                driver.quit()

            else:

                print(" O endereço de cobrança está correto")

                # Prossegue para o checkout
                ObjetoFazer.Encontrar(By.NAME, "processAddress").click()

                # Aceita os termos de serviço
                print(" Aceitando os termos de serviço e prosseguindo")
                ObjetoFazer.Encontrar(By.CSS_SELECTOR, ".checkbox > label:nth-child(2)").click()
                ObjetoFazer.Encontrar(By.NAME, "processCarrier").click()

                # Faz a validação do preço total
                if ValorTotal != ObjetoFazer.Encontrar(By.ID, "total_price").text:
                    print(" O valor total da compra está errado")
                    driver.quit()

                else:

                    print(" O valor total da compra está correto")

                    # Seleciona um método de pagamento
                    ObjetoFazer.Encontrar(By.CLASS_NAME, "cheque").click()
                    ObjetoFazer.Encontrar(By.CSS_SELECTOR, "button.button-medium").click()
                    print(" Método de pagamento selecionado")

                    # Valida se a compra foi realizada com sucesso
                    if ObjetoFazer.Encontrar(By.XPATH, "/html/body/div/div[2]/div/div[3]/div/p[1]").text == "Your order on My Store is complete.":
                        print(" A compra foi realizada com sucesso!")

                    else:

                        print(" Houve um erro ao fazer a validação da compra")
