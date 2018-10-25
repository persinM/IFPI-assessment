from websites.resources.data import WEBSITES

def cleanse_data(sites):
    """
    param sites: list of website data

    Checks and updates sites so that 'https' urls are set to
    secure = True and 'http' urls are set to secure = False
    """
    for data_item in sites:
        if data_item['url'][4] == 's':
            data_item['secure'] = True
        else:
            data_item['secure'] = False

if __name__ == "__main__":
    cleanse_data(WEBSITES)
    for site in WEBSITES:
        print(site['url'], site['secure'])
