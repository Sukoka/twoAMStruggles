#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
*/

#include <stdio.h>
#include <stdbool.h>

bool uniqueOccurrences(int *arr, int arrSize)
{
    int count[2001] = {0};
    for (int i = 0; i < arrSize; i++)
    {
        count[arr[i] + 1000]++;
    }

    // Check if any two frequencies are equal
    for (int i = 0; i < 2001; i++)
    {
        if (count[i] != 0)
        {
            for (int j = i + 1; j < 2001; j++)
            {
                if (count[j] != 0 && count[i] == count[j])
                {
                    return false;
                }
            }
        }
    }

    return true;
}

int main()
{
    int n;
    printf("how many elements: ");
    scanf("%d", &n);
    int arr[n];

    for (int i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
    }
    if (uniqueOccurrences(arr, n))
    {
        printf("True");
    }
    else
    {
        printf("False");
    }
    return 0;
}