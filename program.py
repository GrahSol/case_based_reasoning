import pandas as pd

# Fungsi keanggotaan
def trapesium_turun(x, a, b):
    if x <= a: return 1.0
    elif x >= b: return 0.0
    else: return (b - x) / (b - a)

def trapesium_naik(x, a, b):
    if x <= a: return 0.0
    elif x >= b: return 1.0
    else: return (x - a) / (b - a)

def segitiga(x, a, b, c):
    if x <= a or x >= c: return 0.0
    elif a < x <= b: return (x - a) / (b - a)
    elif b < x < c: return (c - x) / (c - b)
    return 0.0

# Fuzzification
def fuzzification(servis, harga):
    f_servis = {
        'Buruk': trapesium_turun(servis, 30, 50),
        'Biasa': segitiga(servis, 20, 50, 80),    
        'Bagus': trapesium_naik(servis, 50, 80)   
    }
    f_harga = {
        'Murah': trapesium_turun(harga, 22000, 30000),
        'Sedang': segitiga(harga, 28000, 40000, 50000),
        'Mahal': trapesium_naik(harga, 45000, 55000)
    }
    return f_servis, f_harga

# Inference
def inference(f_servis, f_harga):
    r1 = min(f_servis['Buruk'], f_harga['Mahal'])   
    r2 = min(f_servis['Buruk'], f_harga['Sedang'])  
    r3 = min(f_servis['Buruk'], f_harga['Murah'])   
    r4 = min(f_servis['Biasa'], f_harga['Mahal'])   
    r5 = min(f_servis['Biasa'], f_harga['Sedang'])  
    r6 = min(f_servis['Biasa'], f_harga['Murah'])   
    r7 = min(f_servis['Bagus'], f_harga['Mahal'])   
    r8 = min(f_servis['Bagus'], f_harga['Sedang'])  
    r9 = min(f_servis['Bagus'], f_harga['Murah'])   

    rendah = max(r1, r2, r3, r4)
    sedang = max(r5, r7)
    tinggi = max(r6, r8, r9)

    return {'Rendah': rendah, 'Sedang': sedang, 'Tinggi': tinggi}

# Defuzzification
def defuzzification(inf_result):
    pembilang = 0.0
    penyebut = 0.0
    for i in range(0, 1001):
        z = i / 10.0  
        
        mu_rendah = min(inf_result['Rendah'], trapesium_turun(z, 30, 50))
        mu_sedang = min(inf_result['Sedang'], segitiga(z, 40, 60, 80))
        mu_tinggi = min(inf_result['Tinggi'], trapesium_naik(z, 70, 90))
        
        mu_z = max(mu_rendah, mu_sedang, mu_tinggi)
        
        pembilang += z * mu_z
        penyebut += mu_z
    if penyebut == 0:
        return 0.0
        
    return pembilang / penyebut

# main
def main():
    try:
        print("Membaca file restoran.xlsx ...")
        df = pd.read_excel('restoran.xlsx')
        
        id_col = df.columns[0]
        servis_col = df.columns[1]
        harga_col = df.columns[2]
        
        results = []
        
        for index, row in df.iterrows():
            id_restoran = row[id_col]
            servis = row[servis_col]
            harga = row[harga_col]
            
            f_servis, f_harga = fuzzification(servis, harga)
            inf_result = inference(f_servis, f_harga)
            skor = round(defuzzification(inf_result), 5)
            
            results.append({
                'ID': id_restoran,
                'Kualitas Servis': servis,
                'Harga': harga,
                'Skor Kelayakan': skor
            })
            
        df_results = pd.DataFrame(results)
        df_sorted = df_results.sort_values(
            by=['Skor Kelayakan', 'Kualitas Servis', 'Harga'],
            ascending=[False, False, True]
        )
        
        df_top_5 = df_sorted.head(5)
        
        print("\nMenyimpan 5 restoran terbaik ke peringkat.xlsx ...")
        df_top_5.to_excel('peringkat.xlsx', index=False)
        
        print("\n===== DAFTAR 5 RESTORAN TERBAIK =====")
        print(df_top_5.to_string(index=False))
        print("\nProses Selesai dan hasil sudah diekstrak ke xlsx!")
        
    except FileNotFoundError:
        print("File 'restoran.xlsx' tidak ditemukan! Pastikan nama file sesuai dan berada pada satu folder dengan program ini.")

if __name__ == '__main__':
    main()