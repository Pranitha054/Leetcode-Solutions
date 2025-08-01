class Solution(object):
    def smallestNumber(self, num):
        if num >= 0:
            digits = sorted(str(num))
            if digits[0] == '0':
                for i in range(1, len(digits)):
                    if digits[i] != '0':
                        digits[0], digits[i] = digits[i], digits[0]
                        break
            return int(''.join(digits))
        else:
            digits = sorted(str(-num), reverse=True)
            return -int(''.join(digits))
