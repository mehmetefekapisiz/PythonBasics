notlar = [30, 0, 0, 40, 40, 25, 50, 55, 37, 40, 55, 45, 65, 35, 50, 60,
          65, 65, 42, 45, 70, 37, 60, 55, 0, 45, 55, 0, 65, 60, 50, 50,
          35, 95, 75, 47, 75, 55, 55, 82, 40, 75, 80, 60, 75, 55, 80, 50,
          50, 65, 77, 47, 77, 60, 60, 60, 50, 52, 67, 45, 55, 40, 75, 32,
          50, 45, 85, 50, 70, 40, 47, 55, 50, 95, 55, 80, 25, 25, 80, 37,
          35, 32, 80, 50, 55, 60, 65, 55, 70, 30, 55, 32, 65, 47, 75, 45,
          40, 40, 45, 60, 40, 80, 33, 55, 55, 35, 42, 42, 42, 60, 70, 65,
          0, 57, 45, 32, 37, 40, 15, 42, 40, 80, 90, 75, 75, 60, 85, 0, 70,
          45, 80, 80, 65, 50, 42, 63, 70, 55, 50, 75, 52, 45, 50, 70, 75, 45,
          52, 60, 85, 58, 58, 55, 50, 55, 50, 55, 0, 70, 80, 65, 45, 62]

yuksek_notlar = [notu for notu in notlar if isinstance(notu, int) and notu >= 90]
sayi = len(yuksek_notlar)

print("90 ve üstü not alan öğrenci sayısı:", sayi)
