import os
import cv2

# Caminho da pasta principal que contém as subpastas
dataset_dir = r'C:\Users\unico\Downloads\Gun_Action_Recognition_Dataset\Handgun'

# Função para extrair frames de um vídeo e salvar com o nome adequado
def extrair_frames(video_path, output_folder, folder_name):
    # Captura o vídeo
    cap = cv2.VideoCapture(video_path)
    frame_count = 0
    
    # Loop para extrair frames
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        # Gera o nome do frame baseado no nome da pasta e no número do frame
        frame_filename = os.path.join(output_folder, f"{folder_name}_frame_{frame_count:04d}.jpg")
        cv2.imwrite(frame_filename, frame)
        frame_count += 1

    cap.release()

# Percorre todas as pastas dentro do diretório
for folder in os.listdir(dataset_dir):
    folder_path = os.path.join(dataset_dir, folder)
    
    # Verifica se é uma pasta
    if os.path.isdir(folder_path):
        # Procura por arquivos .mp4 dentro da pasta
        for file in os.listdir(folder_path):
            if file.endswith('.mp4'):
                video_path = os.path.join(folder_path, file)
                # Extrai os frames e salva na mesma pasta
                extrair_frames(video_path, folder_path, folder)
