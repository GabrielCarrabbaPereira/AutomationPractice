from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
#from selenium.webdriver.support import expected_conditions as EC
from classes import Fazer

class Dados:
    def __init__(self, driver):
# Dados a serem utilizados no cadastramento
        self.PrimeiroNome = "Gabriel"
        self.UltimoNome = "Pereira"
        self.DiaNascimento = "12"
        self.MesNascimento = "8"
        self.AnoNascimento = "1998"

        self.Rua = "Rua das Flores"
        self.Cidade = "Porto ALegre"
        self.Estado = "Delaware"
        self.Cep = "55555"

        self.TelefoneCelular = "123456789"

        self.AddressAlias = "Teste"

        self.driver = driver
###------------------------------------------

# Método para preencher os dados de cadastramento
    def Cadastro(self, ObjetoFazer):
        print(" Preenchendo os dados de cadastramento")

        # Seleciona o gênero
        ObjetoFazer.Esperar(By.ID, "id_gender1").click()
        ###-------------------------------------------------

        # Escreve o nome e sobrenome
        inputPrimeiroNome = ObjetoFazer.Encontrar(By.ID, "customer_firstname")
        inputPrimeiroNome.send_keys(self.PrimeiroNome)             # Nome
        inputUltimoNome = ObjetoFazer.Encontrar(By.ID, "customer_lastname")
        inputUltimoNome.send_keys(self.UltimoNome)                 # Sobrenome
        ###--------------------------------------------------------------------

        # Gera uma senha e preenche o campo referente a mesma
        inputSenha = ObjetoFazer.Encontrar(By.ID, "passwd")         # Senha
        inputSenha.send_keys(ObjetoFazer.gerador_de_caracteres(8))  # Senha
        ###--------------------------------------------------------------------

        # Preenche os dados relacionados a data de nascimento
        selectDay = Select(ObjetoFazer.Encontrar(By.ID, "days"))  # Dia
        selectDay.select_by_value(self.DiaNascimento)             # Dia

        selectMonth = Select(ObjetoFazer.Encontrar(By.ID, "months"))  # Mês
        selectMonth.select_by_value(self.MesNascimento)               # Mês

        selectYear = Select(ObjetoFazer.Encontrar(By.ID, "years"))  # Ano
        selectYear.select_by_value(self.AnoNascimento)              # Ano
        ###----------------------------------------------------------------------

        # Preenche os dados relacionados ao endereço
        inputRua = ObjetoFazer.Encontrar(By.ID, "address1")  # Rua
        inputRua.send_keys(self.Rua)                         # Rua

        inputCidade = ObjetoFazer.Encontrar(By.ID, "city")  # Cidade
        inputCidade.send_keys(self.Cidade)                  # Cidade

        selectEstado = Select(ObjetoFazer.Encontrar(By.ID, "id_state"))  # Estado
        selectEstado.select_by_visible_text(self.Estado)                 # Estado

        inputCep = ObjetoFazer.Encontrar(By.ID, "postcode")  # Cep
        inputCep.send_keys(self.Cep)                         # Cep

        inputMPhone = ObjetoFazer.Encontrar(By.ID, "phone_mobile")  # Telefone Celular
        inputMPhone.send_keys(self.TelefoneCelular)                 # Telefone Celular

        inputAlias = ObjetoFazer.Encontrar(By.ID, "alias")  # Address Alias
        inputAlias.clear()                                  # Address Alias
        inputAlias.send_keys(self.AddressAlias)             # Address Alias
        ###----------------------------------------------------------------------------

        # Envia o registro de dados
        ObjetoFazer.Encontrar(By.ID, "submitAccount").click()
###-----------------------------------------------------------------------------------
