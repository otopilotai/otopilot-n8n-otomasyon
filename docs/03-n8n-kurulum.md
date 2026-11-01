# 3 · Sunucuya n8n kurulumu

Bu bölümde n8n'i Docker ile kuracak ve önüne **Caddy** koyacağız. Caddy, alan adın için ücretsiz HTTPS sertifikasını (Let's Encrypt) otomatik alır ve yeniler.

```
İnternet ──443──▶ Caddy (HTTPS) ──▶ n8n:5678 (sadece içeriden)
```

Resmi kaynaklar: [n8n · Deploy to Hetzner](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-hetzner) · [n8n · Docker Compose](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/use-docker-compose) · [Caddy dokümantasyonu](https://caddyserver.com/docs/)

## 3.1 Alan adı (domain) ve DNS

WhatsApp gibi servisler webhook'ları yalnızca **HTTPS** adreslere gönderir; bu yüzden bir alan adına ihtiyacın var.

**Seçenek A — Kendi alan adın:** Herhangi bir kayıt firmasından alan adı al. DNS panelinde bir **A kaydı** ekle:

| Tür | Ad | Değer |
|---|---|---|
| A | `n8n` | `SUNUCU_IP_ADRESI` |

Sonuç: `n8n.alanadin.com`

**Seçenek B — Ücretsiz alt alan adı:** [DuckDNS](https://www.duckdns.org)'e gir, bir ad seç (örn. `otopilot`) ve IP'ni yaz. Sonuç: `otopilot.duckdns.org`

DNS'in yayıldığını kontrol et (birkaç dakika sürebilir):
```bash
ping n8n.alanadin.com     # sunucu IP'ni göstermeli
```

## 3.2 Docker'ı kontrol et / kur

Sunucuyu **Docker CE** imajıyla oluşturduysan Docker hazırdır:
```bash
docker --version && docker compose version
```

Ubuntu imajı seçtiysen Docker'ın resmi kurulum betiğiyle kur:
```bash
curl -fsSL https://get.docker.com | sh
```
Kaynak: [Docker · Ubuntu kurulumu](https://docs.docker.com/engine/install/ubuntu/)

## 3.3 Kurulum dosyalarını hazırla

Bu repodaki [`setup/`](../setup) klasörünü sunucuya al:
```bash
git clone https://github.com/sowyersalamanka-sys/otopilot-n8n-otomasyon.git
cd otopilot-n8n-otomasyon/setup
cp .env.example .env
```

Şifreleme anahtarı üret ve kopyala:
```bash
openssl rand -hex 32
```

`.env` dosyasını düzenle:
```bash
nano .env
```
```ini
N8N_HOST=n8n.alanadin.com          # 3.1'deki alan adın
GENERIC_TIMEZONE=Europe/Istanbul
N8N_ENCRYPTION_KEY=buraya_openssl_ciktisini_yapistir
```
Kaydet: `Ctrl+O`, `Enter`, çık: `Ctrl+X`.

> 🔐 **`N8N_ENCRYPTION_KEY`'i kaybetme.** n8n, kayıtlı kimlik bilgilerini (API anahtarları, tokenlar) bu anahtarla şifreler. Anahtar değişirse ya da kaybolursa kayıtlı kimlik bilgilerin açılamaz. Güvenli bir yere (şifre yöneticisine) kaydet.

## 3.4 Başlat

```bash
docker compose up -d
docker compose logs -f        # logları izle, Ctrl+C ile çık
```

1–2 dakika sonra tarayıcıda `https://n8n.alanadin.com` adresini aç. İlk açılışta **sahip (owner) hesabını** oluştur: e-posta, ad, güçlü bir şifre.

> Sertifika hatası görürsen: DNS kaydının doğru IP'yi gösterdiğinden ve 80/443 portlarının açık olduğundan emin ol, sonra `docker compose restart caddy`.

## 3.5 İlk güvenlik ayarları

- n8n'de **Settings → Personal → Two-factor authentication** ile 2FA'yı aç.
- Hetzner hesabında 2FA'nın açık olduğundan emin ol.
- `.env` dosyasını kimseyle paylaşma, GitHub'a yükleme (bu repodaki `.gitignore` onu zaten dışarıda bırakır).

## 3.6 Güncelleme

n8n sık güncellenir. Güncellemeden önce yedek al (3.7), sonra:
```bash
cd otopilot-n8n-otomasyon/setup
docker compose pull
docker compose up -d
docker image prune -f        # eski imajları temizle
```
Büyük sürüm geçişlerinde n8n.in sürüm notlarını ([docs.n8n.io](https://docs.n8n.io) → Release notes) oku.

## 3.7 Yedekleme

**Workflow'ları dışa aktar:**
```bash
docker compose exec n8n n8n export:workflow --all --output=/home/node/.n8n/yedek-workflows.json
docker compose cp n8n:/home/node/.n8n/yedek-workflows.json ./
```

**Tüm veriyi (veritabanı + ayarlar) yedekle:**
```bash
docker compose stop n8n
docker run --rm -v setup_n8n_data:/data -v "$PWD":/backup alpine \
  tar czf /backup/n8n-data-$(date +%F).tar.gz -C /data .
docker compose start n8n
```
> Volume adı klasör adına göre değişir; `docker volume ls` ile kontrol et.

Yedekleri sunucunun dışında da (bilgisayarın, bulut depolama) sakla. Hetzner'in ücretli otomatik **Backups** özelliği de ek bir güvence sağlar.

## Sorun giderme

| Belirti | Olası neden | Çözüm |
|---|---|---|
| Site açılmıyor | DNS yayılmadı / port kapalı | `ping` ile IP'yi kontrol et, güvenlik duvarına 80/443 ekle |
| "Bad gateway" | n8n henüz başlamadı | `docker compose logs n8n` |
| Webhook URL'leri `localhost` gösteriyor | `N8N_HOST` yanlış | `.env`'i düzelt, `docker compose up -d` |
| Kimlik bilgileri açılmıyor | Şifreleme anahtarı değişti | Eski `N8N_ENCRYPTION_KEY`'i geri yaz |

> 💡 Herhangi bir hata mesajını olduğu gibi Claude'a yapıştır: *"n8n'i Docker ile Hetzner'e kurdum, şu hatayı alıyorum: …"*

---
[← Hetzner'den sunucu kiralama](02-hetzner-sunucu.md) · [Sonraki: İlk workflow'unu oluştur →](04-ilk-workflow.md)
