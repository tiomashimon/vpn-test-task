from urllib.parse import urlparse
from bs4 import BeautifulSoup



def get_base_url(url):
    parsed_url = urlparse(url)
    base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
    return base_url


def change_html_href(response, user_site_name, base_url):
    soup = BeautifulSoup(response.text, 'html.parser')
    for a_tag in soup.find_all('a'):
        original_href = a_tag.get('href')

        href_base_url = get_base_url(original_href)
        if href_base_url == '://':
            original_href = base_url + original_href
        if original_href and base_url in original_href:
            new_href = f'http://localhost:8000/website/{user_site_name}/{original_href}'
            a_tag['href'] = new_href
    return str(soup)