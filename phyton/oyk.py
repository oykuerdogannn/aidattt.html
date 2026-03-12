import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re

def istifa_ve_bunali_analizi():
    # 1. Veriyi Hazırla (Senin paylaştığın veriler üzerinden simülasyon)
    # Gerçek kullanımda: df = pd.read_csv("bunaldim_500_tweet.csv")
    df = pd.read_csv("bunaldim_500_tweet.csv")

    # 2. Analiz Kategorileri (Anahtar Kelime Grupları)
    kategoriler = {
        'Sosyal Medya / Kaos': ['kaos', 'site', 'tweet', 'sosyal medya', 'takip', 'viral', 'linç'],
        'İnsanlar / İlişkiler': ['insanlar', 'kız', 'kavga', 'yalnız', 'zorba', 'çenesi', 'ilgi', 'arkadaş'],
        'İş / Eğitim / Sorumluluk': ['ders', 'okul', 'iş', 'hazırlanmam', 'çalışamıyorum', 'krono', 'görev'],
        'Çevre / Mekan / Şehir': ['şehir', 'soğuk', 'evde', 'oda', 'mekan', 'köy', 'dışarı', 'yol'],
        'İçsel / Duygusal Tükenmişlik': ['tükendim', 'yalnızım', 'yoruldum', 'mutsuzum', 'sıkıldım', 'daraldım']
    }

    def kategori_ata(metin):# kullanıcının yazdığı şikayet alınır
        metin = str(metin).lower()# lowe tüm harfleri küçük harfe çevirir
        for kat, anahtarlar in kategoriler.items():
            if any(anahtar in metin for anahtar in anahtarlar):# anahtar kelimeler metnin içinde geçiyor mu
                return kat# eşleşme bulursa geri döndürür
        return 'Diğer / Genel Şikayet' # bulunmayan anahtar kelimelere diğer sütunu açar

    # Kategorize etme işlemini uygula
    df['Sebep_Kategorisi'] = df['Duygu_Metni'].apply(kategori_ata)

    # 3. Analiz Sonuçlarını Hesapla
    analiz_sonuclari = df['Sebep_Kategorisi'].value_counts()
    
    # 4. GRAFİKLEME (Görsel şölen değil, temiz analiz grafiği)
    plt.figure(figsize=(12, 6))
    sns.set_style("whitegrid") # Sade ve temiz görünüm
    
    # Sütun grafiği çiz
    ax = sns.barplot(x=analiz_sonuclari.index, y=analiz_sonuclari.values, palette="viridis")
    
    plt.title('Bunalma ve Ayrılma Nedenleri Analizi', fontsize=15, pad=20)
    plt.xlabel('Bunalma Kaynağı (Kategori)', fontsize=12)
    plt.ylabel('Tweet Sayısı / Frekans', fontsize=12)
    plt.xticks(rotation=45) # Yazıların birbirine girmemesi için

    # Sütunların üzerine sayıları yazdır
    for p in ax.patches:
        ax.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2., p.get_height()), 
                    ha = 'center', va = 'center', xytext = (0, 9), textcoords = 'offset points')

    plt.tight_layout()
    plt.show()

    # 5. Sayısal Raporu Terminale Bas
    print("\n--- ANALİZ RAPORU ---")
    print(analiz_sonuclari)
    print("---------------------")

if __name__ == "__main__":
    istifa_ve_bunali_analizi() # en üste def yazıldığı için program başlatıldığında analizi başlat 
