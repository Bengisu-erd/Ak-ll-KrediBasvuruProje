print("==================================================================")
print("                 KREDI BASVURU SISTEMINE HOSGELDINIZ")
print("==================================================================")
isim=input("Ad soy ad :").strip()
yas=int(input("Yasinizi girin:"))
aylik_gelir=float(input("Aylik gelirinizi girin:"))
aylik_kira=float(input("Aylik kira: "))
kredi_borcu=float(input("Aylik kredi odemesi:"))
kart_borcu=float(input("Aylik kredi karti odemesi:"))

print("Calisma durumunu giriniz")
print("1-Calisiyor")
print("2-Ogrenci")
print("3-Issiz")
print("4-Emekli") 

secim=(input("Calisma durumu:(1/2/3/4):"))
calisma_durumu_haritasi={
    "1":"Calisiyor",
    "2":"Ogrenci",
    "3":"Issiz",
    "4":"Emekli"
}
calisma_durumu=calisma_durumu_haritasi.get(secim,"Belirtilmemis")

calisma_suresi=0
if calisma_durumu=="Calisiyor":
    calisma_suresi=int(input("Mevcut isinizdeki calisma surenizi ay cinsinden giriniz: (orn:12 ay) "))

istenen_kredi_miktari=float(input("Talep edilen kredi miktari:"))


hatalar=[]
if yas<=0:
    hatalar.append("Yas bilgisi sifir veya negatif olamaz")
if aylik_gelir<=0:
    hatalar.append("Aylik gelir 0tl veya negatif olamaz.")
if aylik_kira <0:
    hatalar.append("Gider tutarlari negatif girilemez")
if istenen_kredi_miktari<=0:
    hatalar.append("Talep edilen kredi tutari 0 TL'den buyuk olmalidir.")

if hatalar:
    print("\n---GECERSIZ BASVURU---")
    for hata in hatalar:
        print(f"-{hata}")
    exit()

basvuru={
    "ad":isim,
    "yas":yas,
    "gelir":aylik_gelir,
    "kira":aylik_kira,
    "kredi_borcu":kredi_borcu,
    "kart_borcu":kart_borcu,
    "calisma_durumu":calisma_durumu,
    "calisma_suresi":calisma_suresi,
    "istenen_kredi":istenen_kredi_miktari
}
toplam_gider=basvuru["kira"]+basvuru["kredi_borcu"]+basvuru["kart_borcu"]
kullanabilir_gelir=basvuru["gelir"]-toplam_gider
borc_gelir_orani=(toplam_gider/basvuru["gelir"])*100

if yas<18:
    print("Basvuru yapilamaz.")
elif yas>=18 and yas<70:
    print("Degerlendirme devam ediyor")
else:
    print("Basvurunuz reddedildi.")

gelir_seviyesi=" "
if aylik_gelir<20000:
    gelir_seviyesi="Yetersiz gelir"
elif aylik_gelir>=20000 and aylik_gelir<35000:
    gelir_seviyesi="Dusuk gelir"
elif aylik_gelir>=35000 and aylik_gelir<70000:
    gelir_seviyesi="Orta gelir"
elif aylik_gelir>=70000:
    gelir_seviyesi="Yuksek gelir"

risk_seviyesi=""

if borc_gelir_orani<25:
    risk_seviyesi="Dusuk risk"
elif borc_gelir_orani>=25 and borc_gelir_orani<40:
    risk_seviyesi="Orta risk"
elif borc_gelir_orani>=40 and borc_gelir_orani<60:
    risk_seviyesi="Yuksek risk"
else:
    risk_seviyesi="Cok Yuksek Risk"

if basvuru["calisma_durumu"]=="Calisiyor":
    if basvuru["calisma_suresi"]<6:
        kidem_durumu="Riskli"
    elif basvuru["calisma_suresi"] <=12:
        kidem_durumu="Orta"
    elif basvuru["calisma_suresi"]<=36:
        kidem_durumu="İyi"
    else:
        kidem_durumu="Cok Iyi"
else:
    kidem_durumu="Uygulanamaz"

