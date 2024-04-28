#      *   
#     * *
#    * * *
#   * * * *
#  * * * * *
def triangle(size: int) -> None:
    if size % 2 == 0:
        raise ValueError(f"size must be odd, was {size}")

    for i in range(size):
        print(" " * (size - i - 1) + "* " * (i + 1))
    
if __name__ == "__main__":
    triangle(5)