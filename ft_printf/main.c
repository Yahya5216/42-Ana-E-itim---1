
#include <stdio.h>
#include "ft_printf.h"

int main(void)
{
    int len_orj;
    int len_ft;

    char *str = "Test Metni";
    char *null_str = NULL;
    int num = -2147483648;          
    unsigned int unum = 4294967295; 
    int hex_val = 255;

    printf("========== TESTLER BASLIYOR ==========\n\n");

    // 1. String ve Char Testi
    len_orj = printf("ORJ: Karakter: %c, String: %s, Null String: %s\n", 'Z', str, null_str);
    len_ft  = ft_printf("FT : Karakter: %c, String: %s, Null String: %s\n", 'Z', str, null_str);
    printf("Uzunluklar -> ORJ: %d | FT: %d\n\n", len_orj, len_ft);

    // 2. Sayı Testleri (d, i, u)
    len_orj = printf("ORJ: Sayi: %d, Int Min: %i, Unsigned: %u\n", 42, num, unum);
    len_ft  = ft_printf("FT : Sayi: %d, Int Min: %i, Unsigned: %u\n", 42, num, unum);
    printf("Uzunluklar -> ORJ: %d | FT: %d\n\n", len_orj, len_ft);

    // 3. Hexadecimal ve Yüzde Testi (x, X, %%)
    len_orj = printf("ORJ: Hex(kucuk): %x, Hex(buyuk): %X, Yuzde: %%\n", hex_val, hex_val);
    len_ft  = ft_printf("FT : Hex(kucuk): %x, Hex(buyuk): %X, Yuzde: %%\n", hex_val, hex_val);
    printf("Uzunluklar -> ORJ: %d | FT: %d\n\n", len_orj, len_ft);

    // 4. Pointer Testi (p)
    len_orj = printf("ORJ: Pointer: %p, Null Pointer: %p\n", str, NULL);
    len_ft  = ft_printf("FT : Pointer: %p, Null Pointer: %p\n", str, NULL);
    printf("Uzunluklar -> ORJ: %d | FT: %d\n\n", len_orj, len_ft);

    printf("========== TESTLER BITTI ==========\n");

    return (0);
}