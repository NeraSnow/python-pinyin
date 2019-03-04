from pypinyin import pinyin, lazy_pinyin, Style

source = open('source.txt', 'r')
output = open('output.txt', 'w')



word = source.readline()
while word != '': 
    output.write(word)
    pinyins = lazy_pinyin(word, errors = 'ignore', style=Style.TONE)
    for onepinyin in pinyins:
        output.write(onepinyin)
    output.write('\n')
    word = source.readline()

