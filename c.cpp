#include<bits/stdc++.h>
using namespace std;
int main(){
    long long m,n;cin>>m>>n;
    vector<long long>v(m);
    for(long long  i = 0; i< m ;i++){
        cin>>v[i];
    }
    while(n--){
        long long l,r,k;cin>>l>>r>>k;
        long long div = pow(10,k);
        long long res=1;
        for(long long i =l-1; i < r ; i++){
            res=res*v[i];
        }
        if(res % div ==0)cout<<"YES"<<endl;
        else cout<<"NO"<<endl;
    }
}