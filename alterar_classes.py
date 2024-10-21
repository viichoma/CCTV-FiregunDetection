import os

def alterar_classe_yolo(diretorio, classe_atual=1, nova_classe=0):
    # Iterar sobre todas as pastas no diretório
    for subdir, _, files in os.walk(diretorio):
        for file in files:
            # Verificar se o arquivo é um arquivo .txt
            if file.endswith(".txt"):
                file_path = os.path.join(subdir, file)
                
                # Ler o conteúdo do arquivo
                with open(file_path, 'r') as f:
                    linhas = f.readlines()
                
                # Alterar o primeiro número de cada linha (classe)
                novas_linhas = []
                for linha in linhas:
                    elementos = linha.split()
                    if elementos[0] == str(classe_atual):
                        elementos[0] = str(nova_classe)
                    novas_linhas.append(' '.join(elementos) + '\n')
                
                # Escrever de volta no arquivo
                with open(file_path, 'w') as f:
                    f.writelines(novas_linhas)

# Caminho do diretório
diretorio = r'C:\Users\unico\Downloads\Gun_Action_Recognition_Dataset\Machine_Gun'

# Chamar a função para alterar as classes
alterar_classe_yolo(diretorio)
