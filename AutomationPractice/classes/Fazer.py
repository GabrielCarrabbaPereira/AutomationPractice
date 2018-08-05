from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import random
import string
from selenium.webdriver.common.by import By

class Açoes:
    def __init__(self, driver):
        self.driver = driver
# Encontra um elemento
    def Encontrar(self, tipo, onde):
        return self.driver.find_element(tipo, onde)
###--------------------------------------------------------------------------------------------

# Espera um elemento ser clicável
    def Esperar(self, tipo, onde):
        return WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((tipo, onde)))
###--------------------------------------------------------------------------------------------

# Gera caracteres aleatórios
    def gerador_de_caracteres(self, size):
        char = string.ascii_uppercase + string.digits
        return ''.join(random.choice(char) for i in range(size))
###--------------------------------------------------------------------------------------------
