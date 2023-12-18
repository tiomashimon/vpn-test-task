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



# def change_html_resource_paths(response, user_site_name, base_url):
#     soup = BeautifulSoup(response, 'html.parser')

#     for link_tag in soup.find_all('link', {'rel': 'stylesheet'}):
#         original_href = link_tag.get('href')
#         if original_href and not original_href.startswith(('http:', 'https:')):
#             link_tag['href'] = f'http://localhost:8000/website/{user_site_name}/{original_href}'

#     for script_tag in soup.find_all('script', {'src': True}):
#         original_src = script_tag['src']
#         if original_src and not original_src.startswith(('http:', 'https:')):
#             script_tag['src'] = f'http://localhost:8000/website/{user_site_name}/{original_src}'

#     for img_tag in soup.find_all('img', {'src': True}):
#         original_src = img_tag['src']
#         if original_src and not original_src.startswith(('http:', 'https:')):
#             img_tag['src'] = f'http://localhost:8000/website/{user_site_name}/{original_src}'

#     return str(soup)


# def load_resource(base_url, resource_path):
#     resource_url = f'{base_url}/{resource_path}'
#     try:
#         response = requests.get(resource_url)
#         response.raise_for_status() 
#         return response.text
#     except requests.RequestException as e:
#         return f'Failed to load resource {resource_path}'