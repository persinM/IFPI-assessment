from websites.resources.data import WEBSITES

def find_data(sites, key):
    new_data = []
    for data_item in sites:
        if data_item['value'] >= key:
            new_data.append(data_item)
    return new_data

if __name__ == "__main__":
    print(find_data(WEBSITES, 4))
