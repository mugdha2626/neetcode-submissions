class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Map character count tuple -> list of anagrams
        ans = collections.defaultdict(list)

        for word in strs:
            #store of all the letters
            count = [0] * 26
            
            #for each char we will store the the freq
            for char in word:
                count[ord(char) - ord('a')] += 1
            
            #the same freq are grouped together and added to the list
            ans[tuple(count)].append(word)
            #tuples can be used a key in a hashmap.

        return list(ans.values())

