# Otopilot AI · 30 Günde Otomasyon Sistemi

> Sıfırdan, AI agent'larla işletmeleri ve günlük işleri otomatikleştiren bir sistem kurma rehberi.
> Kendi sunucunda n8n kur, workflow'ları oluştur, işletmelere sat.

Bu repo, Instagram'daki **"30 günde 10.000$ challenge"** serisinde kurduğumuz sistemin yazılı ve adım adım halidir. Her bölüm bir öncekinin üzerine kurulur. Sırayla ilerlersen sonunda elinde çalışan bir otomasyon altyapısı ve işletmelere sunabileceğin hazır bir hizmet olur.

---

## Ne kuruyoruz?

```
Müşteri / tetikleyici          Senin sunucun (Hetzner)                 Sonuç
─────────────────────          ─────────────────────────               ───────────────
WhatsApp mesajı   ──┐          ┌───────────────────────┐
Form / e-posta    ──┼────────▶ │  n8n  (workflow'lar)  │ ──▶  Otomatik yanıt, randevu,
Zamanlayıcı       ──┘          │  + AI modelleri       │      içerik, rapor, CRM kaydı…
                               └───────────────────────┘
                               Caddy (HTTPS) · Docker
```

- **Sunucu:** Hetzner Cloud'da aylık ~8$'lık küçük bir sunucu
- **Otomasyon:** n8n'in kendi sunucuna kurulan ücretsiz sürümü (Community Edition)
- **Yardımcı:** Kurulumun her adımında Claude
- **İlk ürün:** İşletmeler için 7/24 çalışan bir WhatsApp asistanı

## Bölümler

| # | Bölüm | Ne öğreneceksin |
|---|---|---|
| 1 | [Araçlar ve maliyet](docs/01-araclar-ve-maliyet.md) | Neye ihtiyacın var, aylık ne tutar, n8n Cloud ile karşılaştırma |
| 2 | [Hetzner'den sunucu kiralama](docs/02-hetzner-sunucu.md) | Hesap, doğrulama, SSH anahtarı, sunucu seçimi, güvenlik duvarı |
| 3 | [Sunucuya n8n kurulumu](docs/03-n8n-kurulum.md) | Alan adı, Docker, Caddy ile HTTPS, güncelleme, yedekleme |
| 4 | [İlk workflow'unu oluştur](docs/04-ilk-workflow.md) | Düğüm, tetikleyici, ifade (expression), test etme |
| 5 | [WhatsApp asistanı](docs/05-whatsapp-asistani.md) | Meta kurulumu, butonlu menü, "akış baştan başlıyor" sorununun çözümü |
| 6 | [Hazır şablon kaynakları](docs/06-hazir-sablonlar.md) | Binlerce hazır workflow'u nereden bulursun, nasıl içe aktarırsın |
| 7 | [İşletmelere ne satabilirsin?](docs/07-isletmelere-satis.md) | Sektör sektör fikirler, fiyatlandırma modeli, satış süreci |
| 8 | [Güvenlik, lisans ve yasal notlar](docs/08-guvenlik-ve-yasal.md) | n8n lisansı, KVKK, İYS, WhatsApp kuralları |

## Hazır dosyalar

| Dosya | Açıklama |
|---|---|
| [`setup/docker-compose.yml`](setup/docker-compose.yml) | n8n + Caddy (otomatik HTTPS) |
| [`setup/Caddyfile`](setup/Caddyfile) | Ters vekil (reverse proxy) ayarı |
| [`setup/.env.example`](setup/.env.example) | Doldurman gereken ayarlar |
| [`workflows/whatsapp-asistan.json`](workflows/whatsapp-asistan.json) | n8n'e içe aktarılabilir WhatsApp asistanı |

## Hızlı başlangıç (deneyimliler için)

```bash
# Ubuntu sunucuda, root olarak
git clone https://github.com/sowyersalamanka-sys/otopilot-n8n-otomasyon.git && cd otopilot-n8n-otomasyon/setup
cp .env.example .env && nano .env          # alan adını ve anahtarı yaz
docker compose up -d                        # birkaç dakika sonra https://<alan-adin> açılır
```

Ayrıntılar ve ön koşullar (alan adı, DNS, Docker) için [Bölüm 3](docs/03-n8n-kurulum.md)'e bak.

## Seri haritası

| Gün | Konu | Durum |
|---|---|---|
| 1 | Seriye giriş, plan ve kurallar | ✅ |
| 2 | Claude aboneliği (kasa -20$) | ✅ |
| 3 | Hetzner hesabı ve sunucu seçimi | ✅ |
| 4 | n8n nedir? WhatsApp asistanı workflow'u | ✅ |
| 5+ | Sunucuya n8n kurulumu, ilk agent'lar, ilk müşteri… | Devam ediyor |

Kasa durumu her videoda gerçek rakamlarla paylaşılıyor.

---

> **Not:** Bu repo kişisel bir deneyimin kaydıdır; kazanç garantisi veya yatırım tavsiyesi değildir. Bahsi geçen markalar (n8n, Hetzner, WhatsApp/Meta, Claude, Docker, Caddy vb.) ile iş birliğim yoktur; tüm marka adları sahiplerine aittir. Fiyatlar ve arayüzler zamanla değişebilir, her bölümde resmi kaynak linkleri verilmiştir.
