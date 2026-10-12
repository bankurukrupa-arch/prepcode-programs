class Solution:
    def isPalindrome(self, word: str) -> bool:
        word = "racecar"
        if word == word[::-1]:
            print(True)
        else:
            print(False)    