import requests

def parsing(url):
    try:
        prs = requests.get(url)

        with open("my_programs/parser_site/parsed.txt", mode="w", encoding="utf-8") as txt:
            txt.write(prs.text)
            
    except:
        return "Sayt topilmadi!"

