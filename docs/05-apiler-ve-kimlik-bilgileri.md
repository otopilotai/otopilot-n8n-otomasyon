# 5 · API'ler ve kimlik bilgileri

n8n'in gücü, farklı servisleri birbirine bağlamasından gelir. Bunun için her servise **API** üzerinden bağlanırsın. Bu bölümde API mantığını, n8n'e nasıl eklendiğini ve hazır bir workflow'u kendi API'lerinle nasıl dolduracağını öğreneceksin. Hangi otomasyonu kuracağına (YouTube, WhatsApp, e-posta, içerik üretimi…) sen karar verirsin; yöntem hep aynı.

## 5.1 API nedir? (30 saniyede)

**API**, bir uygulamanın başka bir uygulamayla konuşma kapısıdır. n8n bir servise "şunu yap" der (videoyu yükle, mesaj gönder, metin yaz), servis de cevap verir.

Kapıdan girmek için bir "anahtara" ihtiyacın var. n8n'de buna **kimlik bilgisi (credential)** denir. Üç yaygın türü vardır:

| Tür | Nasıl çalışır | Örnek servisler |
|---|---|---|
| **API anahtarı (API key)** | Servisin panelinden bir anahtar kopyalarsın, n8n'e yapıştırırsın | OpenAI, Anthropic, Creatomate |
| **Token** | Bir bot veya uygulama oluşturunca verilen uzun şifre | Telegram bot, Meta (WhatsApp/Instagram) |
| **OAuth2** | "Google ile giriş yap" gibi; hesabına izin verirsin, şifre paylaşılmaz | Google (YouTube, Sheets, Gmail, Drive), Microsoft, Buffer |

> 🔐 API anahtarları şifre gibidir: kimseyle paylaşma, ekran kaydında gösterme, GitHub'a yükleme. Sızdığını düşünürsen servisin panelinden hemen iptal edip yenisini oluştur.

## 5.2 n8n'e kimlik bilgisi ekleme (her servis için aynı)

1. n8n → **Overview → Credentials → Add credential** (veya bir düğümün içinde **Credential → Create new**)
2. Servisi ara ve seç (örn. "OpenAI", "YouTube OAuth2 API", "Telegram API")
3. İstenen alanları doldur:
   - **API anahtarı / token türü:** Anahtarı yapıştır → **Save**
   - **OAuth2 türü:** n8n'in gösterdiği **OAuth Redirect URL**'yi kopyala (`https://<alan-adin>/rest/oauth2-credential/callback` biçimindedir), servisin geliştirici panelinde bu adrese izin ver, oradan aldığın **Client ID** ve **Client Secret**'ı n8n'e yapıştır → **Sign in with …** → izin ver
4. Yeşil "Connection tested successfully" mesajını gör.

Kimlik bilgisini bir kez eklersin; sonra o servisi kullanan tüm workflow'larda listeden seçersin.

> Her servisin n8n'e nasıl bağlanacağını n8n dokümantasyonunda bulabilirsin: [docs.n8n.io](https://docs.n8n.io) → **Integrations** → servisin adı → **Credentials**. Burada adım adım ekran görüntüleri vardır.

## 5.3 En çok kullanılan API'ler (genel bakış)

