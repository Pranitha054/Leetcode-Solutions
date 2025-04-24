class Solution(object):
    def generate(self, numRows):
        triangle = []  # Initialize an empty list to store the rows of the triangle
        
        for i in range(numRows):
            row = [None] * (i + 1)
            
            row[0], row[i] = 1, 1
            
            for j in range(1, i):
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]
            
            triangle.append(row)
        
        return triangle
                
        