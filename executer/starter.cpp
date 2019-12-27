
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(int argcv, char *argv[])
{
	char c;
	string fcontent;
	ifstream file("starter.txt");
	file >> noskipws;
	while (file >> c)
	{
		fcontent += c;
	};
	file.close();
	const char *command = fcontent.c_str();
	system(command);
	cout << fcontent;
	
	

}


