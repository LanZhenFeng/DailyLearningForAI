#
# @lc app=leetcode.cn id=459 lang=python3
#
# [459] 重复的子字符串
#

# @lc code=start
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # 暴力求解
        '''
        129/129 cases passed (114 ms)
        Your runtime beats 24.92 % of python3 submissions
        Your memory usage beats 41.14 % of python3 submissions (16.5 MB)
        '''
        # for size in range(1, len(s) // 2+1):
        #     pattern = s[:size]
        #     i = 1
        #     while s[i*size:i*size+size] == pattern:
        #         i += 1
        #     if i*size == len(s):
        #         return True
        # return False
        
        # 移动匹配 find底层由C实现，要比用Python实现KMP算法快的多
        '''
        129/129 cases passed (34 ms)
        Your runtime beats 95.75 % of python3 submissions
        Your memory usage beats 33.52 % of python3 submissions (16.6 MB)
        '''
        # ns = ''.join([s, s])[1:-1]
        # res = ns.find(s)
        # return False if res == -1 else True

        # _next = [0] * len(s)
        # for i in range(1, len(s)):
        #     lens = _next[i-1]
        #     while lens and s[i] != s[lens]:
        #         lens = _next[lens-1]
        #     if s[i] == s[lens]:
        #         _next[i] = lens + 1
        
        # j = 0
        # for i in range(len(ns)):
        #     while j and ns[i] != s[j]:
        #         j = _next[j-1]
        #     if ns[i] == s[j]:
        #         j += 1
        #         if j == len(s):
        #             return True
        # return False

        # KMP + 推导
        '''
        129/129 cases passed (77 ms)
        Your runtime beats 49.52 % of python3 submissions
        Your memory usage beats 5.91 % of python3 submissions (16.9 MB)
        '''
        if len(s) == 0:
            return False
        _next = [0] * len(s)
        for i in range(1, len(s)):
            lens = _next[i-1]
            while lens and s[i] != s[lens]:
                lens = _next[lens-1]
            if s[i] == s[lens]:
                _next[i] = lens + 1

        if _next[-1] != 0 and len(s) % (len(s) - _next[-1]) == 0:
            return True

        return False

# @lc code=end

