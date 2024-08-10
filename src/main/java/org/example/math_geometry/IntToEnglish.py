class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        ones_map = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
        }

        twos_map = {
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety"
        }

        def get_string(n):  # takes numbers in 3s and returns a string
            # 123, 120, 102, 100, 012
            hundred = n // 100
            res = []
            if hundred:  # if hundred > 0
                res.append(ones_map[hundred] + " Hundred")
            last_2 = n % 100
            if last_2 >= 20:
                tens, ones = last_2 // 10, last_2 % 10
                res.append(twos_map[tens * 10])
                if ones:
                    res.append(ones_map[ones])
            elif last_2:  # if 0 < last_2 < 20
                res.append(ones_map[last_2])

            return " ".join(res)

        postfix = ["", " Thousand", " Million", " Billion"]
        res = []
        i = 0
        while num:
            digits = num % 1000
            s = get_string(digits)  # 1,000,000
            if s:  # if s is non-empty string
                res.append(s + postfix[i])  # res is built in reverse, extract last 3 digits first
            i += 1
            num = num // 1000

        return " ".join(res[::-1])
