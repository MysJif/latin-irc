from googletrans import Translator

trans = Translator()

text = "hello world, please kill me"

result = trans.translate(text, dest='la')

print(text)
print(result.text)
