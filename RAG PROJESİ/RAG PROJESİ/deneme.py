import sqlite3
from foundry_local import ModelClient

# 1. Metni oku ve parçalara böl
def metni_oku_ve_bol(dosya_yolu):
    with open(dosya_yolu, "r", encoding="utf-8") as file:
        tam_metin = file.read()
    parcalar = tam_metin.split("\n\n")
    return [p.strip() for p in parcalar if len(p.strip()) > 10]

# 2. Veritabanını kur ve verileri kaydet
def veritabanini_hazirla(parcalar):
    conn = sqlite3.connect("rag_veritabani.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT,
            embedding TEXT
        )
    ''')
    cursor.execute('DELETE FROM documents')
    for parca in parcalar:
        cursor.execute("INSERT INTO documents (content, embedding) VALUES (?, ?)", (parca, "[0.0, 0.0]"))
    conn.commit()
    conn.close()

# 3. Gerçek Model ile Asistanı Başlat
def asistan_baslat():
    # Veritabanından bağlamı çek
    conn = sqlite3.connect("rag_veritabani.db")
    cursor = conn.cursor()
    cursor.execute("SELECT content FROM documents LIMIT 3")
    sonuclar = cursor.fetchall()
    conn.close()
    
    baglam = "\n---\n".join([satir[0] for satir in sonuclar])
    
    print("="*50)
    print("Yapay Zeka Modeli Hazırlanıyor...")
    print("LÜTFEN DİKKAT: Model ilk kez çalıştırılıyorsa, bilgisayarınıza indirilmesi birkaç dakika sürebilir. Lütfen bekleyin.")
    print("="*50)
    
    # Foundry Local üzerinden modeli yüklüyoruz
    client = ModelClient("phi-1.5-mini")
    
    print("\n🤖 GERÇEK YEREL RAG ASİSTANI HAZIR 🤖")
    print("Çıkmak için 'q' veya 'çıkış' yazın.")
    print("="*50)
    
    while True:
        soru = input("\nSen: ")
        if soru.lower() in ['q', 'çıkış']:
            print("Asistan kapatılıyor. Görüşmek üzere!")
            break
            
        print("Asistan: Düşünüyor (Cevap üretiliyor)...")
        
        sistem_istemi = f"Sen yardımcı bir asistansın. Kullanıcının sorusunu SADECE aşağıdaki metne göre cevapla. Bilgi yoksa 'Bilmiyorum' de.\n\nMETİN:\n{baglam}"
        
        try:
            cevap = client.completeChat(
                messages=[
                    {"role": "system", "content": sistem_istemi},
                    {"role": "user", "content": soru}
                ]
            )
            print(f"Asistan: {cevap}")
        except Exception as e:
            print(f"Asistan yanıt üretirken bir hata oluştu: {e}")

if __name__ == "__main__":
    parcalar = metni_oku_ve_bol("bilgi.txt")
    veritabanini_hazirla(parcalar)
    asistan_baslat()