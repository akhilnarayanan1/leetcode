class Solution:
  def maxArea(self, height: List[int]) -> int:
        
    size = len(height)
    
    first = 0
    last = size-1
    
    max_water = 0                                            # Initializing Answer 💧
    
    while first < last:                                      # Run until left and right poles crosses
        
      water = (last-first) * min(height[first],height[last]) # Water in current section 💧

      if max_water < water:
        max_water = water                                    # Replace if water volume is high
      
      if height[first] > height[last]:                       # Increase ⬆️ or Decrease ⬇️ the pole if its less than other
        last -= 1
      else:
        first += 1
            
    return max_water                                         # Return Answer 💦
        