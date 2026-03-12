import pandas as pd

DOSYA_ADI = r"C:\Users\osman\Desktop\visual\mega_hizmet_verisi_5000.csv"
df = pd.read_csv(DOSYA_ADI, encoding='utf-8-sig')

# CSV’deki tüm sütun isimlerini gör
print(df.columns.tolist())