#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void append(char **result, char sym, int times) {
    int len = strlen(*result);
    *result = realloc(*result, len + times + 1);
    for (int i = 0; i < times; i++) {
        (*result)[len + i] = sym;
    }
    (*result)[len + times] = '\0';
}

char *intToRoman(int num) {
    char *result = (char *)malloc(16 * sizeof(char));
    result[0] = '\0';
    int thousands = num / 1000;
    num %= 1000;
    int hundreds = num / 100;
    num %= 100;
    int tens = num / 10;
    int ones = num % 10;

    append(&result, 'M', thousands);
    if (hundreds == 9) {
        strncat(result, "CM", 2);
    } else if (hundreds >= 5) {
        strncat(result, "D", 1);
        append(&result, 'C', hundreds - 5);
    } else if (hundreds == 4) {
        strncat(result, "CD", 2);
    } else {
        append(&result, 'C', hundreds);
    }

    if (tens == 9) {
        strncat(result, "XC", 2);
    } else if (tens >= 5) {
        strncat(result, "L", 1);
        append(&result, 'X', tens - 5);
    } else if (tens == 4) {
        strncat(result, "XL", 2);
    } else {
        append(&result, 'X', tens);
    }

    if (ones == 9) {
        strncat(result, "IX", 2);
    } else if (ones >= 5) {
        strncat(result, "V", 1);
        append(&result, 'I', ones - 5);
    } else if (ones == 4) {
        strncat(result, "IV", 2);
    } else {
        append(&result, 'I', ones);
    }
    return result;
}

int main() {
    int x;
    printf("Please input x: ");
    scanf("%d", &x);

    char *romanNumeral = intToRoman(x);
    printf("%s\n", romanNumeral);

    free(romanNumeral);

    return 0;
}
