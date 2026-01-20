# MCMXCIV

roman_values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}

class Solution:
    def myRomanToInt(self, s: str) -> int:
        buffer = ""
        int_val = 0
        # print(len(s))
        if len(s) == 1:
            return roman_values[s]
        
        for idx in range(len(s)+1):
            # print(idx, int_val, buffer)
            if idx == len(s)-1:
                buffer += f"{s[idx]}"
                break
            if roman_values[s[idx]] < roman_values[s[idx+1]]:
                buffer += f"{s[idx]}-"
            else:
                buffer += f"{s[idx]}+"

        buffer = buffer.split("+")
        # print(buffer)
        for b in buffer:
            if len(b) > 1:
                char_list = b.split("-")
                int_val += roman_values[char_list[1]] - roman_values[char_list[0]]
            else:
                int_val += roman_values[b]

        # print(int_val)
        return int_val
    
    # Approach 1: Left-to-Right Pass
    def romanToInt_1(self, s: str) -> int:
        total = 0
        idx = 0
        while idx < len(s):
            # print(total)
            if idx < (len(s)-1) and roman_values[s[idx]] < roman_values[s[idx + 1]]:
                total = total + (roman_values[s[idx + 1]] - roman_values[s[idx]])
                idx += 2
            else:
                total += roman_values[s[idx]]
                idx += 1
            
        return total
            

    # Approach 2: Left-to-Right Pass Improved
    def romanToInt_2(self, s: str) -> int:
        ...

    # Approach 3: Right-to-Left pass
    def romanToInt_3(self, s: str) -> int:
        inp_sum = roman_values[s[-1]]

        for i in reversed(range(len(s)-1)):
            # print(s[i],":",roman_values[s[i]])
            if roman_values[s[i]] < roman_values[s[i+1]]:
                inp_sum -= roman_values[s[i]]
            else:
                inp_sum += roman_values[s[i]]
        
        return inp_sum

if __name__ == "__main__":
    # inp_str = input("Enter string: ")
    # inp_str = "MCMXCIV"
    inp_str = "LVIII"
    result = Solution()
    print(result.myRomanToInt(inp_str))
    print("romanToInt_1",result.romanToInt_1(inp_str))
    print("romanToInt_3",result.romanToInt_3(inp_str))