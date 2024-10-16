import pyautogui
import time
from PIL import ImageChops

def is_page_updated(screenshot1, screenshot2):
    # Compara as duas imagens e verifica se há diferenças
    diff = ImageChops.difference(screenshot1, screenshot2)
    return diff.getbbox() is not None  # True se houver diferença, False se forem iguais

# Tira a primeira captura da tela
screenshot1 = pyautogui.screenshot(region=(0, 0, 1920, 1080))  # Ajuste a região conforme necessário
time.sleep(5)  # Aguardando alguns segundos para uma possível atualização

# Tira a segunda captura da tela
screenshot2 = pyautogui.screenshot(region=(0, 0, 1920, 1080))

# Verifica se houve atualização
if is_page_updated(screenshot1, screenshot2):
    print("A página foi atualizada!")
    pyautogui.press('f')
else:
    print("A página não foi atualizada.")
