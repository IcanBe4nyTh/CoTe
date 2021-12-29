// 백준 1712 손익분기점
#include <iostream>
using namespace std;

long Break_Even_Point(long a,long b,long c){
	long result=0;
	if (b>=c) return -1;
	else {
		result = a/(c-b)+1;
		return result;
	}

}
int main(){
	long A,B,C;
	cin >> A >> B >> C ;
	long result = Break_Even_Point(A,B,C);
	cout << result << endl;
}

//첫번째 for문으로 돌리니까 시간초과길래
//두번째에서는 O(n)으로 풀어야될거 같아서 test케이스 보고 규칙 찾아서 방정식을 넣어봤는데 아예 답이 틀렸다
//세번째에서는 문제 다시 읽어보고 손익분기점이 발생하는 정수를 구할 수 있는 지점을 구하는 방정식을 생각해보았다
//처음엔 a/(c-b) 만 했는데 손익분기점을 넘겨야 하기때문에 +1을 넣어주니까 
