class Solution:
    '''
    intdevide{}, bitdivide{} and finalcheck{} functions are used to compute the integer result of a division coperation using bit compuation
    '''
    def intdivide(self, dividend: int, divisor: int):
        if dividend > 0 and divisor > 0:
            self.mark = 1
        elif dividend < 0 and divisor < 0:
            self.mark = 1
            dividend = -dividend
            divisor = -divisor
        elif dividend > 0 and divisor < 0:
            self.mark = -1
            divisor = -divisor
        else:
            self.mark = -1
            dividend = -dividend
        return self.finalcheck(self.bitdivide(dividend, divisor), self.mark)

    def bitdivide(self, dividend_: int, divisor_: int):
        result = 0
        for i in range(31,-1,-1):
            if (dividend_>>i) - divisor_ >=0:
                result += 2**i
                dividend_ -= divisor_<<i
        return result

    def finalcheck(self, result: int, mark: int):
        if mark == 1:
            if result < -2 ** 31 or result > 2 ** 31 - 1:
                return 2 ** 31 - 1
            else:
                return result
        else:
            if -result < -2 ** 31 or -result > 2 ** 31 - 1:
                return 2 ** 31 - 1
            else:
                return -result


if __name__ == "__main__":
    divide = 7
    divisor = 3
    Solu = Solution()
    print(Solu.intdivide(divide, divisor))