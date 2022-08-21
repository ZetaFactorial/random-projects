import googletrans

def in_every_language(phrase='I love you', fromlang='en', filename='in_every_language'):

    translator = googletrans.Translator()

    with open(filename, 'w', encoding="utf-8") as file:
        for lang in googletrans.LANGCODES:
            result = translator.translate(phrase, src=fromlang, dest=lang)
            file.write(f'{lang}: {result.text}\n')

if __name__ == '__main__':
    in_every_language()
