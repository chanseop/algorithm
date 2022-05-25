#include <iostream>
using namespace std;

int main() {
	int a,b;
	int i = 0;

	while (!(cin>>a>>b).eof()) {   //EOF파일에 대한 이해가 필요했다.
		cout << a + b << "\n";      //문제에서는 몇개의 문자가 필요한지 나와 있지 않았기 때문에 더이상 문자가 존재하지 않을때 끝나는 코딩이 필요했고
	}                             //그래서 EOF에 대한 이해가 필요해서 이해를 한다음 사용하였다.

	return 0;
}
/*
#include <iostream>
using namespace std;

int main() {
	int a, b;
	while (cin >> a >> b) {
		cout << a + b << "\n";
	}
	return 0;
}*/
