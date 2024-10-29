main.cpp
```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define vec vector
#define str string
#define all(x) x.begin(),x.end()
#define p(x) cout<<(x)<<endl
#define pv(x) for(auto& _:x){cout<<(_)<<' ';}cout<<endl

#ifdef LOCAL
#define d(x) cerr<<#x<<'='<<x<<endl
#define dd(x) cerr<<x;
#define dv(x) cerr<<#x<<"=["; for(auto& _ :x){dd(_); cerr<<' ';} cerr<<"]\n"
#define ddv(x) cerr<<"["; for(auto& _ :x){dd(_); cerr<<' ';} cerr<<"]\n"
#define dvv(x) cerr<<#x<<"="; for(auto& _ :x){ddv(_); cerr<<"  ";} cerr<<"\n"
#define dm(x) cerr<<#x<<"=["; for(auto& _ :x){cerr<<_.first<<":"<<_.second; cerr<<' ';} cerr<<"]\n"
#else
#define d(...)
#define dv(...)
#define dvv(...)
#define dm(...)
#endif

void solve(){

}

int main(){
  ios::sync_with_stdio(false);
  cin.tie(0); cout.tie(0);
  int t;cin>>t;while(t--){solve();}
}
```

```cpp
#ifdef LOCAL
#include "algo/debug.h"
#else
#define debug(...) 69
#endif
```

r.sh
```c++
rm bin
clear

# # ---------------------------------- compile --------------------------------- #
# g++ $1.cpp -O2 -Wshadow -Wall -std=c++17 -o bin -DLOCAL
# ./bin <in 2> debug
# # ---------------------------------------------------------------------------- #

# ----------------------------------- debug ---------------------------------- #
g++ $1.cpp -g -o2 -std=c++2a -o bin -DLOCAL
gdb ./bin -q 2> debug
# ---------------------------------------------------------------------------- #
```

keybinding.json
```json
{
	"key": "ctrl+enter",
	"command": "workbench.action.terminal.sendSequence",
	"args": {
		"text": "bash r.sh sol/${fileBasenameNoExtension}\u000D"
	},
},
```

.gdbinit
```
set print pretty on
run < in
```

debug.h
```cpp
template <typename A, typename B>
string to_string(pair<A, B> p);s
template <typename A, typename B, typename C>
string to_string(tuple<A, B, C> p);
template <typename A, typename B, typename C, typename D>
string to_string(tuple<A, B, C, D> p);

string to_string(const string& s) { return '"' + s + '"';}
string to_string(const char* s) {return to_string((string) s);}
string to_string(bool b) {return (b ? "true" : "false");}

string to_string(vector<bool> v) {
  bool first = true;
  string res = "{";
  for (int i = 0; i < static_cast<int>(v.size()); i++) {
    if (!first) {
      res += ", ";
    }
    first = false;
    res += to_string(v[i]);
  }
  res += "}";
  return res;
}

template <size_t N>
string to_string(bitset<N> v) {
  string res = "";
  for (size_t i = 0; i < N; i++) {
    res += static_cast<char>('0' + v[i]);
  }
  return res;
}

template <typename A>
string to_string(A v) {
  bool first = true;
  string res = "{";
  for (const auto &x : v) {
    if (!first) {
      res += ", ";
    }
    first = false;
    res += to_string(x);
  }
  res += "}";
  return res;
}

  

template <typename A, typename B>
string to_string(pair<A, B> p) {
  return "(" + to_string(p.first) + ", " + to_string(p.second) + ")";
}

  

template <typename A, typename B, typename C>
string to_string(tuple<A, B, C> p) {
  return "(" + to_string(get<0>(p)) + ", " + to_string(get<1>(p)) + ", " + to_string(get<2>(p)) + ")";
}

  

template <typename A, typename B, typename C, typename D>
string to_string(tuple<A, B, C, D> p) {
  return "(" + to_string(get<0>(p)) + ", " + to_string(get<1>(p)) + ", " + to_string(get<2>(p)) + ", " + to_string(get<3>(p)) + ")";
}

  

void debug_out() { cerr << endl; }
template <typename Head, typename... Tail>
void debug_out(Head H, Tail... T) {
  cerr << " " << to_string(H);
  debug_out(T...);
}

#ifdef LOCAL
#define debug(...) cerr << "[" << #__VA_ARGS__ << "]:", debug_out(__VA_ARGS__)
#else
#define debug(...) 42
#endif
```

