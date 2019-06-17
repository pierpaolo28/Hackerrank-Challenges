# Complete the hourglassSum function below.
def hourglassSum(arr):
    listres = []
    # Looping though all the values that can be included in the hourglass
    for i in range(0,4):
        for j in range(0,4):
            # Adding all the values that form an hourglass
            oneres = arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
            # Making a list with all sums of all the hourglass in the matrix
            listres.append(oneres)
    # returning the maximum value of the sums of all the hourglasses in the matrix
    return max(listres)