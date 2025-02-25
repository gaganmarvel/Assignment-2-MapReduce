from mrjob.job import MRJob
import re

WORD_RE = re.compile(r"\b\w+\b")  # Extract words using regex

class MRWordCount(MRJob):

    def mapper(self, _, line):
        line = line.strip().lower()

        # splitting the line into words
        words = WORD_RE.findall(line)

        # emitting each word with count 1
        for word in words:
            yield word, 1

    def reducer(self, word, counts):
        # sum up occurrences of each word
        yield word, sum(counts)

if __name__ == "__main__":
    MRWordCount.run()
