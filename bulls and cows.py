# https://leetcode.com/problems/bulls-and-cows/

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = sum(list(map(lambda x,y: 1 if x==y else 0, secret, guess)))
        cows = 0
        counts_secret = {}
        counts_guess = {}
        for val in secret:
            counts_secret[val] = counts_secret.get(val, 0) + 1

        for val in guess:
            counts_guess[val] = counts_guess.get(val, 0) + 1

        for key, value in counts_secret.items():
            cows += min(value, counts_guess.get(key, 0))

        cows -= bulls

        return f'{bulls}A{cows}B'