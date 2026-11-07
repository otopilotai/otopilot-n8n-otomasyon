# 8 · Güvenlik, lisans ve yasal notlar

> Bu bölüm genel bilgilendirme amaçlıdır, hukuki danışmanlık değildir. Ticari faaliyete başlamadan önce bir avukata/mali müşavire danışmanı öneririz.

## 8.1 n8n lisansı (Sustainable Use License)

n8n'in kendi sunucuna kurulan sürümü ücretsizdir ama açık kaynak değil, "fair-code" lisanslıdır. n8n'in resmi lisans SSS'sine göre:

| Durum | İzin |
|---|---|
| n8n'i kendi işini yürütmek için kullanmak | ✅ Serbest |
| Müşteriler için workflow kurmak, kurulum/bakım/eğitim/danışmanlık ücreti almak | ✅ Serbest (müşteri workflow oluşturup düzenleyemiyorsa) |
| Hazır workflow'ları arka planda çalıştırıp, müşterinin sadece sonuçlarını alması (webhook/API ile tetikleme) | ✅ Serbest |
| n8n'i müşterilere hizmet olarak barındırıp **onların workflow oluşturmasına** izin vermek | ❌ Yasak |
| n8n arayüzünü kendi ürününün içine gömüp son kullanıcılara workflow düzenletmek | ❌ Yasak |
| n8n markasını kaldırıp kendi ürünün gibi satmak (white-label) | ❌ Yasak |

Belirleyici olan şey **müşterinin n8n'e erişimi**; müşteri sayısı ya da gelir değil. Emin olmadığın durumlar için: license@n8n.io

Kaynak: [n8n · License FAQ](https://docs.n8n.io/n8n-community-license/community-license/license-faq)

## 8.2 KVKK (kişisel veriler)

WhatsApp mesajları, telefon numaraları, isimler ve randevu bilgileri **kişisel veridir**. Bir işletme adına bu verileri işlediğinde:

- İşletme genellikle **veri sorumlusu**, sen **veri işleyen** olursun. Aranızda veri işleme hükümleri içeren bir sözleşme olmalı.
- Müşterilere **aydınlatma metni** sunulmalı (örn. menü mesajında link).
- Veriler yalnızca gereken süre kadar saklanmalı; sunucu güvenliği (2FA, güncel yazılım, güçlü şifreler) senin sorumluluğundadır.
- **Sağlık verisi özel nitelikli kişisel veridir** (klinikler!). Teşhis, tedavi gibi bilgileri otomasyonlarda işlemekten kaçın ya da bir hukukçuyla birlikte kurgula.
- Yurt dışındaki sunucuya (Almanya/Finlandiya) ve yurt dışı servislere (Meta, OpenAI) veri aktarımı KVKK'da ayrıca düzenlenmiştir; müşterine bu konuda danışmanlık aldırmasını öner.

Kaynak: [KVKK resmi sitesi](https://www.kvkk.gov.tr)

## 8.3 Ticari mesajlar ve İYS

Kampanya, indirim, duyuru gibi **ticari elektronik iletiler** göndermek için Türkiye'de alıcının önceden onayı gerekir ve bu onaylar **İleti Yönetim Sistemi (İYS)** üzerinden yönetilir. Müşterinin yazdığı mesaja cevap vermek (hizmet mesajı) ile toplu kampanya mesajı göndermek farklı kurallara tabidir.

Kaynak: [İYS · İleti Yönetim Sistemi](https://iys.org.tr)

## 8.4 Platform kuralları (YouTube, Meta, diğerleri)

Otomasyonla bir platforma içerik yüklüyor veya mesaj gönderiyorsan o platformun kurallarına uymak zorundasın:

- **YouTube:** Otomatik/AI ile üretilen içerikte telif, yanıltıcı içerik ve "tekrarlayan/düşük emekli içerik" politikalarına dikkat et; gerçekçi AI içerikleri için açıklama (disclosure) seçeneğini kullan. Bkz. [YouTube Topluluk Kuralları](https://www.youtube.com/howyoutubeworks/policies/community-guidelines/)
- **WhatsApp / Instagram (Meta):** İşletmenin ilk mesajı için kişinin onayı ve onaylı şablon gerekir; izinsiz toplu mesaj numarayı/hesabı kısıtlatır. Bkz. [WhatsApp Business Policy](https://business.whatsapp.com/policy)
- **API kullanım şartları:** Her servisin API'sinin kota ve kullanım şartları vardır; kotayı aşmak veya şartları ihlal etmek erişimin kesilmesine yol açabilir.

## 8.5 Sosyal medyada paylaşım

- Bir markadan para, ürün veya affiliate (komisyon) geliri alıyorsan paylaşımda **#reklam / #işbirliği** ile belirtmen gerekir. Kaynak: [Ticaret Bakanlığı · Sosyal medya etkileyicileri kılavuzu](https://ticaret.gov.tr/haberler/ticaret-bakanligi-sosyal-medya-etkileyicileri-icin-kilavuz-yayimladi)
- Kazanç hedeflerini **garanti gibi** sunma.

## 8.6 Sunucu güvenliği kontrol listesi

- [ ] Hetzner ve n8n hesaplarında 2FA açık
- [ ] SSH ile şifre yerine anahtarla bağlanılıyor
- [ ] Güvenlik duvarında yalnızca 22, 80, 443 açık
- [ ] `.env` ve `N8N_ENCRYPTION_KEY` güvenli bir yerde yedekli, hiçbir yerde paylaşılmıyor
- [ ] n8n ve Ubuntu düzenli güncelleniyor
- [ ] Düzenli yedek alınıyor ve yedekten geri yükleme bir kez denendi
- [ ] Topluluk düğümleri ve şablonlardaki kodlar kullanılmadan önce incelendi
- [ ] API anahtarları müşteri başına ayrı ve gerektiğinde iptal edilebilir

---
[← İşletmelere ne satabilirsin?](07-isletmelere-satis.md) · [Ana sayfa](../README.md) · [Sonraki: Fiyatlandırma şablonu →](09-fiyatlandirma-sablonu.md)
