class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result

    def decode(self, s: str) -> List[str]:
        result =[]
        i=0
        while i < len(s):
            j=i
            while s[j] != "#"  and j < len(s):
                j+=1
            length_str = s[i:j]
            if length_str == "":
                break
            length = int(length_str)

            string_start = j+1
            string_end = string_start + length
            result.append(s[string_start:string_end])
            i=string_end
        return result
