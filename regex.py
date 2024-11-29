import requests, re
link = "https://auto.bazos.cz"
hlavni_stranka = requests.get(link)
vyraz = r"/inzerat/[A-z0-9/-]*"
odkazy = re.findall(vyraz, hlavni_stranka.text)
for odkaz in odkazy:
    print(link + odkaz)
    stranka = requests.get(link + odkaz)
    zkratky = re.findall(r"\d+\.?\s?\d+\s?km", stranka.text)
    for zkratka in zkratky:
        print(zkratka)
