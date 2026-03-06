import sys
from City import City


def generate_output(date: str, paths:list[str]):
    for p in paths:
        city = City(p, date)
        print(city)


# Input must be in the form of: Date (M/D/Y), CSV Path, ... , CSV Path [accepts 1+ CSVs]
if __name__ == '__main__':
    try:
        date = sys.argv[1]
        paths = []
        for i in range (2, len(sys.argv)):
            paths.append(sys.argv[i])
        generate_output(date, paths)
    except:
        print("Arguments invalid")
        sys.exit(1)
