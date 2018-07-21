import bs4, requests, os, pathlib


url = 'https://globoesporte.globo.com/futebol/copa-do-mundo/'

html = requests.get(url).text

soup = bs4.BeautifulSoup(html, 'html.parser')

divs = soup.find_all('div', {'class' : 'jogador-escudo' })

imgs = []

for div in divs:
    imgs.append({ 'nome': (div.findChildren('img')[0]).get('alt'), 'src' : (div.findChildren('img')[0]).get('src')})

print(imgs)

for img in imgs:
    foriginal = requests.get(img['src'])
    if foriginal.status_code == 200:
        fcopia = open("{1}/static/show/img/{0}.png".format(img['nome'], pathlib.Path(os.path.dirname(os.path.abspath(__file__))).parent), 'wb')
        for chunk in foriginal.iter_content(100000):
            fcopia.write(chunk)
        fcopia.close()

