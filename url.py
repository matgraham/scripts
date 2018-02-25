
def get_text(url):
    html = urlopen('http://www.indeed.com/viewjob?jk=d88f3bb95f1a4466')
    site = html.read()
    soup = BeautifulSoup(site, 'html.parser')
    for i in soup.find_all('script'):
        i.decompose()
    for i in soup.find_all('style'):
        i.decompose()
    for i in soup.find_all('noscript'):
        i.decompose()
    for i in soup.find_all('div'):
        i.decompose()
    for i in soup.find_all('meta'):
        i.decompose()
    text = soup.get_text()
        
    #breaking text into lines and removeing excess
    lines = [line.strip() for line in text.splitlines()]

    #removing blank lines
    lines = [l for l in lines if l != '']

    #concatenate into one string
    cleaned = ''.join(lines)
    return(cleaned)

