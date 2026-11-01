# 7 · İşletmelere ne satabilirsin?

İşletmeler "otomasyon" satın almaz; **zaman, kaçırılmayan müşteri ve daha az hata** satın alır. Bu bölüm, kurduğun sistemi bir hizmete dönüştürmenin yol haritası.

## 7.1 Sektör sektör otomasyon fikirleri

| Sektör | Sorun | Satabileceğin sistem | Kullanılan araçlar |
|---|---|---|---|
| **Kafe / restoran** | Mesajlara geç dönülüyor, rezervasyon karışıyor | WhatsApp menü + rezervasyon asistanı, Google yorumlarına AI ile yanıt taslağı | WhatsApp, Google Sheets/Calendar, AI |
| **Kuaför / güzellik salonu** | Randevuya gelmeyen müşteriler | Randevu onayı + 1 gün önce hatırlatma, boşalan saati bekleme listesine duyurma | WhatsApp, Google Calendar |
| **Klinik / diş hekimi** | Telefon trafiği, randevu iptalleri | Randevu hatırlatma, kontrol zamanı bildirimi, ön bilgi formu | WhatsApp, Form, Calendar (sağlık verisi için bkz. Bölüm 8) |
| **Emlak ofisi** | Gelen talepler kayboluyor | Web formu/ilan sitesi talebini CRM'e yazma, anında otomatik yanıt, AI ile ilan açıklaması | Webhook, Google Sheets/CRM, AI |
| **E-ticaret** | Aynı sorular, sipariş takibi | Sipariş durumu bildirimi, SSS AI asistanı, ürün açıklaması üretimi, stok uyarısı | Shopify/WooCommerce, WhatsApp/e-posta, AI |
| **Muhasebe / ofis** | Manuel fatura girişi | E-postadaki faturalardan veri çekip tabloya yazma, tahsilat hatırlatması | Gmail, OCR/AI, Google Sheets |
| **Ajans / içerik üreticisi** | İçerik üretimi zaman alıyor | Tek mesajla senaryo → video render → planlı paylaşım | Telegram, AI, Creatomate, Buffer |
| **Kurs / eğitim** | Kayıt sonrası manuel işler | Kayıt formu → ödeme kontrolü → hoş geldin e-postası/WhatsApp, ders hatırlatma | Form, Stripe/iyzico, e-posta |
| **Her işletme** | Kimse raporlara bakmıyor | Günlük/haftalık özet raporu (satış, mesaj sayısı, yorumlar) WhatsApp'a | Sheets, AI, WhatsApp/Telegram |

## 7.2 Paketleme: tek sistem, üç paket

| Paket | İçerik | Kime |
|---|---|---|
| **Başlangıç** | 1 hazır otomasyon (örn. WhatsApp menü asistanı), kurulum + eğitim | Küçük esnaf |
| **Büyüme** | 2–3 otomasyon + AI yanıt + haftalık rapor | Düzenli müşteri trafiği olan işletmeler |
| **Özel** | İşletmeye özel süreç analizi ve özel workflow'lar | Orta ölçekli işletmeler, ajanslar |

## 7.3 Fiyatlandırma modeli

Önerilen yapı: **tek seferlik kurulum ücreti + aylık bakım/destek ücreti.**

- **Kurulum ücreti:** Analiz, kurulum, test ve eğitim emeği.
- **Aylık ücret:** Sunucu, izleme, güncelleme, küçük değişiklikler ve destek. Düzenli gelirin buradan gelir.
- **Kullanım maliyetleri** (WhatsApp mesaj ücretleri, AI API ücretleri) ya müşterinin kendi hesabından ödenir ya da faturaya ayrı kalem olarak eklenir. Pazarlıkta bunu baştan netleştir.

**Değere göre fiyat belirle, saate göre değil.** Basit bir hesap:

```
Kazandırılan zaman  = haftada X saat × 4 hafta
Aylık değer         = kazandırılan saat × o işi yapan kişinin saatlik maliyeti
                      + kaçırılmayan müşterilerden gelen ek gelir
Aylık ücretin       = bu değerin küçük bir kısmı  →  müşteri için kolay "evet"
```

Rakamları kendi şehrindeki piyasaya ve müşterinin büyüklüğüne göre belirle. İlk 2–3 müşteride düşük fiyat + referans izni almak, portföy oluşturmanın en hızlı yoludur.

## 7.4 Satış süreci

1. **Hedef seç:** Tek bir sektörle başla (örn. kuaförler). Aynı sistemi tekrar tekrar satmak, her seferinde yeni sistem kurmaktan çok daha kârlı.
2. **Demo hazırla:** Kendi test numaranla çalışan bir WhatsApp asistanı. İşletme sahibinin telefonundan mesaj atıp sonucu görmesi en güçlü satış argümanıdır.
3. **Ulaş:** Instagram DM, Google Maps'teki işletmeler, yüz yüze ziyaret. Mesajın kısa olsun: *"Mesajlarınıza 7/24 otomatik cevap veren bir sistem kuruyorum, 2 dakikalık demosunu göstereyim mi?"*
4. **Ücretsiz/indirimli pilot:** 1–2 haftalık deneme. Sonunda kaç mesajın otomatik yanıtlandığını raporla.
5. **Sözleşme:** Kapsam, ücret, destek süresi, veri işleme sorumlulukları (bkz. Bölüm 8).
6. **Teslim ve eğitim:** Kısa bir kullanım videosu kaydet. Destek taleplerin azalır.
7. **Referans iste:** Memnun müşteriden yorum ve tavsiye.

## 7.5 Teknik teslim: müşterinin sunucusu mu, seninki mi?

| Seçenek | Artı | Dikkat |
|---|---|---|
| **Müşterinin kendi sunucusu/n8n'i** | Veriler ve hesaplar müşteride; lisans açısından en temiz yol | Müşteri sunucu ücretini öder; erişim için yetki alman gerekir |
| **Senin sunucun** | Tek yerden yönetim, kolay bakım | Müşteri n8n arayüzüne **erişmemeli** ve workflow düzenleyememeli (n8n lisansı, Bölüm 8). Verilerin sorumluluğu sende. |

---
[← Hazır şablonlar](06-hazir-sablonlar.md) · [Sonraki: Güvenlik, lisans ve yasal notlar →](08-guvenlik-ve-yasal.md)
