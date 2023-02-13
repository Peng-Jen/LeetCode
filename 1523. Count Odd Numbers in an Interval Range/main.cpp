class Solution
{
public:
    int countOdds(int low, int high)
    {
        int nums = high - low + 1;
        if (nums % 2 == 0)
            return nums / 2;
        return nums / 2 + low % 2;
    }
};
