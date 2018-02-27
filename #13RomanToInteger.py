#13.给定一个罗马数字转换成整数
# 对应I:1,V:5,X:10,L:50,C:100,D:500,M:1000
#其中算法：IV:
class Solution:
    # @return an integer
    def romanToInt(self, s):
        numeral_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C":100, "D": 500, "M": 1000}
        decimal = 0
        for i in range(len(s)):
            if i > 0 and numeral_map[s[i]] > numeral_map[s[i - 1]]:
                decimal += numeral_map[s[i]] - 2 * numeral_map[s[i - 1]]
            else:
                decimal += numeral_map[s[i]]
        return decimal

if __name__ == "__main__":
    print Solution().romanToInt("IIVX")
    print Solution().romanToInt("MMMCMXCIX")
