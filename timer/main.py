
from pyscript import document
import time
import random
import asyncio

def randomGrid(col, row) -> list:
    """Generate a random grid of integers."""
    return [
        [random.randint(1, 100) for _ in range(col)]
        for _ in range(row)
    ]

def solution(grid, col, row) -> tuple:
    """
    Generate a random grid of integers and find maximun product of 4 intergers in a row, column, or diagonal.
    """
    
    max_product : int = 0
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
    return max_product, grid



    

global running
running = False
async def update(current_count, wall_clock):
    output_div = document.querySelector("#output")
    output_div.innerText = f"Current time through calculations {current_count} seconds, wall clock time: {wall_clock:.2f} seconds"

async def start() -> None:
    print("Starting calculations...")
    global running
    running = True
    current_count = 0
    wall_clock = 0
    col = 2000
    row = 2000

    grid = randomGrid(col, row)
    while running:
        print("Calculating...")
        
        start = time.time()
        solution(grid, col, row)
        wall_clock += time.time() - start
        current_count += 1
    
        await update(current_count, wall_clock)
        await asyncio.sleep(0.01)

async def stop() -> None:
    global running
    running = False


