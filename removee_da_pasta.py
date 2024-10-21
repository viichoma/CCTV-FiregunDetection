import os
import shutil

# Caminho da pasta onde estão as pastas com arquivos
base_path = r'C:\Users\unico\Downloads\K-Fold\Fold2\train'

# Loop pelas pastas dentro da pasta principal
for folder_name in os.listdir(base_path):
    folder_path = os.path.join(base_path, folder_name)
    
    # Verifica se o item é uma pasta
    if os.path.isdir(folder_path):
        # Move todos os arquivos da pasta para o diretório raiz
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            
            # Se o arquivo for 'label.json' ou 'video.mp4', deletar
            if file_name == 'label.json' or file_name == 'video.mp4':
                os.remove(file_path)  # Deleta o arquivo
                print(f"Arquivo {file_name} deletado.")
            else:
                # Caso contrário, mover o arquivo
                shutil.move(file_path, base_path)
                print(f"Arquivo {file_name} movido.")

        # Remove a pasta vazia
        os.rmdir(folder_path)

print("Processo concluído com sucesso!")
