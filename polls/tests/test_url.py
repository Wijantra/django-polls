from selenium import webdriver

def get_links(url):
    """Find all links on page at the given url.
       Return a list of all link addresses, as strings.
    """
    browser = webdriver.Firefox()
    browser.get(url)
    links = []
    link = browser.find_elements_by_tag_name('a')
    for i in link:
        links.append(i.get_attribute('href'))
    browser.close()
    return links


if __name__ == "__main__":
    url = "https://cpske.github.io/ISP/"
    all_url = get_links(url)
    for i in all_url:
        print(i)
