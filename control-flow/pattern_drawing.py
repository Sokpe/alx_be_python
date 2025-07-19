def get_pattern_size():
    while True:
        try:
            size = int(input("Enter the size of the pattern: "))
            if size > 0:
                return size
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

def draw_pattern(size):
    row = 0
    while row < size:
        for _ in range(size):
            print("*", end="")
        print()
        row += 1

def main():
    size = get_pattern_size()
    draw_pattern(size)

if __name__ == "__main__":
    main()
