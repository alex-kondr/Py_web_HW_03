CYRILLIC = ('а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 
            'і', 'ї', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 
            'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 
            'ы', 'ь', 'э', 'ю', 'я')

LATIN = ('a', 'b', 'v', 'g', 'd', 'e', 'e', 'zh', 'z', 'i', 
         'i', 'yi', 'y', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 
         's', 't', 'u', 'f', 'h', 'ts', 'ch', 'sh', 'sch', 
         '', 'y', '', 'e', 'yu', 'ya')

TRANSLIT_DICT = {}

for c, l in zip(CYRILLIC, LATIN):
    TRANSLIT_DICT[ord(c)] = l
    TRANSLIT_DICT[ord(c.upper())] = l.upper()

def normalize(txt):
    txt = txt.translate(TRANSLIT_DICT)
    txt_out = ""

    for char in txt:
        if not char.isdigit() and not char.isalpha():
            char = "_"

        txt_out += char

    return txt_out

