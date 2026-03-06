import sys
from City import City


def generate_output(date: str, paths:list[str]):
    if paths == []:
        print("Please pass a CSV file path")
        sys.exit(1)
    with open("output.txt", "w") as f:
        f.write("------------------------------------------------------------------------------------------- \n"
                + " PM2.5 Data Analysis with Averages for " + date + " and Other Insights from the Complete Sets"
                + "\n-------------------------------------------------------------------------------------------\n")
        cities = []
        for p in paths:
            city = City(p, date)
            cities.append(city)
            f.write(str(city) + "\n")
        f.write("\n---------\n"
                + " Results "
                + "\n---------\n")

        sum_who = 0
        sum_epa = 0
        sum_epa_24hr = 0
        for c in cities:
            sum_who += len(c.readings_exceeding_WHO)
            sum_epa += len(c.readings_exceeding_EPA)
            sum_epa_24hr += len(c.readings_exceeding_EPA_24hr)

        f.write(" Average Number of Readings Exceeding WHO Standards (5.0 ug/m^3): \n" +
                "\t " + str(round(sum_who / len(cities), 3)) + "\n" +
                " Average Number of Readings Exceeding EPA Standards (9.0 ug/m^3): \n" +
                "\t " + str(round(sum_epa / len(cities), 3)) + "\n" +
                " Average Number of Readings Exceeding EPA 24hr Standards (35.0 ug/m^3): \n" +
                "\t " + str(round(sum_epa_24hr / len(cities), 3)) + "\n" +
                "\n -- If any of the above values are significant and non-zero, there is a high probability that \n" +
                "\tthis data indicates a significant health hazard to individuals living in this area.")



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
