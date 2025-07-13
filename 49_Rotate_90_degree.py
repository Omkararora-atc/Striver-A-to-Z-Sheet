def rotate(matrix):
    for i in range(len(matrix)):
        for j in range(i+1,len(matrix)):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    for i in range(len(matrix)):
        low=0
        high=len(matrix)-1
        while low<high:
            matrix[i][low],matrix[i][high]=matrix[i][high],matrix[i][low]
            low+=1
            high-=1
    return matrix
# ### Example usage:
if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    rotated_matrix = rotate(matrix)
    print("Rotated matrix:")
    for row in rotated_matrix:
        print(row)
