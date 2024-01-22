# PROJETO DE AUTOMAÇÃO DE TAREFAS 

# PASSO A PASSO DO CODIGO

# PASSO 1 - ENTRAR NO SISTEMA DA EMPRESA
    #https://dlp.hashtagtreinamentos.com/python/intensivao/login

    # BAIXAR UMA BIBLIOTECA EM PYTHON 
         # 1 - pyautogui (Ferramenta de RPA) pip install pyautogui

# ENTÃO VC IMPORTA A BIBLIOTECA QUE VC VAI USAR 
import pyautogui
import time

pyautogui.PAUSE = 3 #  aqui estamos programando uma pausa de 1 segundo em cada comando da janela 

# aperta a tecla do windows (command + barra de espaço )
pyautogui.press('win')
# digita o nome do programa (Nesse Caso é o Google Chrome)
pyautogui.write('google chrome')
# apertar enter 
pyautogui.press('enter')

# aqui é comando para esperar depois da tela ou seja nesse lugar especifico
# exemplo uma pausa de 10 segundos na tela 
time.sleep(3) # espera 10 segundos nessa linha de codigo !!!!

# CLICAR NO PERFIL - ESCOLHIDO 
pyautogui.click(x=590, y=332) # cordenadas do mouse 

# CLICAR NA BARRA DE URL
pyautogui.click(x=218, y=59)

# DIGITAR A URL 
pyautogui.write('https://www.youtube.com/')

# PRESSIONAR ENTER 
pyautogui.press('enter')

# TEMPO DE ESPERA 
time.sleep(2)

# JANELA DO YOUTUBE ESCOLHIDA  
pyautogui.click(x=778, y=327) # Aqui local escolhido para clicar 

# AMPLIAR A JANELA DO YOUTUBE
pyautogui.click(x=836, y=607) 

# quando for um formulario basta apenas colocar o 'tab'
  # pyautogui.press('tab') aqui pula o campo para o proximo 


# digitar o linnk 
# AQUI NESSE CASO CRIAMOS UMA VARIAVEL PARA O LINK 
    # 1 - link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
    # pyautogui.write(link)


#-----------------------------------EXEMPLOS----------------------------------
# clicar ---> pyautogui.click
# escrever ---> pyautogui.write
# apertar uma tecla  --- > pyautogui.press
# apertar uma tecla de atalho --> pyautogui..hotkey( TECLA DE ATALHO)
# rolar a pagina --> pyautogui.scroll (numeros positivos para cima / numeros negativos para baixo)


# pyautogui.press('win') # AQUI DEMOS UM COMANDO PARA ABRIR UMA JANELA WINDONS 
#-----------------------------------------------------------------------------

# PASSO 2 - FAZER O LOGIN

    # 1-> AQUI USAMOS O ARQUIVO AUXILIAR PARA AJUDAR A ACHAR A POSIÇÃO DO MOUSE 
    #      INTERESSANTE PARA ACHAR A POSIÇÃO NO EIXO X E Y !!!!!!

#-------------------------------------------------------------------------------

# PASSO 3 - IMPORTAR A BASE DE DADOS 

     # BAIXAR UMA BIBLIOTECA EM PYTHON 
         # 1 - pandas numpy openpyxl (3 bibliotecas )
#import pandas

#tabela = pandas.read_csv('produtos.csv')
#print(tabela)

#for linha in tabela.index:
 # uuiuhuiuhiu # aqui vc coloca o comando que vai ser executado mais de 1 vez 

# PASSO 4 - CADASTRAR UM PRODUTO

# PASSO 5 - REPETIR ATÉ ACABAR A BASE DE DADOS 
