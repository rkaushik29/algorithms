#include <string>
#include <vector>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);


/*
 * Complete the 'maxValue' function below.
 *
 * The function is expected to return a LONG_INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. 2D_INTEGER_ARRAY rounds
 */

long maxValue(int n, vector<vector<int>> rounds) {
    long max = 0;
    
    long *investements = (long*)malloc(sizeof(long)*n);
    int i = 0;
    for(i = 0; i < n; ++i) {
        investements[i] = 0;
    }
    i = 0;
    while (i < rounds.size()) {
        int left = rounds[i][0];
        int right = rounds[i][1];
        int contribution = rounds[i][2];
        
        right--;
        left--;
        int j = 0;
        
        for (j = left; j <= right; ++j) {
            investements[j] += contribution;
        }
        ++i;
    }
    max = investements[0];
    for (i = 1; i < n; ++i) {
        if (investements[i] > max) {
            max = investements[i];
        }
    }
    
    return max;

}
