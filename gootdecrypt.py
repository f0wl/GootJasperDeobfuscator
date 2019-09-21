import sys
import re
import base64
  
def decodeJS(String):

    print('[*] Decoded String\n')
    first = 0
    f = open(filename, "r")

    if f.mode == 'r':
        fl = f.readlines()
        assembledString = ''
        for x in fl:
            if x == '\n':
                continue
            if "\" \"" in x:
                continue
            if "new Array()" in x:
                continue
            if "push" in x:
                arrayname,dirtystr = x.split('.push("')
                cleanstr = dirtystr.strip('");\n')
                if first is 0:
                    assembledString += cleanstr
                    first = 1
                elif first is 1:
                    assembledString = assembledString + ' ' + cleanstr
            if "= \"\"" in x:
                break
        i, num0, num1, num2 = 0, 2, 2, 1
        #i = 0
        #num0 = 2
        #num1 = 2
        #num2 = 1
        finalString = ''
        while i < len(assembledString):
            if num1 != num0:
                num1 += num2
            elif num1 == num0:
                finalString += assembledString[i]
                num1 = num2
            i += 1
        print(finalString)

        print('\n[*] Decoded Base64\n')

    head,b64ps,tail = finalString.split('\'')
    result = base64.b64decode(b64ps)
    print(result)
    return


def decodeVBS(String):

    print('[*] Decoded String\n')

    f = open(filename, "r")
    
    if f.mode == 'r':
        fl = f.readlines()
        assembledString = ''
        for x in fl:
            inte = 0
            if x == '\n':
                continue
            name,inte = x.split(' ')
            inte = inte.strip('\n')
            if name == 'Function':
                continue
            if name == 'ffhvgwa':
                char = str(chr(int(inte) - 302))
                assembledString += char
            if name == 'End':
                print(assembledString)
                break

    print('\n[*] Decoded Base64\n')

    head,b64ps,tail = assembledString.split('\'')
    result = base64.b64decode(b64ps)
    print(result)
    return   

print('\n  _____          __  __    _ __    ___                        __          ')          
print(' / ___/__  ___  / /_/ /__ (_) /_  / _ \\___ __________ _____  / /____  ____')
print('/ (_ / _ \\/ _ \\/ __/  \'_// / __/ / // / -_) __/ __/ // / _ \\/ __/ _ \\/ __/')
print('\\___/\\___/\\___/\\__/_/\\_\\/_/\\__/ /____/\\__/\\__/_/  \\_, / .__/\\__/\\___/_/   ')   
print('                                                 /___/_/                  ')  
print('Gootkit/Jasper Decryptor - Marius Genheimer, 2019 - https://dissectingmalwa.re')
print('')

filename = sys.argv[1]
filen,suffix = filename.split('.')

if suffix == 'vbs':
    decodeVBS(filename)
elif suffix == 'js':
    decodeJS(filename)