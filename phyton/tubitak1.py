import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- 1. AYARLAR VE VERİ YÜKLEME ---
DOSYA_ADI = r"C:\Users\osman\Desktop\visual\mega_hizmet_verisi_5000.csv"  # Dosyanın tam yolu
sns.set_theme(style="whitegrid")  # Grafikleri güzelleştir
plt.rcParams['font.family'] = 'DejaVu Sans'  # Türkçe karakter sorunu olmasın

# --- 2. İSTİFA NEDENLERİ FONKSİYONU ---
def neden_bul(tweet):
    tweet = str(tweet).lower()
    
    # 1. Ekonomik (Yan haklar ve alım gücü eklendi)
    if any(k in tweet for k in ['maaş', 'ücret', 'zam', 'ekonomi', 'para', 'geçim', 'prim', 'ikramiye', 'sodexo', 'multinet', 'yan hak', 'alım gücü', 'enflasyon', 'borç']): 
        return 'Ekonomik'
    
    # 2. Yönetimsel (Liyakat ve iletişim eklendi)
    if any(k in tweet for k in ['mobbing', 'baskı', 'müdür', 'yönetici', 'huzursuz', 'aşırı kontrol', 'adaletsiz', 'otoriter', 'liyakat', 'torpil', 'vizyonsuz', 'iletişimsiz', 'patron', 'ceo', 'amir']): 
        return 'Yönetmsel'
    
    # 3. Çalışma Koşulları (Fiziksel şartlar eklendi)
    if any(k in tweet for k in ['nöbet', 'vardiya', 'mesai', 'yoğun', 'tempo', 'dinlenme', 'mola', 'hafta sonu', 'izin', 'ofis', 'ergonomi', 'yemekhane', 'servis']): 
        return 'Çalışma Koşulları'
    
    # 4. Psikolojik ve Sağlık (Tükenmişlik eklendi)
    if any(k in tweet for k in ['stres', 'yorgun', 'hastalık', 'depresyon', 'tükenmişlik', 'burnout', 'psikoloji', 'anksiyete', 'uykusuz', 'sağlık', 'bel fıtığı']): 
        return 'Sağlık / Yorgunluk'
    
    # 5. İş-Özel Yaşam Dengesi (Yeni Kategori)
    if any(k in tweet for k in ['denge', 'balance', 'aile', 'çocuk', 'vakit', 'kendime zaman', 'sosyal hayat', 'hobilerim']): 
        return 'İş-Yaşam Dengesi'
    
    # 6. Uzaktan Çalışma (Modern terimler eklendi)
    if any(k in tweet for k in ['uzaktan', 'remote', 'esnek', 'evden', 'home office', 'hybrid', 'hibrit', 'mekan bağımsız', 'ofise gitme']): 
        return 'Uzaktan Çalışma İsteği'
    
    # 7. Kariyer ve Gelişim (Eğitim eklendi)
    if any(k in tweet for k in ['kariyer', 'teklif', 'yeni iş', 'gelişim', 'fırsat', 'ilerleme', 'terfi', 'yükselme', 'promosyon', 'eğitim', 'kurs', 'sertifika', 'vizyon', 'öğrenme']): 
        return 'Kariyer Fırsatı'
    
    # 8. Kurumsal Kültür (Değerler eklendi)
    if any(k in tweet for k in ['kültür', 'etik', 'saygı', 'değer', 'takdir', 'motivasyon', 'aidiyet', 'kurumsallık', 'şirket politikası']): 
        return 'Kurumsal Kültür'
    
    # 9. İş Güvencesi ve Hukuk (İstifa/Tazminat eklendi)
    if any(k in tweet for k in ['güvence', 'sözleşme', 'fesih', 'tazminat', 'ihbar', 'sgk', 'sigorta',  'kod 29']): 
        return 'İş Güvencesi'
    
    # 10. Sosyal İlişkiler
    if any(k in tweet for k in ['arkadaş', 'ekip', 'takım', 'işyeri arkadaş', 'dedikodu', 'çatışma', 'gruplaşma', 'iş ortamı']): 
        return 'İş Arkadaşları / Takım'
    
    return 'Diğer/Belirsiz'
        
        
    

# --- 3. VERİYİ OKU VE İSTİFA NEDENLERİNİ HESAPLA ---
try:
    df = pd.read_csv(DOSYA_ADI, encoding='utf-8-sig')
    df['istifa_nedeni'] = df['Tweet'].apply(neden_bul)
except FileNotFoundError:
    print(f"🛑 HATA: '{DOSYA_ADI}' dosyası bulunamadı!")
    exit()

# --- 4. GRAFİK OLUŞTUR ---
plt.figure(figsize=(10,6))
sns.countplot(
    y=df['istifa_nedeni'], 
    order=df['istifa_nedeni'].value_counts().index,
    palette="viridis"
)
plt.title("İstifa Nedenleri (Tüm Tweetler)", fontsize=16, fontweight='bold')
plt.xlabel("Tweet Sayısı")
plt.ylabel("İstifa Nedeni")
plt.tight_layout()
plt.savefig('istifa_analiz_grafikleri.png', dpi=300)
print("\n✅ Grafik başarıyla oluşturuldu ve 'istifa_analiz_grafikleri.png' adıyla kaydedildi.")
plt.show()