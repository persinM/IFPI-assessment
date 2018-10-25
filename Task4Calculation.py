from websites.resources.data import WEBSITES

def data_calculation(sites):
    total = 0
    for data_item in sites:
        total += data_item['value']
    return total

if __name__ == "__main__":
    print(data_calculation(WEBSITES))
