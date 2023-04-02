import cesar as ces
import wizhener as wiz


def errors_core(user_key, shifr):
    """A function that links the functions of 2 ciphers to find errors in the entered key"""

    if shifr == 'Цезарь':
        prot = ces.Cesar(0, user_key)
        return ces.Cesar.errors(prot)
    else:
        prot = wiz.Wizhener(0, user_key)
        return wiz.Wizhener.find_error(prot)



def key_file(key_file, key):
    """Saving a key to a file"""

    with open(key_file, 'w', encoding="utf-8") as f1:
        f1.write(str(key))

def end_programm(file_3,  file_2, user_key, sfh):
    """The function encrypts the received text by key and cipher type"""

    with open(file_3, 'w', encoding="utf-8") as f3:
        with open(file_2, 'r', encoding="utf-8") as f2:
            for line in f2:
                for symbol in line:
                    if symbol.isalpha() == True:
                        if sfh == 'Цезарь':
                            pt = ces.Cesar(ord(symbol), int(user_key))
                            f3.write(chr(ces.Cesar.STR(pt)))
                        else:
                            pt = wiz.Wizhener(ord(symbol), user_key)
                            f3.write(chr(wiz.Wizhener.STR(pt)))
                    else:
                        f3.write(symbol)
