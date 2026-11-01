# 2 · Hetzner'den sunucu kiralama

Bu bölümün sonunda internette 7/24 çalışan, sadece senin erişebildiğin bir Ubuntu sunucun olacak.

## 2.1 Hesap aç

1. [accounts.hetzner.com](https://accounts.hetzner.com) adresinden **Sign up** ile e-posta ve şifre belirleyerek kayıt ol.
2. E-postandaki doğrulama bağlantısına tıkla.
3. Kişisel bilgilerini ve ödeme yöntemini ekle.

> ⚠️ **Kimlik doğrulaması ve 2FA:** Hetzner yeni hesaplarda kimlik doğrulaması ve iki adımlı doğrulama (2FA) isteyebilir. Kimliğini hazır tut ve telefonuna bir doğrulama uygulaması (Google Authenticator, Microsoft Authenticator, Authy vb.) kur. Onay süreci zaman alabildiği için hesabı sunucuya ihtiyaç duymadan **bir gün önce** açmanı öneririz.

## 2.2 SSH anahtarı oluştur (önerilir)

Şifre yerine SSH anahtarıyla bağlanmak hem daha güvenli hem daha pratiktir.

**Mac / Linux / Windows 10+ (PowerShell):**
```bash
ssh-keygen -t ed25519 -C "otopilot-sunucu"
# Enter'a basarak varsayılan konuma kaydet, istersen bir parola belirle
cat ~/.ssh/id_ed25519.pub        # Windows: type $env:USERPROFILE\.ssh\id_ed25519.pub
```
Çıkan `ssh-ed25519 AAAA...` ile başlayan satırı kopyala. Sunucu oluştururken Hetzner'e ekleyeceksin.

> 💡 Takılırsan Claude'a şunu yaz: *"Windows'ta SSH anahtarı oluşturup Hetzner'e eklemek istiyorum, adım adım anlat."*

## 2.3 Proje ve sunucu oluştur

1. [console.hetzner.com](https://console.hetzner.com) → **+ New project** → örn. `N8N OTOMASYON`
2. Projeye gir → **Create server** (Sunucu ekle)
3. Seçimler:

| Ayar | Önerimiz | Neden |
|---|---|---|
| **Location (konum)** | Almanya (Nuremberg / Falkenstein) veya Helsinki | Türkiye'ye yakın, düşük gecikme |
| **Image** | **Apps → Docker CE** (veya OS Images → Ubuntu) | Docker CE imajı Docker'ı hazır kurulu getirir |
| **Type** | En küçük paylaşımlı vCPU sunucu | Temel n8n kullanımı için yeterli |
| **Networking** | IPv4 + IPv6 | Webhook'lar için genel IPv4 gerekir |
| **SSH keys** | 2.2'de oluşturduğun anahtar | Güvenli giriş |
| **Backups** | İsteğe bağlı (ücretli) | Otomatik günlük yedek |
| **Name** | `n8n-sunucu` | — |

> n8n'in resmi Hetzner rehberi temel kullanım için küçük bir sunucunun yeterli olduğunu, n8n'in yapay zekâ asistanı (n8n Assistant) özelliğini kullanacaksan **en az 2 vCPU / 4 GB RAM** seçmeni önerir. Kaynak: [n8n · Deploy to Hetzner](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-hetzner)

4. Sağ alttaki toplam fiyatı kontrol et (bizim seçimimizde **8,09$/ay, KDV hariç**) → **Create & Buy now**.
5. Birkaç saniye sonra sunucu **Running** durumuna geçer. Sunucunun **IPv4 adresini** not al.

## 2.4 Sunucuya bağlan

```bash
ssh root@SUNUCU_IP_ADRESI
```
İlk bağlantıda "Are you sure you want to continue connecting?" sorusuna `yes` yaz.

İlk iş sistemi güncelle:
```bash
apt update && apt upgrade -y
```

## 2.5 Güvenlik duvarı

İki seçenekten birini kullan:

**A) Hetzner Cloud Firewall (önerilir, konsoldan):** Projede **Firewalls → Create Firewall** → gelen (inbound) kurallar: `TCP 22` (SSH), `TCP 80` (HTTP), `TCP 443` (HTTPS) → sunucuya uygula.

**B) Sunucu üzerinde ufw:**
```bash
ufw allow OpenSSH
ufw allow 80/tcp
ufw allow 443/tcp
ufw enable
```

> n8n'in 5678 portunu dışarı **açma**. Dış dünyaya sadece Caddy (80/443) açık olacak; n8n ona arkadan bağlanacak.

---
[← Araçlar ve maliyet](01-araclar-ve-maliyet.md) · [Sonraki: Sunucuya n8n kurulumu →](03-n8n-kurulum.md)
