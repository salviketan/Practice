# MCMXCIV
class Solution:
    def romanToInt(self, s: str) -> int:
        buffer = ""
        int_val = 0
        roman_value_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        # print(len(s))
        if len(s) == 1:
            return roman_value_dict[s]
        
        for idx in range(len(s)+1):
            # print(idx, int_val, buffer)
            if idx == len(s)-1:
                buffer += f"{s[idx]}"
                break
            if roman_value_dict[s[idx]] < roman_value_dict[s[idx+1]]:
                buffer += f"{s[idx]}-"
            else:
                buffer += f"{s[idx]}+"

        buffer = buffer.split("+")
        # print(buffer)
        for b in buffer:
            if len(b) > 1:
                char_list = b.split("-")
                int_val += roman_value_dict[char_list[1]] - roman_value_dict[char_list[0]]
            else:
                int_val += roman_value_dict[b]

        # print(int_val)
        return int_val
if __name__ == "__main__":
    # inp_str = input("Enter string: ")
    inp_str = "MCMXCIV"
    result = Solution()
    print(result.romanToInt(inp_str))