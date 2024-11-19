from deep_translator import GoogleTranslator

text = 'happy coding'

trasnlated = GoogleTranslator('en','pt').translate(text)
print(trasnlated)