help
```cpp
/*-------------------------------------vec2------------------------------------------*/
struct vec2 { int x, y, id; };

vec2 operator+(vec2 a, vec2 b) { return {a.x + b.x, a.y + b.y}; }
vec2 operator-(vec2 a, vec2 b) { return {a.x - b.x, a.y - b.y}; }
vec2& operator+=(vec2 &a, const vec2 &b) { a.x += b.x; a.y += b.y; return a; }
vec2& operator-=(vec2 &a, const vec2 &b) { a.x -= b.x; a.y -= b.y; return a; }

istream& operator>>(istream &is, vec2 &x) { return is >> x.x >> x.y; }
ostream& operator<<(ostream &os, vec2 x) { return os << '{' << x.x << ' ' << x.y << '}'; }

bool operator==(const vec2 &v1, const vec2 &v2) { return (v1.x == v2.x && v1.y == v2.y); }
bool operator<(const vec2 &v1, const vec2 &v2) { return tie(v1.x, v1.y) < tie(v2.x, v2.y); }
/*-----------------------------------------------------------------------------------*/

/*------------------------------------ll* mod-----------------------------------------*/
const ll mod = 1e9 + 7;

struct ml;
ml inv(ml a);
ml pow(ml b, ll exp);

struct ml {
    ll v;
    ml(ll _v = 0) : v(_v % mod) {
        if (v < 0) v += mod;
    }
    ml(const ml &other) : v(other.v) {}
    ml& operator=(const ml &other) {
        v = other.v;
        return *this;
    }
};

ml& operator++(ml &a) {
    a.v = (a.v + 1) % mod;
    return a;
}

ml& operator--(ml &a) {
    a.v = (a.v - 1 + mod) % mod;
    return a;
}

ml operator++(ml &a, int) {
    ml temp = a;
    a.v = (a.v + 1) % mod;
    return temp;
}

ml operator--(ml &a, int) {
    ml temp = a;
    a.v = (a.v - 1 + mod) % mod;
    return temp;
}

ml& operator+=(ml &a, const ml &b) {
    a.v = (a.v + b.v) % mod;
    return a;
}

ml& operator-=(ml &a, const ml &b) {
    a.v = (a.v - b.v + mod) % mod;
    return a;
}

ml& operator*=(ml &a, const ml &b) {
    a.v = (a.v * b.v) % mod;
    return a;
}

ml& operator/=(ml &a, const ml &b) {
    a.v = (a.v * inv(b).v) % mod;
    return a;
}

ml operator+(ml a, ml b) { return {(a.v + b.v) % mod}; }
ml operator-(ml a, ml b) { return {((a.v - b.v) % mod + mod) % mod}; }
ml operator*(ml a, ml b) { return {(a.v * b.v) % mod}; }
ml operator/(ml a, ml b) { return {(a * inv(b))}; }

bool operator==(ml a, ml b) { return a.v == b.v; }
bool operator!=(ml a, ml b) { return a.v != b.v; }
bool operator<(ml a, ml b) { return a.v < b.v; }
bool operator<=(ml a, ml b) { return a.v <= b.v; }
bool operator>(ml a, ml b) { return a.v > b.v; }
bool operator>=(ml a, ml b) { return a.v >= b.v; }

istream& operator>>(istream &is, ml &a) { return is >> a.v; }
ostream& operator<<(ostream &os, ml a) { return os << a.v; }

ml inv(ml a) { return pow(a, mod - 2); }

ml pow(ml b, ll exp) {
    ml r = 1;
    exp = exp % (mod - 1);
    while (exp > 0) {
        if (exp & 1) r *= b;
        b *= b;
        exp >>= 1;
    }
    return r;
}
/*-----------------------------------------------------------------------------------*/
```