from websites.resources.data import WEBSITES

def amend_data(sites):
    for data_item in sites:
        if data_item['domain'][:3] != "www.":
            data_item['domain'] = "www." + data_item['domain']

if __name__ == "__main__":
    amend_data(WEBSITES)
    print(WEBSITES)
