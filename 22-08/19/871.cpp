#include <vector>
#include <iostream>
using namespace std;


class Solution {
public:
    int minRefuelStops(int target, int startFuel, vector<vector<int> >& stations) {
        int n = stations.size();
        vector<vector<int> > dp(n + 1, vector<int>(target + 1, 0));

        for (int i = 0; i <= n; ++i) {
            dp[i][0] = 0;
        }

        for (int i = 1; i <=n; i++){
            for (int j=1; j <=i; j++){
                dp[i][j] = dp[i-1][j];
                if (j >= stations[i-1][0]){
                    dp[i][j] = max(dp[i][j], dp[i-1][j-1] + stations[i-1][1]);
                }
            }
        }


        for (int j = 0; j < n+1; j++){
            if (dp[n][j] >= target){
                return j;
            }
        }
        return -1;
    }
};

// create a test case to test the solution
// target = 1, startFuel = 1, stations = [[0,1]]
// output = 1
// target = 100, startFuel = 1, stations = [[0,1],[10,100]]
// output = -1
// target = 100, startFuel = 10, stations = [[0,1],[10,100]]
// output = 1
// target = 100, startFuel = 10, stations = [[0,1],[10,100],[20,200],[30,300],[40,400],[50,500],[60,600],[70,700],[80,800],[90,900],[100,1000]]
// output = 7
// main function to test the solution
int main() {
    Solution s;
    int target = 100;
    int startFuel = 10;
    vector<vector<int> > stations {{0,1},{10,100},{20,200},{30,300},{40,400},{50,500},{60,600},{70,700},{80,800},{90,900},{100,1000}};
    cout << s.minRefuelStops(target, startFuel, stations) << endl;
    return 0;
}