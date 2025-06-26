from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s.replace(" ", "")) == Counter(t.replace(" ", ""))
    

def main():
    s_list = ["anagram", "rat"]
    t_list = ["nagaram", "cat"]
    
    sol = Solution()
    
    for s, t in zip(s_list, t_list):
        result = sol.isAnagram(s, t)
        print(f"{s} vs {t} -> {result}")


if __name__ == '__main__':
    main()