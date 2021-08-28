#include<bits/stdc++.h>
using namespace std;
int main() {
	int n;
	cin>>n;
	int droppedPackets = 0;
	vector<int> packets(n);
	for(int i=0;i<n;i++) {
		cin>>packets[i];
	}
	deque<int> second;
	deque<int> tenseconds;
	deque<int> minute;
	second.push_back(packets[0]);
	tenseconds.push_back(packets[0]);
	minute.push_back(packets[0]);
	for(int i=1;i<n;i++) {
		while(!second.empty() && second.front() < packets[i]) {
			second.pop_front();
		}
		while(!tenseconds.empty() && (tenseconds.front() + 9) < packets[i]) {
			tenseconds.pop_front();
		}
		while(!minute.empty() && (minute.front() + 59) < packets[i]) {
			minute.pop_front();
		}
		if(second.size() >= 3) {
			droppedPackets++;
		}
		else if(tenseconds.size() >= 20) {
			droppedPackets++;
		}
		else if(minute.size() >= 60) {
			droppedPackets++;
		}
		second.push_back(packets[i]);
		tenseconds.push_back(packets[i]);
		minute.push_back(packets[i]);
	} 
	cout<<droppedPackets;
}