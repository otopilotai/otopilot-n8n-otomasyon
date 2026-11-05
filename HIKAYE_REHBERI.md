# Otopilot AI — günlük hikâye üretim rehberi

Hesap: @otopilot.ai (Instagram, Windsor.ai connector `instagram`, account 17841472173509916)
Seri: "30 günde 10.000$ challenge". Para birimi her zaman dolar. Kasa: -28$ (Claude 20$ + Hetzner 8$) — artıya geçince güncel değer Reels açıklamasından okunur.
Kurallar: satış/reklam yok, işletme isimleri paylaşılmaz, her şey ücretsiz öğretilir. Rakamlar uydurulmaz (yalnızca açıklamalarda geçen gerçek rakamlar).
Marka: siyah zemin, neon pembe / sarı / nane; Inter fontları; emoji KULLANMA (PIL'de kutu olarak çıkar). ✓ ve → kullanılabilir.

## Günde 2 hikâye
1. **Sabah (etkileşim)** — `question` beat'i ile başlayan anket/soru/quiz hikâyesi. Soru, kullanıcı anket veya soru çıkartmasını alttaki boş alana eklesin diye bırakılır. Konu: o haftanın Reels konusu, otomasyon, AI araçları, para kazanma.
2. **Akşam (Reels'e çekim)** — bugünün/son Reels'in merakını uyandıran teaser + "BU AKŞAM 20:00" veya "YENİ VİDEO YAYINDA" + yorum kelimesi hatırlatması.

## Büyüme planı (Gün 9–30) — yorum kelimesi → ManyChat DM
9 Kasa artıya geçti (KASA) · 10 Kuaföre ne sattım (DEMO) · 11 Yorumlara meslek yaz · 12 Yorum yanıtı (DEMO) · 13 ChatGPT mi Claude mu ·
14 Haftalık kasa (KASA) · 15 İlk müşterim reddetti (SATIS) · 16 n8n/Zapier/Make maliyet (TABLO) · 17 DM'lerime AI cevap veriyor (TEST) ·
18 Yorum yanıtı · 19 En çok sorulan 3 soru (SATIS) · 20 100 takipçi çekilişi · 21 Haftalık kasa · 22 YouTube otomasyonu (YOUTUBE) ·
23 İlk AI hikâye videosu · 24 Parayı neye harcayayım (oylama) · 25 Seçimi uyguluyorum · 26 Yorum yanıtı · 27 En pahalı 3 hata (SATIS) ·
28 Haftalık kasa · 29 30 günlük yol haritası (YOL) · 30 Final + 2. sezon (SEZON2)

## Motor
`python3 hikaye.py spec.json preview out.png` · `python3 hikaye.py spec.json render out.mp4` (çalışma klasöründe av_*.png olmalı).
Beat tipleri: hook{big,sub} · big{lines:[{t,color,size}]} · card{icon,l1,l2,rot} · question{lines,hint} · cta{icon,big,pill}.
Ortak alanlar: d (sn), color (pembe|sari|nane|kirmizi), pose (rest|open|point|pointL|wave|shock|c1|c2|c3|whisper).
İkonlar: film eq pad robot shop chart check question money plane. Toplam 10–15 sn hedefle. Hikâye üst/alt 250px güvenli alanına yazı koyma.
`ornek.json` örnek bir sabah hikâyesidir.
