#include <string>
using namespace std;

class Solution
{
public:
    string addBinary(string a, string b)
    {
        int maxLEN = max(a.length(), b.length());
        a.insert(0, maxLEN - a.length(), '0');
        b.insert(0, maxLEN - b.length(), '0');
        string result = "";
        int carry = 0;
        for (int i = 0; i < maxLEN; i++)
        {
            carry += (a[a.length() - 1 - i] - '0') + (b[b.length() - 1 - i] - '0');
            char bit = (carry % 2) + '0';
            carry /= 2;
            result.insert(0, 1, bit);
        }
        if (carry == 1)
            result.insert(0, 1, '1');
        return result;
    }
};
