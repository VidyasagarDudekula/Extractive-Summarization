from collections import defaultdict
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
import re
import os
import math
content_file_path = os.path.abspath(os.getcwd()) + '/data/content.txt'
stopwords = stopwords.words('english')
# nltk.download('wordnet')


class MyException(Exception):
    """This is a custom exception."""
    def __init__(self, message):
        super().__init__(message)


class Summary():
    def __init__(self):
        self.content = ""
        self.cleaned_text = ""
        self.sent_count = ""
        self.__doc_token_freq = None
        self.__sent_token_freq = None
        self.__sent_filtered_tokens = None
        self.__sentences = None
        self.__scored_Sentences = None
        self.__stemmer = None
        self.__lemmatizer = None
        self._load_data()

    def _get_sentences(self, text):
        sentences = sent_tokenize(text)
        return sentences
    
    def _load_data(self):
        self.__stemmer = PorterStemmer()
        self.__lemmatizer = WordNetLemmatizer()

    def _clean_content(self, text):
        text = re.sub(r"\s+", " ", text)
        text = re.sub(r'"', " ", text)
        text = text.replace(" . ", ". ")
        text = text.replace(".. ", ". ")
        text = re.sub(r"\s+", " ", text)
        return text

    def _valid_token(self, token):
        return len(token)>1 and token.isalnum() and token not in stopwords
    
    def _modify_token(self, token):
        token = self.__stemmer.stem(token)
        return self.__lemmatizer.lemmatize(token)

    def _filter_tokens(self, doc_tokens):
        return [self._modify_token(token.lower().strip()) for token in doc_tokens if self._valid_token(token)]

    def _build_freq_dictionary(self):
        self.__doc_token_freq = defaultdict(int)
        self.__sent_token_freq = defaultdict(int)

        for ind, sent in enumerate(self.__sent_filtered_tokens):
            current = []
            for token in sent:
                self.__sent_token_freq[(ind, token)] += 1
                if token in current:
                    continue
                self.__doc_token_freq[token] += 1
                current.append(token)

    def _get_corpus(self):
        sent_tokens = [word_tokenize(sent) for sent in self.sentences]
        self.__sent_filtered_tokens = [self._filter_tokens(doc_tokens) for doc_tokens in sent_tokens]
        self._build_freq_dictionary()

    def _cal_sent_score(self):
        self.__doc_score = []
        for ind, sent in enumerate(self.__sent_filtered_tokens):
            total_score = 0
            for token in sent:
                tf = self.__sent_token_freq[(ind, token)]/len(sent)
                idf = math.log(len(self.sentences)/(self.__doc_token_freq[token] + 1))
                total_score += (tf * idf)
            self.__doc_score.append((ind, total_score))
        self.__scored_Sentences = []
        for ind, score in self.__doc_score:
            self.__scored_Sentences.append((self.sentences[ind], score))
        self.__scored_Sentences = sorted(self.__scored_Sentences, key=lambda x: x[1], reverse=True)

    def _get_summary_sentences(self):
        temp = []
        ind = 0
        while ind < min(len(self.__scored_Sentences), self.sent_count):
            temp.append(self.__scored_Sentences[ind][0])
            ind += 1
        return " ".join(temp)

    def get_summary(self, **kwargs):
        content = kwargs.get('content', "")
        sent_count = kwargs.get('sent_count', 4)
        self.sent_count = sent_count
        if self.sent_count is None or isinstance(self.sent_count, int) is False:
            raise MyException("The sent_count type is not a valid interger")
        if self.sent_count < -1:
            raise MyException("The sent_count can't be less than 1")
        self.content = content
        if self.content == "":
            with open(content_file_path, 'r') as file:
                content = file.read()
            self.content = content
        if self.content is None or isinstance(self.content, str) is False:
            raise MyException("The content type is not a valid string")
        self.cleaned_text = self._clean_content(self.content)
        self.sentences = self._get_sentences(self.cleaned_text)
        if len(self.sentences) < 5:
            raise MyException("The Content is too short less than 5 sentences!")
        self._get_corpus()
        self._cal_sent_score()
        return self._get_summary_sentences()


if __name__ == '__main__':
    summary = Summary().get_summary(sent_count=5)
    print(summary)