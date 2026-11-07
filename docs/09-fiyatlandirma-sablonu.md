# 9 · Fiyatlandırma şablonu

Bu bölüm, "30 günde 10.000$" serisinde işletmelere otomasyon satarken kullandığım fiyatlandırma mantığını anlatır. Kendi işine uyarla, kopyala, kullan.

> **Gerçek rakamlar (serinin 9. günü itibarıyla):** Emlakçıya katalog botu kurulumu **7.500 TL**, iki kuaföre otomatik randevu sistemi **6.000 TL + 6.000 TL**. Bu bölümdeki diğer aralıklar benim gerçekleşmiş satışım değil, **öneri** niteliğindedir. Kendi şehrine, sektörüne ve tecrübene göre ayarla.

## 9.1 Fiyatın 3 parçası

| Parça | Ne zaman alınır? | Neyi karşılar? |
|---|---|---|
| **Kurulum ücreti** | Tek sefer, iş başında | Analiz, workflow'u işletmeye uyarlama, test, teslim, kısa eğitim |
| **Aylık bakım** *(opsiyonel)* | Her ay | Sunucu, izleme, küçük değişiklikler, hata düzeltme, destek |
| **Ek iş** | Talep geldikçe | Yeni özellik, yeni kanal (ör. Instagram'a ek WhatsApp), raporlama |

Kural: **Kurulum bir kere kazandırır, bakım her ay kazandırır.** Mümkünse her kuruluma bir bakım paketi öner.

## 9.2 Şablon mantığı: aynı workflow'u tekrar sat

Asıl kazanç burada: Bir sistemi bir kez iyi kur, **boş şablonunu sakla**. Yeni müşteride sadece işletme bilgilerini (isim, saatler, hizmetler, fiyatlar, katalog) girersin.

- İlk kurulum: Saatler/günler sürer.
- Şablondan kurulum: Çok daha kısa sürer.
- **Fiyatı harcadığın saate göre değil, işletmeye kazandırdığı değere göre belirle.** Şablon sayesinde hızlandın diye fiyatı düşürme.

## 9.3 Örnek paketler

| Paket | İçerik | Kurulum | Aylık bakım (öneri) |
|---|---|---|---|
| **Randevu asistanı** *(gerçek: 6.000 TL)* | Mesajla randevu alma, takvim, onay ve hatırlatma | 5.000 – 8.000 TL | 750 – 1.500 TL |
| **Katalog / bilgi botu** *(gerçek: 7.500 TL)* | Müşteri sorusuna göre ürün, daire veya menü bilgisi ve katalog gönderme | 6.000 – 10.000 TL | 1.000 – 2.000 TL |
| **SSS + yönlendirme asistanı** | Sık sorulan sorular, fiyat listesi, adres ve saatler, insana devretme | 4.000 – 6.000 TL | 500 – 1.000 TL |
| **Müşteri bulma / raporlama** | Aday listesi, otomatik tablo, haftalık rapor | 7.500 – 12.000 TL | 1.000 – 2.500 TL |

Fiyatı yukarı çeken şeyler: Birden fazla kanal, ödeme veya CRM entegrasyonu, çok şubeli işletme, özel raporlar, hızlı teslim.
Fiyatı aşağı çeken şeyler: Hazır şablonun birebir uyması, tek kanal, işletmenin içeriği (fiyat listesi, katalog) hazır vermesi.

## 9.4 Aylık bakımı hesapla

Önce kendi aylık maliyetini çıkar, sonra üstüne emeğini koy:

```
Aylık maliyet  = sunucu payı + API/kullanım ücretleri + varsa ek araçlar
Aylık bakım    = aylık maliyet + (ayda ayıracağın destek saati × saat ücretin)
```

- Tek bir sunucuda birden fazla müşterinin workflow'u çalışabilir; sunucu maliyetini müşterilere paylaştır.
- AI (ör. Claude) ve mesajlaşma API'leri **kullanıma göre** ücretlendirilir. Faturanı ilk ay takip et, bakım fiyatını gerçek kullanıma göre güncelle.
- Bakıma neyin dahil olduğunu **yazılı** belirt (ör. "ayda 2 küçük değişiklik"). Gerisi ek iş olsun.

## 9.5 Teklif mesajı (kopyala-yapıştır)

```
Merhaba [İşletme adı],

Görüştüğümüz [randevu / katalog / SSS] asistanının teklifi:

✅ Kurulum (tek sefer): [X] TL
   - İşletmenize özel ayarlama, test ve teslim
   - Kısa kullanım eğitimi
✅ Aylık bakım (opsiyonel): [Y] TL / ay
   - Sunucu ve izleme, küçük güncellemeler, destek

⏱ Teslim süresi: [N] iş günü
💳 Ödeme: %50 başta, %50 teslimde

Onaylarsanız [gün] başlayabiliriz.
```

## 9.6 Sık gelen itirazlar

| İtiraz | Cevap |
|---|---|
| "Pahalı." | "Bu sistem ayda kaç mesajı sizin yerinize cevaplıyor? Bir çalışanın o mesajlara harcadığı süreyi düşünün." Gerekirse kapsamı küçült, fiyatı değil. |
| "Düşüneyim." | "Size 1 haftalık demo kurayım, kendi müşterilerinizle deneyin." |
| "Bozulursa ne olacak?" | "Aylık bakım tam bunun için: izliyorum, sorun olursa ben düzeltiyorum." |
| "Başkası daha ucuza yapıyor." | Neyin dahil olduğunu kıyasla: test, eğitim, bakım, destek. |

## 9.7 Yasal ve vergi notu

- Aldığın ödemeler gelir sayılır. Ödeme almadan önce **fatura veya serbest meslek makbuzu** düzenleyebilecek bir yapın olsun (ör. şahıs şirketi). Hangi yapının sana uygun olduğunu bir **mali müşavire** danış.
- Müşteri verisiyle çalışıyorsan [Bölüm 8](08-guvenlik-ve-yasal.md)'deki KVKK ve İYS notlarına uy.
- n8n lisansı gereği müşteriye n8n arayüzüne erişim verme ve n8n'i kendi markanmış gibi sunma (ayrıntılar Bölüm 8'de).

> Bu bölüm bilgi amaçlıdır; hukuki, mali veya vergi danışmanlığı değildir.

---
[← Güvenlik, lisans ve yasal notlar](08-guvenlik-ve-yasal.md) · [Ana sayfa](../README.md)
