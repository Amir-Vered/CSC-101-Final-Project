import sys
from City import City


def generate_output(path:str):
    city = City(path, 253, 37, 9)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        generate_output(sys.argv[1])
    else:
        print("Invalid Argument Inputs")
        sys.exit(1)
