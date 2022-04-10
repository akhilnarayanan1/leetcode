class Solution:
    def calPoints(self, ops: List[str]) -> int:
        
        stack = []
        
        for score in ops:
         
            if score == "C":
                last_score = stack.pop()            # Cancel the last entry ❎
            
            elif score == "D":
                last_score = int(stack.pop())
                stack.append(last_score)
                stack.append(last_score * 2)        # Double the last entry and insert ⏫
                
            elif score == "+":
                last_score = int(stack.pop())
                last_last_score = int(stack.pop())
                stack.append(last_last_score)
                stack.append(last_score)            # Don't mess-up with this order 🔢
                stack.append(last_score+last_last_score)
                                                    # Add the last two entries and insert ➕
            else:
                stack.append(int(score))
                                                    # If normal number, add to the stack  📌
                
        
        ans = 0
        
        while stack:
            val = stack.pop()
            ans += val
        
        return ans
            
            
            
        