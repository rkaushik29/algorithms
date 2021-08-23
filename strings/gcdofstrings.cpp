#include <string>

string gcdOfStrings(string str1, string str2) {
    string s = "";
    if( (str1+str2) != (str2+str1) ) {
        s = "";
    }
    else if(str1 == str2) {
        s = str1;
    }
    else if(str1.size() > str2.size()) {
        s = gcdOfStrings(str1.substr(str2.size(), str1.size()-1), str2);
    }
    else if(str2.size() > str1.size()) {
        s = gcdOfStrings(str2.substr(str1.size(), str2.size()-1), str1);
    }
    return s;
}