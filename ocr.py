from PIL import Image
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r"/opt/homebrew/bin/tesseract"

goruntu_yolu = "/Users/bariskaplan/Desktop/OCR_Demo/autumn_poems.jpg"
goruntu = Image.open(goruntu_yolu)

çıkarılan_metin = pytesseract.image_to_string(goruntu)


print('Çıkarılan metin: ') 
print(çıkarılan_metin)