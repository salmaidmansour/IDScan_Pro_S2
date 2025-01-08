# IDScan_Pro_S2

## 🎯 Projet
**IDScan_Pro_S2** est une application innovante qui permet de :
- Scanner une carte nationale marocaine.
- Extraire les données essentielles comme le nom, prénom, date de naissance, numéro CIN, validité, etc.
- Authentifier les utilisateurs avec une double authentification (2FA).

Le projet est organisé en microservices :
- **Service de scan et d'extraction des données** : Implémenté avec **Python** et **Flask**.
- **Authentification double facteur (2FA)** : Backend avec **Spring Boot**, Frontend avec **Angular**.

---

## 📽 Démonstration vidéo
Regardez la démonstration de l'application ici :  
[![Démonstration vidéo](https://img.youtube.com/vi/placeholder/0.jpg)](C:\Users\PC\Desktop\Recording_CIN_Scan.mp4)  
*(Téléchargez la vidéo pour voir la démonstration si le lien ne fonctionne pas.)*

---

## ⚙️ Installation et configuration

### **1. Installation des dépendances pour le service Python**
Assurez-vous d'avoir installé Python 3.x et Tesseract OCR sur votre machine.

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/salmaidmansour/IDScan_Pro_S2.git
   cd IDScan_Pro_S2
2. Créez un environnement virtuel :

python -m venv .venv
source .venv/bin/activate    # Sur macOS/Linux
.venv\Scripts\activate       # Sur Windows

3.Installez les bibliothèques nécessaires :

pip install -r requirements.txt

4. Assurez-vous que Tesseract est installé sur votre machine. Téléchargez-le depuis Tesseract OCR:  https://github.com/tesseract-ocr/tesseract

5. Lancez le service Flask :
python app.py

6. Accédez à l'application via votre navigateur :
http://127.0.0.1:5000







