from websites.resources.data import WEBSITES


def find_data(sites, value):
    """
    param sites: list of website data;
    param value: integer;

    Returns a list of all the data in sites that has a value
    greater than or equal to the inputted value.
    """
    new_data = []
    for data_item in sites:
        if data_item['value'] >= value:
            new_data.append(data_item)
    return new_data

if __name__ == "__main__":
    print(find_data(WEBSITES, 4))
