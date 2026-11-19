import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_painel_controle_oxigenio(driver):
    try:
        caminho_html = os.path.abspath("web/painel.html")
        driver.get(f"file://{caminho_html}")
        
        input_cota = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "cota-oxigenio"))
        )
        input_cota.send_keys("20")
        
        botao_enviar = driver.find_element(By.ID, "btn-solicitar")
        botao_enviar.click()
        
        status_mensagem = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "status-mensagem"))
        )
        assert "Sucesso" in status_mensagem.text
        
    except Exception as e:
        driver.save_screenshot("evidencia_falha.png")
        raise e