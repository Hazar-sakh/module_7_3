class WordsFinder:

    def __init__(self, *files):
        self.file_names = [*files]

    def get_all_words(self):
        words = []
        for i in self.file_names:
            with open(i, encoding='utf-8') as file:
                for line in file:
                    line = line.lower()
                    line = line.split()
                    listOfPunct = [',', '.', '=', '!', '?', ';', ':', ' - ']
                    for k in listOfPunct:
                        for j in line:
                            if k in j:
                                j = list(j)
                                j.remove(k)
                                j = ''.join(j)
                                line.append(j)
                                line.remove(line[line.index(j) - 1])
                    for word in line:
                        words.append(word)
        all_words = dict(zip(self.file_names, [words]))
        return all_words

    """
    Вариант 1
    """

    # def find(self, word):
    #     lOw = self.get_all_words()
    #     lOw = list(*lOw.values())
    #     word = word.lower()
    #     for i in lOw:
    #         if i == word:
    #             j = int(lOw.index(word) + 1)
    #             f_d = {f'{"".join(self.file_names)}': j}
    #             return f_d
    #
    # def count(self, word):
    #     lOw = self.get_all_words()
    #     lOw = list(*lOw.values())
    #     word = word.lower()
    #     c = 0
    #     for i in lOw:
    #         if i == word:
    #             c += 1
    #     c_d = {f'{"".join(self.file_names)}': c}
    #     return c_d

    """
    Вариант 2
    """

    def find(self, word):
        f_d = {}
        word = word.lower()
        for name, words in self.get_all_words().items():
            if word in words:
                f_d[name] = words.index(word)+1
        return f_d

    def count(self, word):
        c_d = {}
        word = word.lower()
        for name, words in self.get_all_words().items():
            c_d[name] = words.count(word)
        return c_d


if __name__ in '__main__':
    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words())  # Все слова
    print(finder2.find('TEXT'))  # 3 слово по счёту
    print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
