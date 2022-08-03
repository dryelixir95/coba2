print('Mencari jarak, kecepatan, waktu'.center(50))
print("Apa yang anda cari? \n1.Jarak? \n2.kecepatan? \n3.waktu?\n")
pilihan = int(input('masukkan pilihan anda? '))

def jarak():
    a = int(input('masukkan kecepatan '))
    b = int(input('masukkan waktu '))
    print('jadi jarak yang ditempuh ialah ')
    print(a*b)

def kecepatan():
    c = int(input('masukkan jarak '))
    b = int(input('masukkan waktu '))
    print('jadi kecepatan rata-rata ialah ')
    print(c/b)

def waktu():
    c = int(input('masukkan jarak '))
    a = int(input('masukkan kecepatan '))
    print('jadi waktu yang ditempuh ialah ')
    print(c/a)

if pilihan == 1:
    jarak()
elif pilihan == 2:
    kecepatan()
elif pilihan == 3:
    waktu()
