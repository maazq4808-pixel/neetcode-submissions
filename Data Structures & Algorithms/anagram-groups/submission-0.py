class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for i in strs:
            label = "".join(sorted(i))
            if label not in seen:
                seen[label] = []
            seen[label].append(i)
        return list(seen.values())
        