class Solution:
  def gridGame(self, grid: List[List[int]]) -> int:
       
    n = len(grid[0])
    top_prefix = [0] * (n + 1)
    bottom_prefix = [0] * (n + 1)
    
    for i in range(n):
        top_prefix[i + 1] = top_prefix[i] + grid[0][i]
        bottom_prefix[i + 1] = bottom_prefix[i] + grid[1][i]
    
    min_second_robot = float('inf')
    
    for col in range(n):
        top_path = top_prefix[n] - top_prefix[col + 1]
        bottom_path = bottom_prefix[col]
        second_robot = max(top_path, bottom_path)
        min_second_robot = min(min_second_robot, second_robot)
    
    return min_second_robot
