class Wizhener():
    """The class encrypts the incoming text with a key"""

    user_key_list = []
    list_eng = list(range(ord('a'), ord('z') + 1))
    list_Eng = list(range(ord('A'), ord('Z') + 1))
    list_Rus = list(range(ord('А'), ord('Я') + 1))
    list_rus = list(range(ord('а'), ord('я') + 1))
    list_language = [list_eng, list_Eng, list_rus, list_Rus]
    sum_index = 0

    def __init__(self, symbol, user_key):
        self.symbol = symbol
        self.user_key = user_key

    def find_error(self):
        """The function checks if the key matches the requirements"""

        for i in self.user_key:
            if i.isalpha() == False or i.istitle() == True:
                return ('Ошибка')
            else:
                Wizhener.user_key_list.append(i)
        return False

    def STR(self):
        """The function encrypts the text and writes it to a file"""

        for i in Wizhener.list_language:
            if self.symbol in i and ord('А') <= self.symbol <= ord('я'):
                return i[(i.index(self.symbol) +
                          abs((ord(Wizhener.user_key_list[Wizhener.sum_index%len(Wizhener.user_key_list)])
                               -ord('а')))) % 33]
            elif self.symbol in i and ord('A') <= self.symbol <= ord('z'):
                return i[(i.index(self.symbol) +
                          abs((ord(Wizhener.user_key_list[Wizhener.sum_index%len(Wizhener.user_key_list)])
                               -ord('a')))) % 26]

