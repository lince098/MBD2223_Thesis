#include <iostream>

std::string longestPalindrome(const std::string &s) {
    std::string res = "";
    int resLen = 0;
    int length = s.length();

    for (int i = 0; i < length; ++i) {
        int l = i;
        int r = i;

        while (r < length && l >= 0 && s[r] == s[l]) {
            if (r - l + 1 >= resLen) {
                resLen = r - l + 1;
                res = s.substr(l, r - l + 1);
            }
            ++r;
            --l;
        }

        r = i + 1;
        l = i;

        while (r < length && l >= 0 && s[r] == s[l]) {
            if (r - l + 1 >= resLen) {
                resLen = r - l + 1;
                res = s.substr(l, r - l + 1);
            }
            ++r;
            --l;
        }
    }

    return res;
}

int main() {
    std::string input = "ababjañlsdkfjjjkkjjjapodsiufapouf";
    std::string result = longestPalindrome(input);
    std::cout << "Longest Palindrome: " << result << std::endl;

    return 0;
}