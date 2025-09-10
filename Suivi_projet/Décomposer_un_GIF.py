from PIL import Image

def gif_to_frames(gif_path, output_folder):
    """
    Décompose un GIF animé en images individuelles.

    Args:
        gif_path (str): Chemin d'accès au fichier GIF.
        output_folder (str): Dossier de sortie pour les images.
    """
    try:
        gif = Image.open(gif_path)
        frame_count = 0  # Initialisation de frame_count ici
        while True:
            current_frame = gif.copy()
            current_frame.save(f"{output_folder}/frame_{frame_count:04d}.png")
            frame_count += 1
            gif.seek(gif.tell() + 1)
    except EOFError:
        pass
    return frame_count #Retourne le nombre d'images

# Utilisation
gif_path = "Hypnose_.gif"
output_folder = "images(Hypnose)_gif"

import os
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

frame_count = gif_to_frames(gif_path, output_folder)
print(f"Le GIF a été décomposé en {frame_count} images dans le dossier '{output_folder}'.")