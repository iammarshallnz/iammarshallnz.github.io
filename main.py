from pyscript import document
import timeit
import random
    
def randomGrid(col, row) -> list:
    """Generate a random grid of integers."""
    return [
        [random.randint(1, 100) for _ in range(col)]
        for _ in range(row)
    ]

def solution(maximum_product):
    """
    Generate a random grid of integers and find maximun product of 4 intergers in a row, column, or diagonal.
    """
    col = 600
    row = 600
    grid = randomGrid(col, row)
    max_product = 0
    # row 
    
    for i in range(row):
        for j in range(col - 3):
            product = grid[i][j] * grid[i][j + 1] * grid[i][j + 2] * grid[i][j + 3]
            if product > max_product:
                max_product = product

    # column
    for j in range(col):
        for i in range(row - 3):
            product = grid[i][j] * grid[i + 1][j] * grid[i + 2][j] * grid[i + 3][j]
            if product > max_product:
                max_product = product

    # diagonal top-left to bottom-right
    for i in range(row - 3):
        for j in range(col - 3):
            product = grid[i][j] * grid[i + 1][j + 1] * grid[i + 2][j + 2] * grid[i + 3][j + 3]
            if product > max_product:
                max_product = product
    
    # diagonal top-right to bottom-left
    for i in range(row - 3):
        for j in range(3, col):
            product = grid[i][j] * grid[i + 1][j - 1] * grid[i + 2][j - 2] * grid[i + 3][j - 3]
            if product > max_product:
                max_product = product
    maximum_product = max_product
    return

def translate_english(event):
    
    
    output_div = document.querySelector("#output")
    max_product = 0
    time_taken = timeit.timeit(lambda: solution(max_product), number=1)
    output_div.innerText = f"{max_product}" + f" in {time_taken:.2f} seconds \n"
