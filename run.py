from argostranslate import package, translate

import os 


installed_languages = translate.get_installed_languages()

languages = []
for language in installed_languages:
    languages.append(language.code)

aviables_languages = []
for file in os.listdir('dataset'):
    aviables_languages.append(file.split('.')[0])

for language in languages:
    if language == 'en' or language not in aviables_languages:
        continue

    print(language, 'en')
    print('en', language)