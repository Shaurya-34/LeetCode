class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        check = {}
        if not strs:
            return []
        for string in strs:
            signature = tuple(sorted(Counter(string).items()))
            if signature in check:
                check[signature].append(string)
            else:
                check[signature] = [string]
        return list(check.values())