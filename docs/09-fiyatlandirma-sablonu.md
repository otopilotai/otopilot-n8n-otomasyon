# 9 · Fiyatlandırma şablonu

Bu bölüm, "30 günde 10.000$" serisinde işletmelere otomasyon satarken kullandığım fiyatlandırma mantığını anlatır. Kendi işine uyarla, kopyala, kullan.

> **Gerçek rakamlar (serinin 9. günü itibarıyla):** Emlakçıya katalog botu kurulumu **7.500 TL**, iki kuaföre otomatik randevu sistemi **6.000 TL + 6.000 TL**. Aylık yönetim modelinde örnek fatura: **1.000 TL API + 2.000 TL yönetim = 3.000 TL/ay** (vergiler hariç). Bu bölümdeki diğer aralıklar benim gerçekleşmiş satışım değil, **öneri** niteliğindedir. Kendi şehrine, sektörüne ve tecrübene göre ayarla.

## 9.1 Fiyatın 3 parçası

| Parça | Ne zaman alınır? | Neyi karşılar? |
|---|---|---|
| **Kurulum ücreti** | Tek sefer, iş başında | Analiz, workflow'u işletmeye uyarlama, test, teslim, kısa eğitim |
| **Aylık yönetim** *(opsiyonel)* | Her ay | API kullanımı (maliyetine) + sistemi çalıştırma, izleme, güncelleme, destek |
| **Ek iş** | Talep geldikçe | Yeni özellik, yeni kanal (ör. Instagram'a ek WhatsApp), raporlama |

Kural: **Kurulum bir kere kazandırır, aylık yönetim her ay kazandırır.** Mümkünse her kuruluma aylık yönetim öner (bkz. 9.4).

## 9.2 Şablon mantığı: aynı workflow'u tekrar sat

Asıl kazanç burada: Bir sistemi bir kez iyi kur, **boş şablonunu sakla**. Yeni müşteride sadece işletme bilgilerini (isim, saatler, hizmetler, fiyatlar, katalog) girersin.

- İlk kurulum: Saatler/günler sürer.
- Şablondan kurulum: Çok daha kısa sürer.
- **Fiyatı harcadığın saate göre değil, işletmeye kazandırdığı değere göre belirle.** Şablon sayesinde hızlandın diye fiyatı düşürme.

## 9.3 Örnek paketler

| Paket | İçerik | Kurulum | Aylık yönetim ücreti (öneri, API hariç) |
|---|---|---|---|
| **Randevu asistanı** *(gerçek: 6.000 TL)* | Mesajla randevu alma, takvim, onay ve hatırlatma | 5.000 – 8.000 TL | 1.500 – 2.500 TL |
| **Katalog / bilgi botu** *(gerçek: 7.500 TL)* | Müşteri sorusuna göre ürün, daire veya menü bilgisi ve katalog gönderme | 6.000 – 10.000 TL | 2.000 – 3.000 TL |
| **SSS + yönlendirme asistanı** | Sık sorulan sorular, fiyat listesi, adres ve saatler, insana devretme | 4.000 – 6.000 TL | 1.000 – 2.000 TL |
| **Müşteri bulma / raporlama** | Aday listesi, otomatik tablo, haftalık rapor | 7.500 – 12.000 TL | 2.000 – 3.500 TL |

Fiyatı yukarı çeken şeyler: Birden fazla kanal, ödeme veya CRM entegrasyonu, çok şubeli işletme, özel raporlar, hızlı teslim.
Fiyatı aşağı çeken şeyler: Hazır şablonun birebir uyması, tek kanal, işletmenin içeriği (fiyat listesi, katalog) hazır vermesi.

## 9.4 Aylık yönetim modeli (benim kullandığım)

Sistemi işletmeye "teslim edip bırakmak" yerine **ben çalıştırıyorum**:

- **Workflow benim:** Kendi n8n sunucumda, kendi şablonumla çalışır.
- **AI ve diğer API anahtarları benim:** Örneğin Claude kullanımı benim hesabımdan ödenir.
- **İşletme sadece erişim verir:** Kendi kanalına (ör. WhatsApp Business, Instagram, takvim) bağlanmam için gereken API izni ya da token'ı verir. n8n arayüzüne erişmez.
- **Her ay tek fatura:** O ay harcanan API tutarı **maliyetine** yansıtılır, üstüne sabit **yönetim ücreti** eklenir.

```
Aylık ödeme = O ayın API harcaması (maliyetine) + Sabit yönetim ücreti   (+ vergiler)
```

**Gerçek örnek:**

| Kalem | Tutar |
|---|---|
| API kullanımı (1 ay) | 1.000 TL |
| Sistem yönetimi | 2.000 TL |
| **İşletmenin ödemesi** | **3.000 TL / ay** (vergiler hariç) |

**Neden bu model?**
- İşletme teknik hiçbir şeyle uğraşmaz; sen düzenli aylık gelir elde edersin.
- API maliyeti şeffaf olduğu için fiyat tartışması azalır: "Kullandığın kadar + yönetim".
- Aynı sunucuda birden fazla işletme çalışır; her yeni müşteri sunucu maliyetini paylaşır.

**İşletmeye "ortalama fiyat" vermek:** API harcaması aydan aya değişir. Teklifte geçmiş kullanımdan bir **ortalama** ver (ör. "ortalama 3.000 TL/ay, kullanıma göre ±"), ya da ilk ayı ölçüp ikinci aydan itibaren sabit paket fiyatına geç.

**Kendini korumak için:**
- AI sağlayıcında **aylık harcama limiti** koy; müşteri başına ayrı API anahtarı ya da ayrı proje kullan ki kullanımı ayrı ölçebilesin.
- Her ay kısa bir **kullanım raporu** gönder (mesaj sayısı, API tutarı).
- Sözleşmede yaz: Ücrete neler dahil (ör. ayda 2 küçük değişiklik), ödeme günü, iptal süresi, ayrılırsa ne olacağı (erişim iptal edilir; workflow sende kalır, işletmenin verisi ona iade edilir/silinir).
- İşletmenin verdiği token'ları n8n'in şifreli kimlik bilgilerinde sakla, kimseyle paylaşma. Müşteri verisini işlediğin için KVKK kapsamında **veri işleyen** sayılabilirsin; aranızda yazılı bir veri işleme sözleşmesi yap (ayrıntılar [Bölüm 10](10-kvkk-uyumu.md)).

**Aylık fatura/özet mesajı (kopyala-yapıştır):**

```
Merhaba [İşletme adı], [Ay] özeti:

📊 Asistanınız bu ay [N] mesajı yanıtladı, [M] randevu/talep oluşturdu.
💳 API kullanımı: [X] TL
🛠 Sistem yönetimi: [Y] TL
= Toplam: [X+Y] TL (+ KDV)

Ödeme son günü: [tarih]. Teşekkürler!
```

## 9.5 Teklif mesajı (kopyala-yapıştır)

```
Merhaba [İşletme adı],

Görüştüğümüz [randevu / katalog / SSS] asistanının teklifi:

✅ Kurulum (tek sefer): [X] TL
   - İşletmenize özel ayarlama, test ve teslim
   - Kısa kullanım eğitimi
✅ Aylık yönetim (opsiyonel): API kullanımı (maliyetine) + [Y] TL / ay
   - Sistemi ben çalıştırırım: sunucu, izleme, güncelleme, destek
   - Ortalama aylık toplam: ~[Z] TL

⏱ Teslim süresi: [N] iş günü
💳 Ödeme: %50 başta, %50 teslimde

Onaylarsanız [gün] başlayabiliriz.
```

## 9.6 Sık gelen itirazlar

| İtiraz | Cevap |
|---|---|
| "Pahalı." | "Bu sistem ayda kaç mesajı sizin yerinize cevaplıyor? Bir çalışanın o mesajlara harcadığı süreyi düşünün." Gerekirse kapsamı küçült, fiyatı değil. |
| "Düşüneyim." | "Size 1 haftalık demo kurayım, kendi müşterilerinizle deneyin." |
| "Bozulursa ne olacak?" | "Aylık yönetim tam bunun için: sistemi ben çalıştırıyorum, sorun olursa ben düzeltiyorum." |
| "API ücreti neden ayrı?" | "Kullandığınız kadar ödüyorsunuz; az mesaj gelen ay faturanız da düşük olur. Her ay raporunu gönderiyorum." |
| "Başkası daha ucuza yapıyor." | Neyin dahil olduğunu kıyasla: test, eğitim, bakım, destek. |

## 9.7 Yasal ve vergi notu

- Aldığın ödemeler gelir sayılır. Ödeme almadan önce **fatura veya serbest meslek makbuzu** düzenleyebilecek bir yapın olsun (ör. şahıs şirketi). Hangi yapının sana uygun olduğunu bir **mali müşavire** danış.
- Müşteri verisiyle çalışıyorsan [Bölüm 10 · KVKK uyumu](10-kvkk-uyumu.md)'ndaki adımları uygula.
- n8n lisansı gereği müşteriye n8n arayüzüne erişim verme ve n8n'i kendi markanmış gibi sunma (ayrıntılar Bölüm 8'de).

> Bu bölüm bilgi amaçlıdır; hukuki, mali veya vergi danışmanlığı değildir.

---
[← Güvenlik, lisans ve yasal notlar](08-guvenlik-ve-yasal.md) · [Ana sayfa](../README.md) · [Sonraki: KVKK uyumu →](10-kvkk-uyumu.md)
