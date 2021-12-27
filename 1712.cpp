// 백준 1712 손익분기점
#include <iostream>
using namespace std;

long Break_Even_Point(long a,long b,long c){
	long result=0;
	if (b>=c) return -1;
	else {
		result = a*(c-b)+(c-b);
		return result;
	}

}
	



int main(){
	long A,B,C;
	cin >> A >> B >> C ;
	long result = Break_Even_Point(A,B,C);
	cout << result << endl;
}
