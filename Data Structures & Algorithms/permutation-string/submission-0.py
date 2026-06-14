class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        
        def char_count(s):
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] +=1
            
            return count


        s1_count = char_count(s1)
        window_count = char_count(s2[:len(s1)])

        for i in range(len(s2) - len(s1)):
            if window_count == s1_count:
                return True
            
            window_count[ord(s2[i]) - ord('a')] -= 1
            window_count[ord(s2[i + len(s1)]) - ord('a')] += 1

        
        return window_count == s1_count
        