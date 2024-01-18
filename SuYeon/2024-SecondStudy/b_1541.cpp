/*
-로 시작하는 숫자부터 다시 -가 붙은 숫자 전까지를 괄호로 묶는다로 생각하자!
부호를 저장하는 배열과, 숫자를 저장하는 배열을 따로 만들자!
결과: 맞았습니다!!
*/

#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main(){
    vector<char> signVector;
    vector<int> numVector;

    string input;
    string concatNum;

    // cout << "input: ";
    getline(cin, input);
    // cout << input << endl; 

    for(int i=0;i<input.length();i++){
        if(i==0){
            if(input[i]=='-'){
                signVector.push_back('-');
            }else{
                signVector.push_back('+');
                concatNum+=input[i];
                int j = i+1;
                while((input[j]!='+')&&(input[j]!='-')){
                    concatNum+=input[j];
                    j++;
                    i++;
                }
                int resultNum = stoi(concatNum);
                numVector.push_back(resultNum);
                concatNum.clear(); //문자열 초기화
            }
        }else{
            if(input[i]=='+'){
                signVector.push_back('+');
            }else if(input[i]=='-'){
                signVector.push_back('-');
            }else{
                concatNum+=input[i];
                int j = i+1;
                while((input[j]!='+')&&(input[j]!='-')&&(j<input.length())){
                    concatNum+=input[j];
                    j++;
                    i++;
                }
                int resultNum = stoi(concatNum);
                numVector.push_back(resultNum);
                concatNum.clear(); //문자열 초기화
            }
        }
    }

    // for(auto s:signVector){
    //     cout << s << " ";
    // }
    // cout << endl;
    // for(auto n:numVector){
    //     cout << n << " ";
    // }

    int result = 0;
    for(int i=0;i<signVector.size();i++){
        if(signVector[i]=='+'){
            result+=numVector[i];
        }else{
            result-=numVector[i];
            int j = i+1;
            while((signVector[j]!='-')&&(j<signVector.size())){
                result-=numVector[j];
                i++;
                j++;
            }

        }
    }
    //cout << "result: " << result << endl;
    cout << result << endl;
}

