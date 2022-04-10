import requests
import copy


def parse_robots_txt(URL):
    print("--- parsing robots.txt ---")

    URL = URL + "/robots.txt"
    robots_parameter = []

    page = requests.get(URL)
    #print(page.text)
    page = page.text

    #print(page.split('\n'))

    temp_block_empty = {
        "User-agent": "",
        "Allow": [],
        "Disallow": [],
        "Crawl-delay": 0}

    temp_block = copy.deepcopy(temp_block_empty)
    for line in page.split('\n'):
        if line == "":
            robots_parameter.append(temp_block)
            temp_block = copy.deepcopy(temp_block_empty)
        else:
            temp_para = line.split(': ')
            if temp_para[0] == "User-agent":
                temp_block["User-agent"] = temp_para[1]
            elif temp_para[0] == "Allow":
                temp_block["Allow"].append(temp_para[1])
            elif temp_para[0] == "Disallow":
                temp_block["Disallow"].append(temp_para[1])
            elif temp_para[0] == "Crawl-delay":
                temp_block["Crawl-delay"] = temp_para[1]
    print(robots_parameter)
    return robots_parameter


if __name__ == "__main__":
    parse_robots_txt(URL)
