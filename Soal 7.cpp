#include <bits/stdc++.h>
using namespace std;

int main() {
	int lat, lon, alt, lat2, lon2, alt2;
	cin >> lat >> lon >> alt >> lat2 >> lon2 >> alt2;
	
	int hasilx = (lat-lat2)*(lat-lat2);
	int hasily = (lon-lon2)*(lon-lon2);
	int hasilz = (alt-alt2)*(alt-alt2);
	double hasil = sqrt(hasilx+hasily+hasilz);
	
	cout << fixed << setprecision(2);
	cout << hasil << endl;
}