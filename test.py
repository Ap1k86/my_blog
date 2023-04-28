# from typing import List
# strs = ["flower", "flow", "flight"]
#
#
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         if len(strs) == 0:
#             return ''
#         s = strs[0]
#         for i in range(0, len(strs)):
#             while strs[i].find(s) != 0:
#                 s = s[:-1]
#         return s
#
#
# x = Solution()
# print(x.longestCommonPrefix(strs=strs))
