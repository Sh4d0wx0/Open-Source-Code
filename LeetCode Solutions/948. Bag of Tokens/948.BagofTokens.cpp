#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int bagOfTokensScore(vector<int>& tokens, int power){
        sort(tokens.begin(), tokens.end());
        int low = 0;
        int high = tokens.size() - 1;
        int score = 0;
        int prev = score;
        while (low <= high){
            prev = score;
            if (power >= tokens[low]){
                power -= tokens[low];
                score++;
                low++;
            }else if (power < tokens[high]){
                if (score > 0){
                    power += tokens[high];
                    score--;
                    high--;
                }else{
                    break;
                }
            }else{
                break;
            }
        }

        if (prev > score){
            return prev;
        }

        return score;
    }
};