import pyautogui
from time import sleep

# 1- Clicar e digitar meu usuario
pyautogui.click(1092,554,duration=0.5)
pyautogui.write('kaio')
# 2- Clicar e digitar minha senha
pyautogui.click(1092,581,duration=0.5)
pyautogui.write('123')
# 3- Clicar em "entrar"
pyautogui.click(1004,610,duration=0.5)
# 4- Extrair cada produto
with open('produtos.txt','r') as arquivo:
    for linha in arquivo:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]
#    1- clicar e digitar produto
pyautogui.click(717,532,duration=0.5)
pyautogui.write(produto)
#    2- clicar e digitar quantidade
pyautogui.click(700,559,duration=0.5)
pyautogui.write(quantidade)
#    3- clicar e digitar preço
pyautogui.click(693,579,duration=0.5)
pyautogui.write(preco)
#    4- clicar e registrar
pyautogui.click(594,737,duration=0.5)
sleep(1)