import numpy as np


def ppmi(matrix):

    #行数，列数を取得
    row_num = matrix.shape[0]
    column_num = matrix.shape[1]
    
    result_matrix = np.zeros((row_num, column_num), dtype='float')
    print(result_matrix)

    for i in range(row_num):
        for j in range(column_num):
            log_ij = np.log(matrix[i, j])
            log_ij_sum = np.log(matrix.mean() * row_num * column_num)
            log_i_sum = np.log(matrix.sum(axis=1)[i,0])
            log_j_sum = np.log(matrix.sum(axis=0)[0,j])
            
            temp = log_ij + log_ij_sum - log_i_sum - log_j_sum
            res = max(0, temp)

            result_matrix[i,j] = res 

    return result_matrix
