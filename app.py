import os

while True:
    pasta = input(f"Forneça o caminho da pasta: ")
    try:
        arquivos = [f for f in os.listdir(pasta) if os.path.isfile(os.path.join(pasta, f))]
        arquivo_saida = 'lista_de_nomes.txt'
        with open(arquivo_saida, 'w', encoding='utf-8') as f:
            for nome in arquivos:
                f.write(nome + '\n')
        print(f'Arquivo "{arquivo_saida}" criado com sucesso!')
        break
    except:
        print(f'Caminho não encontrado, verifique e forneça novamente!\n')
