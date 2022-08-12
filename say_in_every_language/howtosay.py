import googletrans

def howToSay(wordToTranslate='Россия'):

    translator = googletrans.Translator()

    with open('howtosay', 'w', encoding="utf-8") as f:
        for lang in googletrans.LANGUAGES.keys():
            result = translator.translate(wordToTranslate, src='ru', dest=lang)
            f.write('{}: {}'.format(lang, result.text)+'\n')

if __name__ == '__main__':
    howToSay()