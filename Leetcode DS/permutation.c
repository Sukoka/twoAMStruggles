/*
Write a program in C to print all permutations of a given string using pointers.
Expected Output :

The permutations of the string are :                                                                         
abcd  abdc  acbd  acdb  adcb  adbc  bacd  badc  bcad  bcda  bdca  bdac  cbad  cbda  cabd  cadb  cdab  cdba  db
ca  dbac  dcba  dcab  dacb  dabc
*/
#include <stdio.h>
#include <string.h>

// Function to swap two characters in a string
void swap(char *x, char *y) {
    char temp = *x;
    *x = *y;
    *y = temp;
}

// Recursive function to generate all permutations of a string
void generatePermutations(char *str, int start, int end) {
    if (start == end) {
        printf("%s\n", str); // Print the current permutation
    } else {
        for (int i = start; i <= end; i++) {
            // Swap the current character with the character at index 'i'
            swap(&str[start], &str[i]);

            // Recursively generate permutations for the remaining characters
            generatePermutations(str, start + 1, end);

            // Backtrack: restore the original order of characters
            swap(&str[start], &str[i]);
        }
    }
}

int main() {
    char inputString[100];

    // Get input string from the user
    printf("Enter a string: ");
    scanf("%s", inputString);

    int length = strlen(inputString);

    // Generate and print all permutations of the input string
    generatePermutations(inputString, 0, length - 1);

    return 0;
}
