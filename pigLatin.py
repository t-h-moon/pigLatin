def findFirstVowel(word):
    for n in range(0, len(word)):
        char = word[n]
        if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' or char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U':
            return n

    return -1


def convertToPigLatin(word):
    index = findFirstVowel(word)
    if index == -1:
        print(word)

    elif index == 0:
        print(word[1:] + word[index:1] + 'way', end='')

    else:
        print(word.lower()[index:] + word[0:index] + 'ay', end='')


def main():
    word = input('input word:')
    reverse('hello')
    while word != 'done':
        word = word.lower()
        convertToPigLatin(word)
        print('\n')
        word = input('Another word:')


main()

# reverse:
# input word:done
# >>> s = 'abc'
# >>> s[::-1]
# 'cba'
