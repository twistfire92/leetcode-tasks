# https://leetcode.com/problems/integer-to-english-words/

class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        units = [
            '',
            'One',
            'Two',
            'Three',
            'Four',
            'Five',
            'Six',
            'Seven',
            'Eight',
            'Nine',
        ]
        teens = [
            'Ten',
            'Eleven',
            'Twelve',
            'Thirteen',
            'Fourteen',
            'Fifteen',
            'Sixteen',
            'Seventeen',
            'Eighteen',
            'Nineteen',
        ]
        tens = [
            '',
            '',
            'Twenty',
            'Thirty',
            'Forty',
            'Fifty',
            'Sixty',
            'Seventy',
            'Eighty',
            'Ninety',
        ]
        billions, num = divmod(num, 1_000_000_000)
        millions, num = divmod(num, 1_000_000)
        thousands, num = divmod(num, 1_000)

        def int_to_words(number, postfix=None):
            words = []
            hundred, number = divmod(number, 100)
            ten, number = divmod(number, 10)
            if hundred:
                words.append(units[hundred])
                words.append("Hundred")
            if ten == 1:
                words.append(teens[number])
            elif ten > 1:
                words.append(tens[ten])
                if number:
                    words.append(units[number])
            else:
                if number:
                    words.append(units[number])
            if postfix:
                words.append(postfix)
            return words

        parts = []
        if billions:
            parts.extend(int_to_words(billions, "Billion"))

        if millions:
            parts.extend(int_to_words(millions, "Million"))

        if thousands:
            parts.extend(int_to_words(thousands, "Thousand"))

        if num:
            parts.extend(int_to_words(num))

        return ' '.join(parts)
            

if __name__ == '__main__':
    num = 50868
    print(Solution().numberToWords(num))
