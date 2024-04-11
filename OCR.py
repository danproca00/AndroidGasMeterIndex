import os
from PIL import Image, ImageOps, ImageEnhance, ImageFilter
from pytesseract import image_to_string
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from firebase_admin import credentials, initialize_app, db

# Autentificarea cu Firebase
cred = credentials.Certificate('database-5fdc8-firebase-adminsdk-zfugi-47c04f3337.json')
default_app = initialize_app(cred, {
    'databaseURL': 'https://database-5fdc8-default-rtdb.firebaseio.com/'
})

# Crearea unei referințe către baza de date Firebase
ref = db.reference('index')


try:
    # Autentificarea cu Google Drive
    gauth = GoogleAuth()
    gauth.LoadClientConfigFile('client_secret_770338931975-qeqdlafnd77d12kkbio2udnphtblvva1.apps.googleusercontent.com.json')

    drive = GoogleDrive(gauth)

    # Descarca imaginea de pe Google Drive
    file_id = '1RdQSFGKtTyYp8Pj_HTWmS9WrDDh9PBqh'
    downloaded = drive.CreateFile({'id': file_id})
    downloaded.GetContentFile('image_1.jpg')

    # Redu luminozitatea imaginii
    image_path = 'image_1.jpg'
    image = Image.open(image_path)
    enhancer = ImageEnhance.Brightness(image)
    darker_image = enhancer.enhance(1)
    darker_image.save('darker_image.jpg')

    # Aplica OCR pe imagine
    text = image_to_string(Image.open('darker_image.jpg'))

    # Salvează textul în Firebase
    ref.set(text)

except Exception as e:
    ref.set(f'Eroare')
