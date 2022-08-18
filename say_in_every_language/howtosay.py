import googletrans

def howtosay(word='Россия'):

    translator = googletrans.Translator()

    with open('howtosay', 'w', encoding="utf-8") as f:
        for lang in googletrans.LANGUAGES.keys():
            result = translator.translate(word, src='ru', dest=lang)
            f.write('{}: {}'.format(lang, result.text)+'\n')

if __name__ == '__main__':
    howtosay()
