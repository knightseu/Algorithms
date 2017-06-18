# http://www.lintcode.com/en/problem/big-integer-multiplication/
# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2
#
# Have you met this question in a real interview? Yes
# Example
# The length of both num1 and num2 is < 110.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.


def multiply_big_num(num1, num2):
    if not num1 or not num2:
        return

    len1 = len(num1)
    len2 = len(num2)
    len3 = len1 + len2

    num3 = [0 for _ in range(len3)]

    carry = 0
    for i in range(len1-1, -1, -1):
        # import pdb; pdb.set_trace()
        # carry = 0
        for j in range(len2-1, -1, -1):
            product = carry + num3[i+j+1] + int(num1[i])*int(num2[j])
            num3[i+j+1] = product % 10
            carry = product // 10
            print(num3)

        # num3[i] = carry

    print(num3)


multiply_big_num("12", "11")


