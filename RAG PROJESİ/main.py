import os

def bilgi_getir(soru):
    dosya_yolu = "bilgi.txt"
    if not os.path.exists(dosya_yolu):
        return "Bilgi dosyası bulunamadı."
        
    with open(dosya_yolu, "r", encoding="utf-8") as f:
        icerik = f.read()
        
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
    while True:
        try:
            soru = input("\nSen: ")
            if not soru.strip():
                continue
            if soru.lower() in ['q', 'çıkış']:
                break
                
            cevap = bilgi_getir(soru)
            print(f"Asistan: {cevap}")
        except EOFError:
            break

if __name__ == "__main__":
    asistan_baslat()