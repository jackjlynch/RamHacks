from foreignArticleFinder.models import Language, WordList, Article

class Reader():
    def __init__(self, language):
        self.language = language
        self.wordList = language.wordList


    def get_stats(self, article, range=None):
        if not range is None:
            words = self.wordList.get_words()[0:range]
        else:
            words = self.wordList.get_words()

        foreignChars = ""
        known = 0
        if not self.language.latinAlphabet:
            for letter in article.text:
                if letter.lower() not in "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*\n\t(),'\"。 ·，“”（）：、.><,/\\[；]{}|`~-=_+《》:‘—"\
                 and letter not in words:
                    foreignChars += letter
                else:
                    known += 1

        else:
            for word in article.text.split(" "):
                #support for languages with spaces not yet implemented
                pass

        if article.wordcount is None:
            article.wordcount = known + len(foreignChars)

        return foreignChars