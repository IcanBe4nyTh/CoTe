// 백준 1712 손익분기점

#include <iostream>
using namespace std;

unsigned long Break_Even_Point(unsigned long a,unsigned long b,unsigned long c){
	unsigned long total_income=0;
	unsigned long total_cost=0;
	if (b>=c) return -1;
	for(unsigned long i=0;;i++){
		total_income=c*i;
		total_cost=a+b*i;
		if(total_income>total_cost) return i;
	}

}

int main(){
	unsigned long A,B,C;
	cin >> A >> B >> C ;
	unsigned long result = Break_Even_Point(A,B,C);
	cout << result << endl;
}
