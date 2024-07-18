


def calculate_pixel_accuracy(grid_one, grid_two):
    total_elements = 0
    matching_elements = 0

    #If the predicted size of the grid differs, then accuracy is 0
    if len(grid_one) != len(grid_two) or (len(grid_one[0]) != len(grid_two[0])):
        return 0

    for row_idx in range(len(grid_one)):
        for col_idx in range(len(grid_one[row_idx])):
            total_elements += 1
            if grid_one[row_idx][col_idx] == grid_two[row_idx][col_idx]:
                matching_elements += 1
    return (matching_elements / total_elements) * 100