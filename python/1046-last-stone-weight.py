class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while len(stones) > 1:
            stones.sort()           # Sort the list every time ⛓️
            
            last = len(stones) - 1 
            second_last = last - 1  # Set last and second_last element 🥇🥈
            
            stones.append(abs(stones[last] - stones[second_last]))
                                    # Append the absoulte difference to the end ➕
                
            stones.pop(last)
            stones.pop(second_last) # Pop these ❎
            
            last -= 2
            second_last -= 2        # Decrease these as well ⬇️
            
        return stones[0]            # Last element is the answer ✅
