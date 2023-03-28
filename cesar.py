class Cesar():
    list_eng = list(range(ord('a'), ord('z') + 1))
    list_Eng = list(range(ord('A'), ord('Z') + 1))
    list_Rus = list(range(ord('А'), ord('Я') + 1))
    list_rus = list(range(ord('а'), ord('я') + 1))
    list_language = [list_eng, list_Eng, list_rus, list_Rus]
    def __init__(self, symbol, user_key):
        self.symbol = symbol
        self.user_key = user_key

    def STR(self):
        for i in Cesar.list_language:
              if self.symbol in i and ord('А') <= self.symbol <= ord('я'):
                  return i[(i.index(self.symbol) + self.user_key)%32]
              elif self.symbol in i and ord('A') <= self.symbol <= ord('z'):
                  return i[(i.index(self.symbol) + self.user_key)%25]



