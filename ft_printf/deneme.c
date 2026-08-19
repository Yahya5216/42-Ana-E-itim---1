
#include "ft_printf.h"

//#include <stdio.h>
//#include <stdarg.h> // Varyadik makrolar için gerekli kütüphane

// 'adet': Kaç sayı gönderildiğini tutan sabit parametre.
// '...': Geri kalan değişken sayıdaki argümanları temsil eder.
int sayilari_topla(int adet, ...)
{
    va_list arguman_listesi; // 1. Adım: Listeyi tanımla
    int toplam = 0;

    // 2. Adım: Listeyi başlat. Son sabit parametre olan 'adet'i veriyoruz ki 
    // sistem ekstra argümanların nerede başladığını bilsin.
    va_start(arguman_listesi, adet); 

    for (int i = 0; i < adet; i++)
    {
        // 3. Adım: Sıradaki argümanı 'int' olarak çek ve toplama ekle.
        // Her va_arg çağrısı bizi listedeki bir sonraki elemana taşır.
        toplam += va_arg(arguman_listesi, int);
    }

    // 4. Adım: Bellek sızıntılarını önlemek için listeyi temizle ve kapat.
    va_end(arguman_listesi); 

    return toplam;
}

int main()
{
    // İlk parametre '3', yani fonksiyona 3 tane toplanacak sayı (10, 20, 30) yolluyoruz.
    int sonuc1 = sayilari_topla(3, 10, 20, 30);
    printf("Sonuc 1: %d\n", sonuc1); // Çıktı: 60

    // İlk parametre '5', yani 5 tane sayı (1, 2, 3, 4, 5) yolluyoruz.
    int sonuc2 = sayilari_topla(5, 1, 2, 3, 4, 5);
    printf("Sonuc 2: %d\n", sonuc2); // Çıktı: 15

    return 0;
}