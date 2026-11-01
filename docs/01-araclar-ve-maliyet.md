# 1 · Araçlar ve maliyet

Bu sistemi kurmak için üç temel araç yeterli. Kod bilmene gerek yok; teknik adımlarda Claude'dan yardım alacağız.

## Temel araçlar

| Araç | Ne işe yarıyor | Aylık maliyet* | Link |
|---|---|---|---|
| **Hetzner Cloud** | Sistemin 7/24 çalışacağı sunucu | ~7,49$ sunucu + 0,60$ IPv4 ≈ **8,09$** (KDV hariç) | [hetzner.com/cloud](https://www.hetzner.com/cloud) |
| **n8n Community Edition** | Uygulamaları ve AI modellerini birbirine bağlayan otomasyon platformu | **0$** (kendi sunucunda) | [n8n.io](https://n8n.io) · [Dokümantasyon](https://docs.n8n.io) |
| **Claude** | Kurulumda komut yazma, hata çözme, workflow tasarlama | Pro: ~20$ | [claude.ai](https://claude.ai) |
| **Alan adı (domain)** | n8n'e HTTPS ile erişmek ve webhook almak için | Yıllık birkaç dolar ya da ücretsiz alt alan adı | [DuckDNS (ücretsiz)](https://www.duckdns.org) |

\* Fiyatlar 31 Ekim 2026'da Hetzner konsolunda görülen değerlerdir. Hetzner euro ile faturalar; kur ve vergiye göre değişebilir.

## Kullanım başına ödenen araçlar (ihtiyaca göre)

| Araç | Ne için | Fiyatlandırma |
|---|---|---|
| [OpenAI API](https://platform.openai.com) / [Anthropic API](https://docs.claude.com) | Workflow içinde yapay zekâ (metin yazma, sınıflandırma, agent) | Kullandığın kadar (token başına) |
| [WhatsApp Cloud API (Meta)](https://developers.facebook.com/docs/whatsapp/cloud-api) | İşletme adına WhatsApp mesajı alma/gönderme | Mesaj başına; bkz. [Meta fiyatlandırma](https://developers.facebook.com/docs/whatsapp/pricing) |
| [Creatomate](https://creatomate.com) | Şablondan otomatik video üretimi | Render kredisi |
| [Buffer](https://buffer.com) | Sosyal medya planlı paylaşım | Ücretsiz plan + ücretli planlar |

> **WhatsApp için önemli:** Üçüncü taraf kaynaklara göre Meta, 1 Ekim 2026'dan itibaren müşteri hizmeti mesajlarını numara başına aylık 1.000 ücretsiz mesajla sınırladı; üstü ücretli. Güncel durumu mutlaka [Meta'nın resmi fiyat sayfasından](https://developers.facebook.com/docs/whatsapp/pricing) kontrol et.

## n8n Cloud mu, kendi sunucun mu?

| | n8n Cloud | Kendi sunucun (Hetzner) |
|---|---|---|
| Aylık maliyet | Starter ~20€, Pro ~50€ (yıllık ödemede) | ~8$ |
| Yıllık maliyet | ~240€ – 600€ | ~97$ |
| Çalıştırma (execution) limiti | Plana göre sınırlı | Sunucu kapasitesi kadar |
| Kurulum | Hazır | Bir kerelik (bu rehberle ~30–60 dk) |
| Bakım | n8n yapar | Sen yaparsın (güncelleme, yedek) |
| Verilerin | n8n'in sunucusunda | Senin sunucunda |

Kaynak: [n8n fiyatları](https://n8n.io/pricing/) (fiyatlar değişebilir).

**Ne zaman n8n Cloud?** Sunucuyla hiç uğraşmak istemiyorsan veya çok küçük denemeler yapacaksan. **Ne zaman kendi sunucun?** Maliyeti düşük tutmak, limitsiz çalıştırmak ve verileri kendi kontrolünde tutmak istiyorsan; bu rehber bu yolu anlatıyor.

---
[← Ana sayfa](../README.md) · [Sonraki: Hetzner'den sunucu kiralama →](02-hetzner-sunucu.md)
