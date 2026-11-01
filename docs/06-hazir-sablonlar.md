# 6 · Hazır şablon kaynakları

Her workflow'u sıfırdan kurmana gerek yok. Binlerce hazır şablonu içe aktarıp işletmeye göre uyarlayabilirsin.

## Kaynaklar

| Kaynak | Ne var | Link |
|---|---|---|
| **n8n resmi şablon galerisi** | Topluluk ve n8n ekibinin binlerce şablonu; kategori, uygulama ve "AI" filtresiyle arama | [n8n.io/workflows](https://n8n.io/workflows/) |
| **n8n topluluk forumu** | Paylaşılan workflow'lar, sorun çözümleri, örnek kurulumlar | [community.n8n.io](https://community.n8n.io) |
| **Zie619/n8n-workflows** | GitHub'da kategorilere ayrılmış, binlerce workflow içeren büyük bir arşiv | [github.com/Zie619/n8n-workflows](https://github.com/Zie619/n8n-workflows) |
| **enescingoz/awesome-n8n-templates** | Kullanım alanına göre düzenlenmiş seçkin şablon listesi | [github.com/enescingoz/awesome-n8n-templates](https://github.com/enescingoz/awesome-n8n-templates) |
| **n8n self-hosted AI starter kit** | n8n + yerel AI modelleri için resmi başlangıç paketi | [github.com/n8n-io/self-hosted-ai-starter-kit](https://github.com/n8n-io/self-hosted-ai-starter-kit) |
| **n8n kursları** | Başlangıç ve ileri seviye resmi eğitimler | [docs.n8n.io](https://docs.n8n.io) → Courses |

## Şablon nasıl içe aktarılır?

**n8n.io galerisinden:** Şablon sayfasında **Use for free → Copy template to clipboard** → kendi n8n'inde boş bir tuvale `Ctrl+V` / `Cmd+V`.

**JSON dosyasından:** n8n → sağ üst **⋯ → Import from File** → `.json` dosyasını seç.

**URL'den:** **⋯ → Import from URL** → ham (raw) JSON adresini yapıştır.

## İçe aktardıktan sonra kontrol listesi

- [ ] Her düğümde kendi **kimlik bilgini** seç (şablonlar kimlik bilgisi içermez).
- [ ] Sabit değerleri (tablo ID'leri, e-posta adresleri, kanal adları) kendi değerlerinle değiştir.
- [ ] **Community node** (topluluk düğümü) kullanılıyorsa kur: Settings → Community nodes. Kurmadan önce düğümün güvenilirliğini kontrol et.
- [ ] Önce **elle test et**, sonra aktifleştir.
- [ ] Topluluk şablonlarındaki kodları (Code düğümleri, HTTP istekleri) çalıştırmadan önce oku. Bilinmeyen bir adrese veri gönderen şablonları kullanma.

## Başlamak için iyi şablon türleri

| Arama terimi (n8n.io/workflows) | Neden iyi bir başlangıç |
|---|---|
| `whatsapp` | İşletmelerin en çok istediği kanal |
| `ai agent` | AI'ın araç kullandığı örnek kurulumlar |
| `google sheets` | Neredeyse her otomasyonun veri ayağı |
| `lead` / `crm` | Satış ekipleri için hazır akışlar |
| `invoice` / `ocr` | Muhasebe ve ofis işleri |
| `social media` / `content` | İçerik üretimi ve planlı paylaşım |

---
[← WhatsApp asistanı](05-whatsapp-asistani.md) · [Sonraki: İşletmelere ne satabilirsin? →](07-isletmelere-satis.md)