| Servis | Ne için | Nereden alınır | Tür | Ücret |
|---|---|---|---|---|
| **OpenAI** (ChatGPT modelleri) | Metin, senaryo, sınıflandırma, AI agent | [platform.openai.com](https://platform.openai.com) → API keys | API anahtarı | Kullandıkça (bakiye yüklenir) |
| **Anthropic** (Claude modelleri) | Metin, analiz, AI agent | [console.anthropic.com](https://console.anthropic.com) → API Keys | API anahtarı | Kullandıkça |
| **Google** (YouTube, Sheets, Gmail, Drive, Calendar) | Video yükleme, tablo, e-posta, dosya, takvim | [Google Cloud Console](https://console.cloud.google.com) → proje → API'yi etkinleştir → OAuth istemcisi | OAuth2 | Çoğu ücretsiz; kota sınırları var |
| **Telegram** | Bot ile mesaj alma/gönderme, kendine bildirim | Telegram'da **@BotFather** → `/newbot` | Token | Ücretsiz |
| **Meta** (WhatsApp, Instagram, Facebook) | İşletme mesajlaşması, gönderi | [developers.facebook.com](https://developers.facebook.com) → uygulama oluştur | Token / OAuth2 | WhatsApp mesaj başına ücretli |
| **Creatomate** | Şablondan otomatik video üretimi | [creatomate.com](https://creatomate.com) → API | API anahtarı | Render kredisi |
| **ElevenLabs** | Metinden seslendirme | [elevenlabs.io](https://elevenlabs.io) → API keys | API anahtarı | Karakter başına / plan |
| **Buffer** | Sosyal medya planlı paylaşım | [buffer.com](https://buffer.com) | OAuth2 / token | Ücretsiz + ücretli planlar |
| **Notion / Airtable** | Veritabanı, içerik takvimi | Servisin entegrasyon ayarları | Token | Ücretsiz planlar var |
| **Her şey için: HTTP Request** | n8n'de hazır düğümü olmayan herhangi bir API | Servisin API dokümantasyonu | Hepsi | — |

> **Google API'leri için ipucu:** Tek bir Google Cloud projesinde YouTube Data API v3, Google Sheets API, Gmail API gibi ihtiyacın olanları etkinleştirip aynı OAuth istemcisini (Client ID/Secret) n8n'deki farklı Google kimlik bilgilerinde kullanabilirsin. Uygulama "test" modundayken kendi Google hesabını **Test users** listesine eklemeyi unutma. YouTube API'nin günlük kullanım kotası vardır; video yükleme kotayı hızlı tüketir.

## 5.4 Hazır bir workflow'u kendi API'lerinle doldurma

[Bölüm 6](06-hazir-sablonlar.md)'daki kaynaklardan bir şablon bulduğunda izleyeceğin yol:

1. **Şablonu içe aktar** (kopyala-yapıştır veya Import from File/URL).
2. **Gerekli servisleri listele:** Tuvalde kırmızı uyarı işareti olan düğümler kimlik bilgisi bekliyor. Şablon açıklamasında da genelde "Requirements" bölümü vardır.
3. **API'leri al:** 5.3'teki tablodan her servisin anahtarını veya OAuth istemcisini oluştur.
4. **Kimlik bilgilerini ekle** (5.2) ve her düğümde listeden seç.
5. **Sabit değerleri değiştir:** Kanal/klasör/tablo ID'leri, e-posta adresleri, prompt metinleri, dil ayarları. Bunlar genelde düğümlerin içinde örnek değer olarak durur.
6. **Adım adım test et:** Tetikleyiciyi elle çalıştır, her düğümün çıktısını incele; hata veren düğümde genelde ya kimlik bilgisi ya da bir alan adı eksiktir.
7. **Aktifleştir** ve ilk günlerde **Executions** sekmesinden takip et.

> 💡 Takıldığın düğümün hata mesajını ve şablonun adını Claude'a yapıştır: *"n8n'de şu şablonu kullanıyorum, YouTube düğümü şu hatayı veriyor, ne yapmalıyım?"*

## 5.5 Örnek otomasyon fikirleri ve gereken API'ler

Hangisini kuracağın tamamen senin hedefine bağlı. Her biri için n8n.io/workflows'ta arama yapıp hazır şablonlarla başlayabilirsin.

| Otomasyon | Akış (özet) | Gerekenler |
|---|---|---|
| **YouTube otomasyonu** | Konu listesi → AI senaryo → seslendirme → video render → YouTube'a yükleme | OpenAI/Anthropic, ElevenLabs, Creatomate, Google (YouTube) |
| **Tek mesajla sosyal medya videosu** | Telegram mesajı → AI senaryo → AI kurgu → render → planlı paylaşım | Telegram, OpenAI, Creatomate, Buffer |
| **WhatsApp müşteri asistanı** | Gelen mesaj → butonlu menü → seçime göre yanıt | Meta (WhatsApp Cloud API) |
| **E-posta asistanı** | Gelen e-postayı AI ile sınıflandır → taslak yanıt → etiketle | Google (Gmail), OpenAI/Anthropic |
| **İçerik takvimi** | Notion'daki fikirler → AI ile metin → zamanında paylaşım | Notion, OpenAI, Buffer |
| **Günlük rapor** | Tablodaki verileri oku → AI özet → Telegram'a gönder | Google (Sheets), OpenAI, Telegram |
| **Potansiyel müşteri (lead) toplama** | Web formu → tabloya yaz → otomatik karşılama e-postası | n8n Form, Google (Sheets, Gmail) |

## 5.6 Maliyeti kontrol altında tut

- AI API'lerinde **harcama limiti** belirle (OpenAI ve Anthropic panellerinde var).
- Testlerde küçük/ucuz modeller kullan, çalışınca gerekirse büyüt.
- Zamanlanmış workflow'ların ne sıklıkla çalıştığını kontrol et; dakikada bir çalışan bir AI düğümü faturayı hızla büyütür.
- Her müşteri veya proje için **ayrı API anahtarı** kullan; hem maliyeti ayrı takip edersin hem gerekirse tek anahtarı iptal edersin.

---
[← İlk workflow](04-ilk-workflow.md) · [Sonraki: Hazır şablon kaynakları →](06-hazir-sablonlar.md)
