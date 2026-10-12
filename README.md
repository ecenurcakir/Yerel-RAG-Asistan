Yerel RAG (Soru-Cevap) Asistanı ve Belge Analiz Sistemi

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12%2B-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/Status-Offline%20Ready-success.svg" alt="Status">
  <img src="https://img.shields.io/badge/Architecture-Custom%20RAG-orange.svg" alt="Architecture">
</p>

---

## 📌 Proje Genel Bakışı
Bu proje, harici bir API'ye, bulut tabanlı servislere veya internet bağlantısına **hiçbir şekilde ihtiyaç duymadan**, tamamen yerel (offline) çalışan Python tabanlı bir Soru-Cevap (RAG) asistanıdır. 

Sistem; kullanıcıların yüklediği **PDF, Word (DOCX) ve metin (TXT)** formatındaki belgeleri işleyerek, verilerin gizliliğini korur ve kaynak odaklı en doğru yanıtları üretir.

---

## 🚀 Öne Çıkan Özellikler

* **🔒 %100 Çevrimdışı Çalışma (Offline):** İnternet gerektirmez, tüm veriler ve işlemler tamamen yerel bilgisayarınızda gerçekleşir.
* **📄 Çoklu Format Desteği:** PDF, DOCX ve TXT formatındaki belgeleri okuyup metin tabanlı işleme yeteneği.
* **🧠 Esnek Kelime Eşleştirme Algoritması:** Bire bir cümle eşleşmesi zorunluluğunu ortadan kaldıran, anlam ve anahtar kelime odaklı arama mekanizması.
* **🛡️ Güvenli Yanıt Mekanizması (Anti-Hallucination):** Veritabanında veya belgede bulunmayan konularda yanlış bilgi uydurmak yerine, eksikliği açıkça belirten güvenlik katmanı.
* **📊 Test ve Kontrol Grubu:** Sistemin doğruluk oranını artırmak amacıyla 100 soruluk kapsamlı bir kontrol grubu ile test edilmiştir.

---

## ⚙️ Teknik İşleyiş ve Mühendislik Süreci

Projenin geliştirme aşamasında karşılaşılan zorluklar ve uygulanan çözümler:

1. **Belge Okuma ve Ön İşleme:** Desteklenen formatlardaki dosyalar sisteme alınarak metin bloklarına ayrıştırılır.
2. **Eşleştirme Sorununun Çözümü:** İlk aşamada metnin bire bir aynısı arandığı için esnek sorulara yanıt alınamıyordu. Yapılan kod optimizasyonu ile kelime bazlı tarama mantığına geçilerek bu sorun çözüldü.
3. **Doğrulama ve Güvenlik:** 100 soruluk test setiyle doğruluk kontrolleri yapılarak asistanın kararlı çalışması sağlandı.

---

## 🛠️ Kurulum ve Gereksinimler

### 1. Kütüphanelerin Yüklenmesi
Projenin dosya okuma yetenekleri için gerekli olan Python kütüphanelerini terminalden yükleyin:
```bash
pip install pypdf python-docx
