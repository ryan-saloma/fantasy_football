
# -----------------------------------------------------------
# Source: scrape_player_data.ipynb
# Author: RS
# Date: 2024-10-02
# Purpose: scrape player section titles and tables from pro-football-reference.com
# -----------------------------------------------------------

# Test getting tables from player pages
base_path = 'scraping/player_pages/'

# Get all h2 tags from the page
def get_headings(page):
    soup = BeautifulSoup(page, 'html.parser')
    h2_tags = soup.find_all('h2')
    headings = []
    for h2 in h2_tags:
        headings.append(h2.get_text())
    return headings

# Get the headings for a QB
player_page_name = 'AlleJo02.htm'
tables_qb = pd.read_html(base_path + player_page_name)
headers_qb = get_headings(open(base_path + player_page_name, 'r').read())
print(headers_qb)

# Repeat for a WR and RB to get all relevant headings
player_page_name = 'SmitDe07.htm'
tables_wr = pd.read_html(base_path + player_page_name)
headers_wr = get_headings(open(base_path + player_page_name, 'r').read())
print(headers_wr)

player_page_name = 'McCaCh01.htm'
tables_rb = pd.read_html(base_path + player_page_name)
headers_rb = get_headings(open(base_path + player_page_name, 'r').read())
print(headers_rb)

# Save concatenated headers
headers = list(set(headers_qb + headers_wr + headers_rb))
headers = pd.Series(headers)
headers.to_csv('scraping/sections.csv', index=False)