max_onerilen_kredi=basvuru["gelir"]*6

if basvuru["istenen_kredi"] <= max_onerilen_kredi:
    kredi_uygunlugu="Uygun"
elif basvuru["istenen_kredi"]<=max_onerilen_kredi*1.5:
    kredi_uygunlugu="Sinirda"
else:
    kredi_uygunlugu="Yuksek"

ret_nedenleri=[]
if basvuru["yas"]<18:
    ret_nedenleri.append("Yas kredi basvurusu icin uygun degil.")
if basvuru["yas"]>70:
    ret_nedenleri.append("Yas kredi basvurusu için uygun degil.")

if basvuru["gelir"]<20000:
    ret_nedenleri.append("Gelir yetersiz.Basvuru için uygun degil.")
if borc_gelir_orani>60:
    ret_nedenleri.append("Borc gelir orani cok yuksek.Basvuru için uyun degil.")
if basvuru["calisma_durumu"]=="Issiz":
    ret_nedenleri.append("Calisma durumu basvuru icin uygun degil.")
if basvuru["istenen_kredi"]>(max_onerilen_kredi*2):
    ret_nedenleri.append("Talep edilen kredi miktari cok yuksek.Basvuru icin uygun degil.")

if ret_nedenleri:
    sonuc="REDDEDILDI"
 
else:
    if basvuru["gelir"]>=35000 and borc_gelir_orani<25 and basvuru["calisma_durumu"]=="Calisiyor" and basvuru["calisma_suresi"]>12 and kredi_uygunlugu=="Uygun":
        sonuc= "ONAYLANDI"
    elif basvuru["gelir"]>=20000 and borc_gelir_orani<40 and basvuru["calisma_durumu"]=="Calisiyor" and basvuru["calisma_suresi"]>12 and kredi_uygunlugu in ["Uygun","Sinirda"]:
        sonuc= "ON ONAY"
    else: 
        sonuc="MANUEL INCELEME"

basvuru_puan=0

if basvuru["gelir"]>=50000:
    basvuru_puan+=30
if borc_gelir_orani<25:
    basvuru_puan+=30
if basvuru["calisma_durumu"]=="Calisiyor" and basvuru["calisma_suresi"]>36:
    basvuru_puan+=20
if basvuru["istenen_kredi"]<=max_onerilen_kredi:
    basvuru_puan+=20

if basvuru_puan>=80 and basvuru_puan<=100:
    puan_etiketi="Cok Iyi"
elif basvuru_puan>=60 and basvuru_puan<80:
    puan_etiketi="Iyi"
elif basvuru_puan>=40 and basvuru_puan<60:
    puan_etiketi="Orta"
else:
    puan_etiketi="Dusuk"

print("=============================================")
print("          KREDI ON DEGERLENDIRME             ")
print("=============================================")

print(f"Basvuru Sahibi: {basvuru['ad']}\n")
print(f"Yas: {basvuru['yas']}\n")
print(f"Calisma Durumu: {basvuru['calisma_durumu']}\n")
print(f"Calisma Suresi: {basvuru['calisma_suresi']} ay\n")


print("--------------------------------------------------\n")

print(f"Aylik Gelir: {basvuru['gelir']} TL\n")
print(f"Aylik Gider: {toplam_gider} TL\n")
print(f"Kullanabilir Gelir: {kullanabilir_gelir} TL\n")

print(f"Borc/Gelir Orani: %{borc_gelir_orani:.2f}\n")

print("--------------------------------------------------\n")

print(f"Talep Edilen Kredi Miktari: {basvuru['istenen_kredi']} TL\n")
print(f"Max Onerilen Kredi Miktari: {max_onerilen_kredi} TL\n")

print(f"Risk Seviyesi: {risk_seviyesi} ")
print(f"Basvuru Puani: {basvuru_puan} {puan_etiketi}\n")

print("--------------------------------------------------\n")


print(f"SONUC: {sonuc}\n")
print("=============================================")

if ret_nedenleri:
    print("RED NEDENLERI:")
    for neden in ret_nedenleri:
        print(f"- {neden}")




