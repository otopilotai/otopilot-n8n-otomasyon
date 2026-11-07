# 10 · KVKK uyumu: işletmelere otomasyon kurarken kendini koru

Bir işletmenin müşteri mesajlarını, randevularını veya iletişim bilgilerini işleyen bir sistem kurduğunda **kişisel veri** işlemiş olursun. Bu bölüm, 6698 sayılı Kişisel Verilerin Korunması Kanunu'na (KVKK) göre rolünü, yükümlülüklerini ve kendini korumak için hazırlaman gerekenleri adım adım anlatır.

> ⚠️ Bu bölüm bilgi amaçlıdır; hukuki danışmanlık değildir. Kurallar ve ceza tutarları değişebilir. İlk sözleşmeni imzalamadan önce bir **KVKK avukatına** göz attır. Resmi kaynak: [kvkk.gov.tr](https://www.kvkk.gov.tr)

## 10.1 Hangi veriler "kişisel veri"?

Bir kişiyi tanımlayan ya da tanımlanabilir kılan her bilgi: ad-soyad, telefon numarası, WhatsApp/Instagram kullanıcı adı, mesaj içeriği, randevu saati, adres, e-posta, IP adresi.

**Özel nitelikli kişisel veri** (daha sıkı kurallara tabidir): sağlık, biyometrik veri, din, etnik köken, siyasi görüş, cinsel hayat, ceza mahkûmiyeti gibi bilgiler.
👉 **Klinik, diş hekimi, psikolog, estetik merkezi** gibi işletmelerde randevu notları bile sağlık verisi içerebilir. Bu sektörlerde ekstra dikkatli ol (bkz. 10.8).

## 10.2 Rolünü bil: veri sorumlusu kim, veri işleyen kim?

| Rol | Kim? | Ne demek? |
|---|---|---|
| **Veri sorumlusu** | İşletme (kuaför, emlakçı, klinik…) | Verinin neden ve nasıl işleneceğine karar verir. Müşterilerine karşı asıl sorumlu odur. |
| **Veri işleyen** | Sen (otomasyonu kuran ve çalıştıran) | Veriyi işletme adına ve onun talimatıyla işlersin. |
| **Alt işleyenler** | Kullandığın servisler: AI sağlayıcısı (ör. Anthropic/Claude), sunucu (ör. Hetzner), mesajlaşma platformu (ör. Meta/WhatsApp) | Senin adına veriyi işleyen/barındıran üçüncü taraflar. |

**Aylık yönetim modelinde (Bölüm 9.4)** sistemi sen çalıştırdığın için rolün daha net: işletmenin verisini **senin sunucunda** ve **senin API hesaplarınla** işliyorsun. Bu da veri işleyen olarak sorumluluğunun arttığı anlamına gelir.

> Veri işleyen olarak, veri sorumlusuyla **birlikte** veri güvenliğinden sorumlusun (KVKK m.12). Yani "ben sadece kurdum" diyerek sorumluluktan kurtulamazsın.

## 10.3 İşletme (veri sorumlusu) neleri yapmalı? Sen ona hatırlat

Bunlar işletmenin yükümlülüğü ama sistemi sen kurduğun için ona yardımcı olman hem güven verir hem seni korur:

1. **Aydınlatma metni (KVKK m.10):** Müşteriler, mesajlarının otomatik bir sistem/yapay zekâ ile işlendiğini, amacını, kimlere aktarıldığını ve haklarını bilmeli. Örnek kısa bildirim (botun ilk mesajı veya profil/web sitesi):

   ```
   Bu hat, randevu ve bilgi taleplerinizi yanıtlamak için otomatik bir asistan
   kullanmaktadır. Mesajlarınız bu amaçla işlenir ve hizmet sağlayıcılarımızla
   (yurt dışındaki sunucu ve yapay zekâ servisleri dahil) paylaşılabilir.
   Ayrıntılı aydınlatma metni: [link]
   ```

2. **Hukuki sebep:** Randevu almak gibi müşterinin talebini yerine getirmek çoğu durumda "sözleşmenin kurulması/ifası" sebebine dayanır. **Pazarlama/kampanya** mesajları ise ayrı onay gerektirir (bkz. 10.9 İYS).
3. **VERBİS kaydı:** Küçük işletmelerin çoğu muaftır (bkz. 10.6), ama işletme kendi durumunu kontrol etmeli.
4. **Başvuru kanalı:** Müşteri "verimi silin" derse işletme 30 gün içinde cevap vermeli. Silme talebini sana iletebilmesi için süreci birlikte belirleyin.

## 10.4 Veri işleme sözleşmesi: seni en çok koruyan belge

Her işletmeyle, hizmet sözleşmesine ek olarak (veya içinde) yazılı bir **veri işleme sözleşmesi** yap. Olmazsa olmaz maddeler:

- **Konu ve amaç:** Hangi sistem, hangi veriler (ad, telefon, mesaj, randevu), hangi amaçla işlenecek.
- **Talimat ilkesi:** Veriyi yalnızca işletmenin talimatı ve sözleşme kapsamında işleyeceğin.
- **Alt işleyenler:** Kullandığın servislerin listesi (AI sağlayıcısı, sunucu, mesajlaşma platformu) ve bunların **yurt dışında** olduğu. Yeni bir servis eklemeden önce işletmeyi bilgilendireceğin.
- **Güvenlik tedbirleri:** 10.7'deki teknik ve idari tedbirler.
- **Gizlilik:** Verilere yalnızca senin (veya yazılı izinle belirlediğin kişilerin) erişeceği.
- **Saklama ve imha:** Verilerin ne kadar süre tutulacağı (ör. mesaj kayıtları 30/90 gün) ve sözleşme bitince **iade/silme**.
- **İhlal bildirimi:** Bir veri ihlali fark ettiğinde işletmeye **gecikmeksizin** (ör. 24 saat içinde) haber vereceğin.
- **Denetim ve işbirliği:** İlgili kişi başvurularında ve Kurul taleplerinde işletmeye destek olacağın.
- **Sorumluluğun sınırı:** İşletmenin talimatından veya kendi hatasından doğan sorunlarda sorumluluğun.

## 10.5 Yurt dışına veri aktarımı (2024'ten beri değişti)

Hetzner (Almanya/Finlandiya), Claude/Anthropic (ABD) ve Meta gibi servisler kullanıyorsan veriler **yurt dışına aktarılıyor** demektir. 1 Haziran 2024'te yürürlüğe giren değişiklikle KVKK m.9 şu yolları öngörür:

1. **Yeterlilik kararı** verilen ülkeye aktarım.
2. **Uygun güvenceler**, en pratiği Kurul'un yayımladığı **standart sözleşmeler**. Standart sözleşme imzalandıktan sonra **5 iş günü içinde Kurum'a bildirilmelidir**. Bildirim yükümlülüğü hem veri sorumlusu hem veri işleyen için geçerlidir; bildirim KEP ile ya da [Standart Sözleşme Bildirim Modülü](https://standartsozlesme.kvkk.gov.tr) üzerinden yapılabilir.
3. **Arızi (tekil, sürekli olmayan) aktarımlar** için istisnalar (ör. açık rıza). Bunlar **düzenli bir otomasyon sistemi için uygun değildir**, çünkü her mesajın yurt dışına gittiği bir sistem "arızi" sayılmaz.

**Pratikte ne yapmalısın?**
- İşletmeye, sistemin yurt dışı servisler kullandığını **yazılı** olarak bildir (sözleşmede alt işleyen listesi).
- AI'a **gereğinden fazla kişisel veri gönderme**. Ör. randevu için AI'ın müşterinin tam adına ve telefonuna ihtiyacı yoksa bunları göndermeden önce maskele veya çıkar (n8n'de bir "Set/Code" düğümüyle).
- Mümkünse **AB'de barındırma** (ör. Hetzner Almanya/Finlandiya lokasyonu) ve servislerin veri işleme koşullarını (DPA) incele.
- Standart sözleşme gerekip gerekmediğini ve nasıl uygulanacağını, ilk büyük müşterinden önce bir avukatla netleştir.

Kaynak: [KVKK · Standart Sözleşme Bildirim Modülü duyurusu](https://www.kvkk.gov.tr/Icerik/8043/Standart-Sozlesme-Bildirim-Modulu-Hakkinda-Kamuoyu-Duyurusu) · [KVKK · Standart sözleşmeler ve BCR dokümanları](https://www.kvkk.gov.tr/Icerik/7938/Standart-Sozlesmeler-ve-Baglayici-Sirket-Kurallarina-Iliskin-Dokumanlar-Hakkinda-Kamuoyu-Duyurusu)

## 10.6 VERBİS kaydı

VERBİS, veri sorumlularının kayıt olduğu sicildir. 1 Ekim 2025'te yürürlüğe giren Kurul kararına göre:

- **Yıllık çalışan sayısı 50'den az ve yıllık mali bilanço toplamı 100 milyon TL'den az** olan, ana faaliyeti özel nitelikli veri işlemek olmayan veri sorumluları kayıttan **muaftır**.
- Ana faaliyeti **özel nitelikli veri işlemek** olanlar (ör. klinik, laboratuvar) için eşik çok daha düşüktür: **10'dan az çalışan ve 10 milyon TL'den az bilanço**.
- Muafiyet yalnızca **kayıt** yükümlülüğünü kaldırır; aydınlatma, güvenlik ve başvurulara cevap verme yükümlülükleri devam eder.

Bu yükümlülük **veri sorumlusuna** (işletmeye) aittir. Veri işleyen olarak senin ayrıca VERBİS kaydı yapman gerekmez; ancak kendi şirketin için de veri sorumlusu olduğun durumlar (ör. kendi müşteri listen) olabilir.

Kaynak: [Erdem & Erdem · VERBİS istisna kriteri değişikliği](https://www.erdem-erdem.av.tr/bilgi-bankasi/verbis-kayit-yukumlulugune-iliskin-istisna-kriteri-degistirildi) · [KVKK kamuoyu duyurusu](https://kvkk.gov.tr/Icerik/8388/KAMUOYU-DUYURUSU)

## 10.7 Teknik ve idari güvenlik tedbirleri (n8n'de uygulanabilir)

**Teknik**
- **HTTPS zorunlu:** Caddy ile otomatik sertifika (Bölüm 3).
- **Kimlik bilgileri:** İşletmenin token'larını sadece n8n'in şifreli **Credentials** bölümünde sakla; workflow içine, notlara, ekran görüntülerine yazma. `N8N_ENCRYPTION_KEY`'i yedekle ve gizli tut.
- **Müşteri başına ayrım:** Her işletmeye ayrı credential, mümkünse ayrı API anahtarı/projesi.
- **Saklama süresi:** n8n çalıştırma kayıtları (execution data) mesaj içeriklerini saklar. Otomatik temizlik aç:
  ```ini
  EXECUTIONS_DATA_PRUNE=true
  EXECUTIONS_DATA_MAX_AGE=336   # saat (14 gün), ihtiyacına göre ayarla
  ```
- **Erişim:** n8n'de 2FA, güçlü şifre; sunucuda SSH anahtarı, kapalı gereksiz portlar (Bölüm 8.6).
- **Veri minimizasyonu:** Sadece gerekli alanları işle; AI'a göndermeden önce gereksiz kişisel bilgileri çıkar.
- **Yedek:** Şifreli ve erişimi kısıtlı yedek; yedeklerin de saklama süresi olsun.

**İdari**
- Veri işleme sözleşmesi (10.4), alt işleyen listesi, saklama-imha tablosu.
- Erişimi olan kişilerin listesi; ekip üyesi varsa gizlilik taahhüdü.
- Yılda en az bir kez kontrol listesini (10.11) gözden geçir.

## 10.8 Riskli sektörler: sağlık ve benzerleri

Klinik, diş hekimi, estetik, psikolog, eczane, laboratuvar gibi işletmelerde mesajlar **sağlık verisi** içerebilir (şikâyet, tedavi, ilaç).
- Botu, sağlık bilgisi **istemeyecek** şekilde tasarla (ör. "Şikâyetinizi yazmayın, sadece uygun saati seçin").
- Sağlık verisini AI servisine göndermekten kaçın; kaçınılmazsa önce avukatla görüş.
- Bu sektörlerde VERBİS eşiği daha düşüktür (10.6); işletmeyi uyar.

## 10.9 Ticari mesajlar ve İYS

- Müşterinin başlattığı konuşmaya cevap vermek (randevu, bilgi) **hizmet iletisidir**.
- Kampanya, indirim, duyuru gibi **ticari elektronik ileti** göndermek için alıcının önceden onayı gerekir ve onaylar **İYS** üzerinden yönetilir (6563 sayılı Kanun).
- Bot üzerinden toplu pazarlama mesajı göndereceksen işletmenin İYS kaydı ve alıcı onayları hazır olmalı.

Kaynak: [İYS](https://iys.org.tr)

## 10.10 Veri ihlali olursa ne yapacaksın?

Örnek: sunucuya yetkisiz erişim, sızan API anahtarı, yanlış kişiye giden mesajlar.

1. **Durdur:** İlgili anahtarları iptal et/yenile, workflow'u kapat, erişimi kes.
2. **Kaydet:** Ne oldu, ne zaman, hangi veriler, kaç kişi etkilendi; not al.
3. **İşletmeye hemen bildir:** Sözleşmedeki süre içinde (ör. 24 saat).
4. **Kurul'a bildirim:** Veri sorumlusu (işletme), ihlali öğrendikten sonra **en kısa sürede ve en geç 72 saat içinde** Kurul'a bildirmeli; gerekirse etkilenen kişilere de haber vermeli. Sen bu bildirim için gereken bilgileri sağla.
5. **Düzelt ve önle:** Kök nedeni gider, tedbirleri güncelle.

## 10.11 Kontrol listesi: her yeni müşteride

- [ ] Hizmet sözleşmesi + **veri işleme sözleşmesi** imzalandı
- [ ] Alt işleyenler (AI, sunucu, mesajlaşma) ve yurt dışı aktarım yazılı bildirildi
- [ ] İşletmenin aydınlatma metni/bot karşılama bildirimi hazır
- [ ] Sektör özel nitelikli veri içeriyor mu? (sağlık vb.) → ek önlem
- [ ] Müşteriye ayrı credential/API anahtarı, harcama limiti
- [ ] n8n çalıştırma kayıtları için otomatik temizlik açık
- [ ] AI'a gönderilen veriler minimuma indirildi
- [ ] Silme/erişim taleplerinin nasıl iletileceği belirlendi
- [ ] İhlal durumunda kimin kime haber vereceği yazılı
- [ ] Sözleşme bitince veri iade/silme ve erişim iptali planlandı

## 10.12 Cezalar hakkında

KVKK ihlallerinde (aydınlatma yükümlülüğü, veri güvenliği, Kurul kararlarına uymama, VERBİS, standart sözleşme bildirimi vb.) **idari para cezaları** uygulanır. Tutarlar her yıl yeniden değerlendirme oranıyla güncellenir; güncel tutarları [kvkk.gov.tr](https://www.kvkk.gov.tr) üzerinden kontrol et. Küçük bir işletme için bile bu cezalar, aldığın kurulum ücretinin çok üzerinde olabilir. Bu yüzden bu bölümdeki adımlar "bürokrasi" değil, **senin sigortan**.

---
[← Fiyatlandırma şablonu](09-fiyatlandirma-sablonu.md) · [Ana sayfa](../README.md)
