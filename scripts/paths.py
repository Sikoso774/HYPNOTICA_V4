# scripts/paths.py
import sys
import os

def get_resource_path(relative_path):
    """
    Retourne le chemin absolu d'une ressource.
    - Si exécuté par PyInstaller (bundle unique ou dossier), le chemin est relatif à sys._MEIPASS.
    - Si exécuté comme script Python, le chemin est relatif à la racine du projet
      (le dossier contenant 'main.py', 'assets/', 'hyphose_frames/', etc.).
    """
    try:
        # Cas PyInstaller (sys._MEIPASS est le répertoire temporaire du bundle)
        base_path = sys._MEIPASS
    except AttributeError: # Ancien: except Exception:
        # Cas exécution normale en script Python (PyCharm, "python script.py", etc.)

        # __file__ est le chemin complet du script actuel (ex: .../MonProjet/scripts/utils_paths.py)
        # os.path.dirname(__file__) donne le répertoire du script (ex: .../MonProjet/scripts/)
        # os.path.join(..., os.pardir) remonte au répertoire parent (ex: .../MonProjet/)
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

    return os.path.join(base_path, relative_path)