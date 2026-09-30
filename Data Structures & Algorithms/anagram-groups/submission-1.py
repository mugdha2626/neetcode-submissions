class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #have a hashmap: [arr of letters a-z] -> list of anagrams
        ans = collections.defaultdict(list)

        mapping = {}

        for word in strs:
            arr = [0] * 26
            for char in word:
                arr[ord(char) - ord("a")] += 1
            ans[tuple(arr)].append(word)
        return list(ans.values())
