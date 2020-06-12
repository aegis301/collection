test_data = ["1912", "1929", "1913-1923",
             "(1951)", "1994", "1934",
             "c. 1915", "1995", "c. 1912",
             "(1988)", "2002", "1957-1959",
             "c. 1955.", "c. 1970's",
             "C. 1990-1999"]

bad_chars = ["(", ")", "c", "C", ".", "s", "'", " "]


def strip_characters(string):
    for char in bad_chars:
        string = string.replace(char, "")
    return string


stripped_test_data = ['1912', '1929', '1913-1923',
                      '1951', '1994', '1934',
                      '1915', '1995', '1912',
                      '1988', '2002', '1957-1959',
                      '1955', '1970', '1990-1999']

processed_test_data = []

# checks if "-" is in the string -> range or Not
for i in stripped_test_data:
    if "-" in i:
        splits = i.split("-")
        avg = (int(splits[0])/int(splits[1]))/2
        processed_test_data.append(round(avg))
    else:

       # if date is a range
        # split string into two strings
        # convert to integer, avearge them
        # round
       #
       # if the date is not a range
     #   convert it to integer
