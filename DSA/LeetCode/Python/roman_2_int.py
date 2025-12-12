# # MCMXCIV
# class Solution:
#     def romanToInt(self, s: str) -> int:
#         buffer = ""
#         int_val = []
#         roman_value_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
#         print(len(s))
#         if len(s) == 1:
#             return roman_value_dict[s]
        
#         for idx in range(len(s)-1):
#             print(idx, int_val, buffer)

#             if roman_value_dict[s[idx]] < roman_value_dict[s[idx+1]] and idx != 0:
#                 buffer += f"{s[idx]}-"
#             else:
#                 buffer += f"{s[idx]}"

#             print(buffer.rstrip("-"))
#         # return int_val
    
# if __name__ == "__main__":
#     # inp_str = input("Enter string: ")
#     inp_str = "MCMXCIV"
#     result = Solution()
#     print(result.romanToInt(inp_str))