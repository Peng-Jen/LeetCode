#include <cmath>
#include <climits>
class Solution
{
public:
    int reverse(int x)
    {
        if (x == INT_MIN)
            return 0;
        bool is_negative = (x < 0) ? true : false;
        int result = 0, p = abs(x);
        while (p)
        {
            if (result > INT_MAX / 10)
                return 0;
            else
                result *= 10;
            if (result > INT_MAX - p % 10)
                return 0;
            else
                result += p % 10;
            p /= 10;
        }
        return result * (1 - 2 * is_negative);
    }
};
