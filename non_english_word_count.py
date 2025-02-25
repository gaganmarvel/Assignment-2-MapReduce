from mrjob.job import MRJob
import re
import enchant

WORD_RE = re.compile(r"\b\w+\b")
english_dict = enchant.Dict("en_US")

class MRNonEnglishWordCount(MRJob):

    def mapper(self, _, line):
        for word in WORD_RE.findall(line):
            word_lower = word.lower()
            if not english_dict.check(word_lower):  # checking if word is not in English dictionary
                yield word_lower, 1

    def reducer(self, word, counts):
        yield word, sum(counts)

if __name__ == "__main__":
    MRNonEnglishWordCount.run()
