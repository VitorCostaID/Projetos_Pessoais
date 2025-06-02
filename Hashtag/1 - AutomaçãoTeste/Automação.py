import openpyxl
import pyperclip
import pyautogui
import time

# Abrir a planilha na variável workbook
workbook = openpyxl.load_workbook('produtos_ficticios.xlsx')

# Carregar a aba "Produtos"
sheet_produtos = workbook['Produtos']

# Tempo de delay de execução de cada código.
pyautogui.PAUSE = 0.5

# Para cada linha na planilha faça:
for linha in sheet_produtos.iter_rows(min_row=2):
    # Armazene em nome_produto o valor da linha correspondente
    # e coluna: linha[numero da coluna].
    nome_produto = linha[0].value

    # Pyperclip usado para conseguir copiar atributos e caracteres
    # Especiais.
    pyperclip.copy(nome_produto)

    # Clicar no botão certo.
    pyautogui.click(x=1228, y=334)

    # Inserir informação copiada anteriormente.
    pyautogui.hotkey('ctrl', 'v')

    #ir para próxima linha
    pyautogui.press("tab")

    descricao = linha[1].value
    pyperclip.copy(descricao)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press("tab")

    categoria = linha[2].value
    pyperclip.copy(categoria)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press("tab")

    codigo_produto = linha[3].value
    pyperclip.copy(codigo_produto)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press("tab")

    peso = linha[4].value
    pyperclip.copy(peso)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press("tab")

    dimensoes = linha[5].value
    pyperclip.copy(dimensoes)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press("tab")
    # Ir para próxima página
    pyautogui.press("enter")

    #Esperar a página carregar
    time.sleep(3)

    preco = linha[6].value
    pyautogui.click(x= 1183, y = 373)
    pyperclip.copy(preco)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press("tab")

    quantidade = linha[7].value
    pyperclip.copy(quantidade)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press("tab")

    data_de_validade = linha[8].value
    pyperclip.copy(data_de_validade)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press("tab")

    cor = linha[9].value
    pyperclip.copy(cor)
    pyautogui.hotkey('ctrl', 'v')

    tamanho = linha[10].value
    pyperclip.copy(tamanho)
    pyautogui.click(x= 1185, y = 716)

    if(tamanho == "Pequeno"):
        pyautogui.press('enter')
    elif(tamanho == "Médio"):
        pyautogui.press('down')
        pyautogui.press('enter')
    else:
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('enter')
    pyautogui.press("tab")

    material = linha[11].value
    pyperclip.copy(material)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press("tab")
    pyautogui.press('enter')

    time.sleep(3)

    fabricante = linha[12].value
    pyautogui.press("tab")
    pyperclip.copy(fabricante)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press("tab")

    pais_origem = linha[13].value
    pyperclip.copy(pais_origem)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press("tab")

    observacoes = linha[14].value
    pyperclip.copy(observacoes)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press("tab")

    codigo_barra = linha[15].value
    pyperclip.copy(codigo_barra)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press("tab")

    localizacao_armazem = linha[16].value
    pyperclip.copy(localizacao_armazem)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.click(x= 1607, y = 187, duration=1)
    pyautogui.click(x= 1437, y = 607, duration=1)

    time.sleep(3)


