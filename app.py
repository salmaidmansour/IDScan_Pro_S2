from flask import Flask, render_template, request, redirect, url_for
import pytesseract
import os
import cv2

# Configuration de l'application Flask
app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Configuration de Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Fonction pour prétraiter l'image
def preprocess_image(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return binary

# Fonction pour extraire les données
def extract_data(image_path):
    # Prétraitement de l'image
    processed_image = preprocess_image(image_path)

    # Extraction des textes avec Tesseract
    extracted_text = pytesseract.image_to_string(processed_image, lang='fra+ara')

    # Extraction des champs spécifiques
    data = {
        "Nom": None,
        "Prénom": None,
        "Date de naissance": None,
        "Lieu de naissance": None,
        "Numéro CIN": None,
        "Validité": None,
    }

    lines = extracted_text.splitlines()
    for line in lines:
        if "Nom" in line or "الاسم العائلي" in line:
            data["Nom"] = line.split(":")[-1].strip()
        elif "Prénom" in line or "الاسم الشخصي" in line:
            data["Prénom"] = line.split(":")[-1].strip()
        elif "Date de naissance" in line or "تاريخ الازدياد" in line:
            data["Date de naissance"] = line.split(":")[-1].strip()
        elif "Lieu de naissance" in line or "مكان الازدياد" in line:
            data["Lieu de naissance"] = line.split(":")[-1].strip()
        elif "CIN" in line or "ب.ت.و" in line:
            data["Numéro CIN"] = line.split(":")[-1].strip()
        elif "Validité" in line or "صالحة إلى غاية" in line:
            data["Validité"] = line.split(":")[-1].strip()

    return data

# Route pour scanner une carte
@app.route('/')
def scan():
    return render_template('scan.html')

# Route pour afficher les résultats
@app.route('/result', methods=['POST'])
def result():
    try:
        file = request.files['file']
        if file:
            # Sauvegarde du fichier dans le dossier uploads
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)

            # Extraction des données
            extracted_data = extract_data(file_path)

            # Suppression du fichier uploadé après traitement
            os.remove(file_path)

            return render_template('result.html', data=extracted_data)
    except Exception as e:
        return render_template('error.html', error=str(e))

if __name__ == '__main__':
    # Création du dossier uploads s'il n'existe pas
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.run(debug=True)
