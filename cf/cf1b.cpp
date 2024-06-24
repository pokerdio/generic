#include <bits/stdc++.h>
#include <iostream>
#include <cassert>
using namespace std;

int IsLetter(char c) {
    return c >= 'A' && c <= 'Z';
}

int IsDigit(char c) {
    return c >= '0' && c<= '9';
}

int Flips(string s) {
    int count = 0; 
    int last = -1;
    for (char c : s) {
        int type = IsLetter(c);
        if (type != last) {
            last = type;
            count++;
        }
    }
    return count; 
}

string EncodeNum(int row, int col) {
    return "R" + to_string (row) + "C" + to_string(col);
}

string EncodeLetter(int row, int col) {
    string s;
    while (col > 0) {
        s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[(col - 1) % 26] + s;
        col = (col - 1) / 26;
    }
    return s + to_string(row);
}

int FirstDigit(string s) {
    for (int i=0 ; i<s.size() ; ++i) {
        if (IsDigit(s[i])) {
            return i;
        }
    }
}
 
int DecodeLetter(string s) {
    int ret = 0;
    int aaa = 0; // the value of an only 'A's code of same length as s
    int plus = 1;
    for (int i=s.size()-1 ; i>=0 ; --i) {
        ret += plus * (s[i] - 'A' + 1);
        plus *= 26;
    }
    return ret;
}

struct Cell {
    int row;
    int column; 
    string original_encoding;
    string alt_encoding; 
    Cell(string s) {
        int i; 
        switch(Flips(s)) {
        case 2:
            i = FirstDigit(s);
            row = stoi(s.substr(i));
            column = DecodeLetter(s.substr(0, i));

            // cout << "2 test " << s << " " << row << " " << column << "\n"; 
            original_encoding = s; 
            alt_encoding = EncodeNum (row, column);
            break;
        case 4:
            sscanf(s.c_str(), "R%dC%d", &row, &column);
            // cout << "4 test " << s << " " << row << " " << column << "\n"; 
            original_encoding = s;
            alt_encoding = EncodeLetter(row, column);
            break;
        default:
            assert(0);
        }
    }
}; 

int main(int argc, char* argv[]) {
    int n; 
    cin >> n;

    // for (int i=1 ; i<100 ; ++i) {
    //     cout  << i <<  " " << EncodeLetter(0, i) << "\n";
    // }

    // exit(0);
    for (int i=0 ; i<n ; ++i) {
        string s; 
        cin >> s;
        Cell cell (s);
        cout << cell.alt_encoding << "\n";
    }
}

