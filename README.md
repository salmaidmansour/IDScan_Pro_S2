# 🆔 **IDScan_Pro_S2**  
### 🚀 **Une solution innovante pour scanner et extraire des données des cartes nationales marocaines**

---

## 🎯 **Projet**

**IDScan_Pro_S2** est une application web puissante qui :  
- 🖼️ **Scanne les cartes nationales marocaines.**  
- 🧾 **Extrait des informations clés**, comme :  
  - **Nom**  
  - **Prénom**  
  - **Date de naissance**  
  - **Numéro CIN**  
  - **Validité**, etc.  
- 🔐 **Authentifie les utilisateurs avec une double authentification (2FA).**  

Ce projet est organisé en **microservices** :  
1. 🖥️ **Service de scan** : Implémenté en **Python** avec Flask et Tesseract OCR.  
2. 🔐 **Authentification 2FA** : Backend en **Spring Boot**, Frontend en **Angular**.  

---

## 📽 **Démonstration vidéo**

### Regardez la vidéo de démonstration de l'application ici :  
📹 [**Voir la vidéo de démonstration**](https://drive.google.com/file/d/1gfdKeJfwDkK2hvqw44vo5eMU2aRwnLm5/view?usp=sharing)  

*(Cliquez sur le lien pour visualiser la démonstration.)*

---

## ⚙️ **Installation et configuration**

### **1. Prérequis**
- 🐍 **Python** : Version 3.x  
- 📦 **pip** : Gestionnaire de paquets Python  
- 🖼️ **Tesseract OCR** : Installez-le depuis [Tesseract OCR](https://github.com/tesseract-ocr/tesseract).  

---

### **2. Installation pour le service Python**
Suivez ces étapes pour configurer et exécuter le service de scan :  

1. **Clonez le dépôt GitHub** :  
   ```bash
   git clone https://github.com/salmaidmansour/IDScan_Pro_S2.git
   cd IDScan_Pro_S2
