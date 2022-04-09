class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        store = {}
        ans = []
        
        for i in nums:
            store[i] = store.get(i, 0) + 1  # Save occurences in dictionary 🔢
        
        temp = sorted(store.items(), key=lambda x: -x[1])[:k]   
                                            # Sort the keys with respect to occurence in reverse till 'k' 🥇🥈
        for i in temp:
            ans.append(i[0])                # Add the key to the ans
        
        return ans
        