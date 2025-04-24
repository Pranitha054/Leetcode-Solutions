class Solution(object):
    def getRow(self, rowIndex):
        traingle=[]
        for i in range(rowIndex+1):
            row=[None]*(i+1)
            row[0],row[i]=1,1
            for j in range(1,i):
                row[j]=traingle[i-1][j-1]+traingle[i-1][j]
            traingle.append(row)
        return traingle[rowIndex]
        