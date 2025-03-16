#include <bits/stdc++.h>
using namespace std;
int n;
 bool is_prime(int i){
    if(i<2) return false;
    for (int x = 2; x <= sqrt(i); x++) {
        if (i % x == 0) {
            return false;
        }
    }
    return true;
}
int main(){
    int n;
    cin>>n;
    for(int i=2;i <= n/2; i++){
        if (!is_prime(i)){
            if(!is_prime(n-i)){
                cout<<i<<' '<<n-i;
                break;
            }
        }
    }
}