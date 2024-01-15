/*
You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.

Return a list answer of size 2 where:

answer[0] is a list of all players that have not lost any matches.
answer[1] is a list of all players that have lost exactly one match.
The values in the two lists should be returned in increasing order.

Note:

You should only consider the players that have played at least one match.
The testcases will be generated such that no two matches will have the same outcome.


Example 1:

Input: matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
Output: [[1,2,10],[4,5,7,8]]
Explanation:
Players 1, 2, and 10 have not lost any matches.
Players 4, 5, 7, and 8 each have lost one match.
Players 3, 6, and 9 each have lost two matches.
Thus, answer[0] = [1,2,10] and answer[1] = [4,5,7,8].
Example 2:

Input: matches = [[2,3],[1,3],[5,4],[6,4]]
Output: [[1,2,5,6],[]]
Explanation:
Players 1, 2, 5, and 6 have not lost any matches.
Players 3 and 4 each have lost two matches.
Thus, answer[0] = [1,2,5,6] and answer[1] = [].


Constraints:

1 <= matches.length <= 105
matches[i].length == 2
1 <= winneri, loseri <= 105
winneri != loseri
All matches[i] are unique.
*/

#include <stdio.h>
#include <stdlib.h>

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */

int **findWinners(int **matches, int matchesSize, int *matchesColSize, int *returnSize, int **returnColumnSizes)
{

    int **resultArray = (int **)malloc(2 * sizeof(int *));

    *returnSize = 2; //[[winner], [loser once]] mo
    *returnColumnSizes = (int *)malloc(2 * sizeof(int));

    // initialize the count
    int winnerCount[200000] = {0};
    int loserCount[200000] = {0};

    // keep track of both wins and losts of the input array;
    for (int i = 0; i < matchesSize; i++)
    {
        winnerCount[matches[i][0]]++;
        loserCount[matches[i][1]]++;
    }

    // winner line
    resultArray[0] = (int *)malloc(200000 * sizeof(int));

    // loser line
    resultArray[1] = (int *)malloc(200000 * sizeof(int));

    // to tell the size of the winner and one-time loser array;
    int count0 = 0;
    int count1 = 0;

    for (int i = 0; i < 200000; i++)
    {
        // if wins above zero and no lost;
        if (winnerCount[i] > 0 && loserCount[i] == 0)
        {
            resultArray[0][count0++] = i;
        }
        else if (loserCount[i] == 0)
        {
            resultArray[1][count1++] = i;
        }
    }

    (*returnColumnSizes)[0] = count0;
    (*returnColumnSizes)[1] = count1;

    return resultArray;
}
int main()
{
    int matchesSize;
    printf("HOW MANY MATCHES: ");
    scanf("%d", &matchesSize);

    int **matches = (int **)malloc(matchesSize * sizeof(int *));
    printf("Enter matches (W L)");
    for (int i = 0; i < matchesSize; i++)
    {
        matches[i] = (int *)malloc(2 * sizeof(int));
        printf("Match: %d", i + 1);
        scanf("%d %d", &matches[i][0], &matches[i][1]);
    }

    int *returnSize;
    int *returnClmSize;

    int **resultArray = findWinners(matches, matchesSize, 2, &returnSize, &returnClmSize);

    for (int i = 0; i < returnSize; i++)
    {
        printf("Result Array %d: [", i);
        for (int j = 0; j < returnClmSize[i]; j++)
        {
            printf("%d ", resultArray[i][j]);
        }
        printf("]\n");
    }

    for (int i = 0; i < matchesSize; i++)
    {
        free(matches[i]);
    }

    free(matches);
    free(resultArray[0]);
    free(resultArray[1]);
    free(resultArray);

    return 0;
}