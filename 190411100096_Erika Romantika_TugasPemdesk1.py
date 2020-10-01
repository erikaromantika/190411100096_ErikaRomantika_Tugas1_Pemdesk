#1. Membuat program deklarasi 5 variabel
print("1. Menghitung nilai rata-rata")
print("")
a=12
b=5
c=10
d=22
e=9
Mean=(a+b+c+d+e)/5
print(a,"+",b,"+",c,"+",d,"+",e,"/",5)
print("Rata-rata dari nilai tersebut adalah ",Mean)
print("============================================================================")
print("")

#2. Program menghitung luas dan keliling bangun datar segitiga
print("2. Menghitung Luas Segitiga Siku-siku")
print("")
a=input("input nilai alas: ")
b=input("input nilai tinggi: ")
c=input("input nilai sisi miring: ")

L= 0.5*int(a)*int(b)
K= int(a)+int(b)+int(c)
print("Luas segitiga siku-siku yang memiliki alas: {} dan tinggi: {} adalah {}".format(a,b,L))
print("Keliling segitiga siku-siku yang memiliki alas: {}, tinggi: {} dan sisi miring: {} adalah {}".format(a,b,c,K))
print("==============================================================================")
print("")

#3. Program menghitung Indeks Massa tubuh
print("3. Menghitung Indeks Massa Tubuh (BMI)")
print("")
kg= float(input("Masukkan berat badan(kg): "))
m= float(input("Masukkan tinggi badan(m): "))

BMI= kg/(m*m)
print(BMI)

if BMI<18.5:
    print("Berat badan kurang")
elif BMI >= 18.5 and BMI <= 22.9:
    print("Berat badan normal")
elif BMI >= 23 and BMI <= 29.9:
    print("Berat badan berlebih(kecenderungan obesitas)")
else:
    print("Obesitas")
print("==============================================================================")
print("")

#4. Program Menentukan Nilai Maksimal dan Minimal
print("4. Menentukan Nilai Maksimal dan Minimal")
print("")
def Maksimal(nilai1):
    maks=0
    for a in nilai1:
        if a>maks:
            maks=a
    return maks
def Minimal(nilai2):
    mins=999
    for b in nilai2:
        if b<mins:
            mins=b
    return mins

banyakNilai=[]
nilai=int(input("Masukkan banyaknya nilai: "))
for c in range(nilai):
    angka=int(input("Masukkan nilai: "))
    banyakNilai.append(angka)
print("Nilai Maksimal= ",Maksimal(banyakNilai))
print("Nilai Minimal= ",Minimal(banyakNilai))
print("==============================================================================")
print("")

#5. Program Menentukan validasi username dan password
print("5. Validasi Username dan Password")
print("")
password = "trunojoyo1"
username = "student"

for a in range(3):
    pw = input("Masukkan password: ")
    un = input("Masukkan username: ")
    b=2
    if pw==password and un==username:
        print("Anda berhasil masuk")
        break
    else:
        print("Maaf username atau password anda salah, pengulangan tersisa ",b-a)
        continue
print("")
print("==Tunggu beberapa saat==")
print("===============================================================================")

