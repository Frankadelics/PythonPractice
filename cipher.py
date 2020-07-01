#Ceasarian Cipher
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
MAX_KEY_SIZE = len(SYMBOLS)

def getMode():
    while True:
        print('Do you wish to encrypt or decrypt a message?')
        mode = input().lower()
        if mode in ['encrypt', 'e', 'decrypt', 'd']:
            return mode
        else:
            print('Enter either "encrypt," "e," "decrypt," or "d"')

def getMessage():
    print('Enter you message:')
    return input()

def getKey():
    key = 0
    while True:
        print('Enter the key number (1 - %s)' % MAX_KEY_SIZE)
        key = int(input())
        if key >= 1 and key <= MAX_KEY_SIZE:
            return key

def getTranslatedMessage(mode, message, key):
    if mode[0] == 'd':
        key = -key
    translated = ''

    for symbol in message:
        print("This is what symbols equals: %s" % symbol)
        symbolIndex = SYMBOLS.find(symbol)
        print('This is symbolIndex when first assigned: %s' % symbolIndex)
        if symbolIndex == -1: #Symbol not found in SYMBOLS
            #Just add this symbol without any change
            translated += symbol
        else:
            #Encrypt or decrypt
            symbolIndex += key
            print('This is symbolIndex with the key: %s' % symbolIndex)
            if symbolIndex >= len(SYMBOLS):
                #symbolIndex will occasionally go out bounds. For example, encrypting 'h' with a key of 33
                #will give 66 when symbolIndex is added with the key. This 66 will go beyond the 52 characters
                #that are given in the SYMBOL constant. Therefore, we have to subtract 52 to get the number
                #that will reflect the actual encrypted letter. In this case, 66 - 52 = 14 and will land 'h'
                #to be encrypted as a capital 'O.'
                symbolIndex -= len(SYMBOLS)
                print('This is symbolIndex in first IF: %s' % symbolIndex)
            elif symbolIndex < 0:
                symbolIndex += len(SYMBOLS)
                print('This is symbolIndex in second IF: %s' % symbolIndex)

        translated += SYMBOLS[symbolIndex]
    return translated

mode = getMode()
message = getMessage()
key = getKey()
print('Your translated text is:')
print(getTranslatedMessage(mode, message, key))