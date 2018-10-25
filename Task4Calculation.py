from websites.resources.data import WEBSITES

def data_calculation(sites):
    """
    param sites: list of website data.

    Returns the total of all site values.
    """
    total = 0
    for data_item in sites:
        total += data_item['value']
    return total

if __name__ == "__main__":
    print(data_calculation(WEBSITES))
