from typing import List


class Matrix:
    def SpiralOrder(self, matrix: List[List[int]])-> List[int]:
        row = len(matrix)
        col = len(matrix[0])
        n = row*col  # number of elements in the matrix
        l, t = 0, 0
        r, b = col, row
        collect = []

        # repeat the following 4 steps until all the elements are collected
        while len(collect) < n:
            # Step1: L to R
            if t < b and l < r:
                for i in range(l,r):
                    collect.append(matrix[t][i])

                t += 1

            # Step2: T to B
            if t < b and l < r:
                for i in range(t,b):
                    collect.append(matrix[i][r-1])

                r -= 1

            # Step3: R to L
            if t < b and l < r:
                for i in range(r-1,l-1,-1):
                    collect.append(matrix[b-1][i])

                b -= 1

            # Step4: B to T
            if t < b and l < r:
                for i in range(b-1,t-1,-1):
                    collect.append(matrix[i][l])

                l += 1

        return collect
    
    def diagonalSum(self, mat: List[List[int]]) -> int:
        summ = 0
        for i in range(len(mat)):
            summ += mat[i][i]
            if i != len(mat)-1-i:
                summ += mat[i][len(mat)-1-i]
        return summ

    def countNegatives(self, grid: List[List[int]]) -> int:
        j = len(grid[0])-1
        count = 0
        for row in grid:
            while j >= 0 and row[j]<0:
                j -= 1
            
            count += len(row)-1-j

        return count

    def countNegatives(self, grid: List[List[int]]) -> int:
        j = len(grid[0])-1
        count = 0
        for row in grid:
            while j >= 0 and row[j]<0:
                j -= 1
            
            count += len(row)-1-j

        return count



if __name__ == "__main__":
    matrix = [
        [1],
        [5],
        [9],
        [13]
    ]
    print(Matrix().SpiralOrder(matrix))