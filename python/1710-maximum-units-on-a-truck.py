class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: -x[1])              # Reverse sort by second index [1] 

        cur_size = 0
        max_units = 0
        
        for num_box, unit in boxTypes:
            rem_size = truckSize - cur_size             # Decreasing remaing size ⬇️
            max_units += unit * min(rem_size, num_box)  # Maximum units covered in truck 
            cur_size += min(rem_size, num_box)          # Current size is increasing ⬆️
        
        return max_units