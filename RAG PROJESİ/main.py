import os
from pypdf import PdfReader
from docx import Document

def dosya_oku():
    # Klasördeki desteklenen dosyaları bulalım
    desteklenen_uzantilar = (".txt", ".pdf", ".docx")
    dosyalar = [f for f in os.listdir(".") if f.lower().endswith(desteklenen_uzantilar)]
    
    if not dosyalar:
        return None, "Bulunduğunuz klasörde okunabilecek .txt, .pdf veya .docx uzantılı bir dosya bulunamadı."
    
    # İlk bulduğu belgeyi otomatik seçebilir veya öncelik verebiliriz
    secilen_dosya = dosyalar[0]
    print(f"[Bilgi] Okunan Belge: {secilen_dosya}")
    
    uzanti = os.path.splitext(secilen_dosya)[1].lower()
    metin = ""
    
    try:
        if uzanti == ".txt":
            with open(secilen_dosya, "r", encoding="utf-8") as f:
                metin = f.read()
                
        elif uzanti == ".pdf":
            reader = PdfReader(secilen_dosya)
            for sayfa in reader.pages:
                sayfa_metni = sayfa.extract_text()
                if sayfa_metni:
                    metin += sayfa_metni + "\n"
                    
        elif uzanti == ".docx":
            doc = Document(secilen_dosya)
            for paragraf in doc.paragraphs:
                metin += paragraf.text + "\n"
                
    except Exception as e:
        return None, f"Dosya okunurken bir hata oluştu: {e}"
        
    return metin, None

def bilgi_getir(soru, icerik):
    # Dosyadaki her bir satırı / paragrafı ayır
    parcalar = [p.strip() for p in icerik.split("\n\n") if p.strip()]
    
    soru_kelimeleri = set(soru.lower().split())
    
    en_iyi_eslesme = "Bu konu hakkında veritabanımda yeterli bilgi bulunmuyor."
    en_cok_ortak = 0
    
    for parca in parcalar:
        parca_kucuk = parca.lower()
        # Sorduğun soru ile metindeki ortak kelimeleri say
        ortak_sayisi = sum(1 for kelime in soru_kelimeleri if len(kelime) > 2 and kelime in parca_kucuk)
        
        if ortak_sayisi > en_cok_ortak:
            en_cok_ortak = ortak_sayisi
            en_iyi_eslesme = parca
            
    if en_cok_ortak == 0:
        return "Bu konu hakkında veritabanımda yeterli bilgi bulunmuyor."
        
    return en_iyi_eslesme

def asistan_baslat():
    print("Yerel RAG Asistanı Başlatılıyor...")
    icerik, hata = dosya_oku()
    if hata:
        print(f"Hata: {hata}")
        return

    print("Asistan hazır! Çıkış yapmak için 'q' veya 'çıkış' yazabilirsiniz.")

    while True:
        try:
            soru = input("\nSen: ")
            if not soru.strip():
                continue
            if soru.lower() in ['q', 'çıkış']:
                break
                
            cevap = bilgi_getir(soru, icerik)
            print(f"Asistan: {cevap}")
        except EOFError:
            break

if __name__ == "__main__":
    asistan_baslat()
