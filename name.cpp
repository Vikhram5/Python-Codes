#include<iostream>
#include<vector>
#include<algorithm>
#include<unordered_map>
#include <string>

using namespace std;

void solve(string &str,int idx,vector<string>&res){
        if(idx==str.size()){
            res.push_back(str);
            return;
        }
        for(int i=idx;i<str.size();i++){
            swap(str[i],str[idx]);
            solve(str,idx+1,res);
            swap(str[i],str[idx]);
        }
    }

int main(){

    vector<string>result;
    string str="vikhram";
    solve(str,0,result);
    for(int i=0;i<result.size();i++){
        cout<<result[i]<<endl;
    }

    return 0;
}