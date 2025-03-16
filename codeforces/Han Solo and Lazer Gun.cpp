#include <bits/stdc++.h>
#include <vector>
#define M_PI 3.14159265358979323846
 
using namespace std;
int n,yo,xo,xi,yi;
int main(){
    cin>>n>>xo>>yo;
    vector<int[2]>stormtroopers(n);
    set<double>stormtroopers_angle;
    for(int i=0;i<n;i++){
        cin>>xi>>yi;
        stormtroopers[i][0] = xi;
        stormtroopers[i][1] = yi;
 
    }
    //find angles
    for(int i=0;i<n;i++){
        double angle= atan2(stormtroopers[i][1] - yo, stormtroopers[i][0] - xo);
        angle=angle*180/M_PI;
        if(angle<0){
            angle=angle+180;
        }
        stormtroopers_angle.insert(angle);
    }
    cout<<stormtroopers_angle.size()<<endl;
}