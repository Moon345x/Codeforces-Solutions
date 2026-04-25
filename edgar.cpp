#include <bits/stdc++.h>
#include <iostream>
using namespace std;

int main(){


    int x;
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin>> x;
    string k;
    for (int i = 0; i < x; i++)
    {
        char m;
        cin>>k;

        for (int j = 0; j < k.length()-1; j++)
        {
            stack<char> s;
            m = k[j];
            if(m == ("(" || "[" || "{")){
                s.push(m);
            }
            else{
                if(m == ')'){
                    if(s.top() == '(') s.pop();
                    else printf("NO"); break;
                }
                if(m == ']'){
                    if(s.top() == '[') s.pop();
                    else printf("NO"); break;
                }
                else{
                    if(s.top() == '{') s.pop();
                    else printf("NO"); break;
                }
                if(s.empty()) printf("YES");
            }
        }


    }

    return 0;
}