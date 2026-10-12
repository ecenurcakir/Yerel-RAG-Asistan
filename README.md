## Yerel RAG Asistanı

Bu proje, internet bağlantısına **hiçbir şekilde ihtiyaç duymadan**, tamamen yerel (offline) çalışan Python tabanlı bir Soru-Cevap (RAG) asistanıdır. Sistem; kullanıcıların yüklediği **PDF, Word ve metin** formatındaki belgeleri işleyerek, verilerin gizliliğini korur ve kaynak odaklı çalışarak en doğru yanıtları üretir.

---

## Özellikler

* **%100 Çevrim dışı Çalışma:** İnternet gerektirmez, tüm veriler ve işlemler tamamen yerel bilgisayarınızda gerçekleşir.
* **Çoklu Format Desteği:** PDF, DOCX ve TXT formatındaki belgeleri okuyup metin tabanlı işleme yeteneği.
* **Esnek Kelime Eşleştirme Algoritması:** Bire bir cümle eşleşmesi zorunluluğunu ortadan kaldıran, anlam ve anahtar kelime odaklı arama mekanizması.
* **Güvenli Yanıt Mekanizması:** Veritabanında veya belgede bulunmayan konularda yanlış bilgi uydurmak yerine, eksikliği açıkça belirten güvenlik katmanı.

---

## Kurulum ve Gereksinimler
Kütüphanelerin Yüklenmesi:

Projenin dosya okuma yetenekleri için gerekli olan Python kütüphanelerini terminalden yükleyin:

pip install pypdf python-docx

Çalıştırma Adımları ve Kullanım Rehberi:

Proje klasörünü bilgisayarınıza indirin.

Okutmak istediğiniz belgeyi ve main.py dosyasını aynı dizine yerleştirin.

Terminalde python main.py komutunu çalıştırarak asistanı aktif hale getirin.

Konsolda belgenizle ilgili soruları yazarak anında kaynak odaklı yanıtlar alın.
