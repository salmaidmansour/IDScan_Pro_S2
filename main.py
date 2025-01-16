import cv2
import pytesseract
import numpy as np
from flask import Flask, request, jsonify

app = Flask(__name__)

# Configuration de Tesseract OCR (ajustez selon votre environnement)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Chemin pour Windows

# Fonction pour extraire du texte à partir d'une région d'intérêt (ROI)
def extract_text_from_roi(image, x, y, w, h):
    roi = image[y:y + h, x:x + w]  # Extraire la région spécifique
    roi = cv2.GaussianBlur(roi, (3, 3), 0)  # Réduction du bruit
    _, roi_bin = cv2.threshold(roi, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    custom_config = r'--oem 3 --psm 6'  # Configuration pour Tesseract
    text = pytesseract.image_to_string(roi_bin, lang="eng+fra", config=custom_config)
    return text.strip()

@app.route('/process_image', methods=['POST'])
def process_image():
    try:
        # Récupérer l'image envoyée
        file = request.files['image']
        image = np.frombuffer(file.read(), np.uint8)
        image = cv2.imdecode(image, cv2.IMREAD_UNCHANGED)  # Charger avec tous les canaux (y compris alpha)

        if image is None:
            return jsonify({"error": "Erreur : Impossible de lire l'image."}), 400

        # Si l'image a un canal alpha (transparence), on le supprime
        if image.shape[2] == 4:
            image = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)  # Convertir BGRA en BGR (supprime le canal alpha)

        # Étape 1 : Convertir l'image en niveaux de gris
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Définir les nouvelles coordonnées des champs à extraire (zones)
        zones = {
            "prenom": (40, 320, 300, 45),  # Zone "Prénom"
            "nom": (30, 450, 260, 45),  # Zone "Nom"
            "date_naissance": (390, 515, 250, 45),  # Zone "Date de naissance"
            "adresse": (60, 650, 450, 45),  # Zone "Lieu de naissance"
            "numero_cin": (1150, 780, 300, 45)  # Zone "Numéro CIN"
        }

        # Extraction et affichage des résultats
        results = {}
        for key, (x, y, w, h) in zones.items():
            results[key] = extract_text_from_roi(gray, x, y, w, h)

        # Structurer les résultats en JSON
        return jsonify(results)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)
