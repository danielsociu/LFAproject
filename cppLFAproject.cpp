#include <bits/stdc++.h>
using namespace std;
//#define st          first
//#define nd          second
#define pb          push_back
#define mkp         make_pair
#define lwbnd		lower_bound
#define upbnd		upper_bound
#define FOR(i,a,b)  for(int i=(a);i<=(b);++i)
#define FORS(i,a,b) for(int i=(a);i<(b);++i)
#define PII         pair<int,int>
#define VI          vector<int>
#define VPII        vector<PII>
#define ALL(x)      x.begin(),x.end()
#define SZ(x)       ((int)(x).size())
#define ll          long long
#define MOD         1000000007 //998244353
#define maxn        200005
const int INF=0x3f3f3f3f;

int n;

class Stare{
    int n;
    Stare** neighbors=nullptr;
public:
    Stare(){
        this->n=::n;
        Stare* temp[n];
        this->neighbors = temp;
    }
    Stare(int n){
        this->n=n;
        Stare* temp[n];
        this->neighbors = temp;
    }
    ~Stare(){
        delete[] neighbors;
    }
    Stare getStare(int pos){
        return neighbors[pos];
    }
};

class Automata{
    int n;
    Stare* stari=nullptr;
public:
    Automata(int n){
        this->n=n;
        this->stari = new Stare[n];
    }
    
};


int main()
{
    int n=5;
    Automata automat(n);
    cout<<automat.stari;

}
