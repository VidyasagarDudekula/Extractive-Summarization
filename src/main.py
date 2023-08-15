from collections import defaultdict
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from gensim.corpora.dictionary import Dictionary
import re
import os
import math
content_file_path = os.path.abspath(os.getcwd()) + '/data/content.txt'


class MyException(Exception):
    """This is a custom exception."""
    def __init__(self, message):
        super().__init__(message)


class Summary():
    def __init__(self):
        self.content = ""
        self.cleaned_text = ""
        self.sent_count = ""
        self.__corpus = None
        self.__token_corpus_id_count = None
        self.__token_doc_id_count = None
        self.__token_doc_id_score = None
        self.__doc_score = None
        self.__sentence_score = None
        self.__sentences = None

    def _get_sentences(self, text):
        sentences = sent_tokenize(text)
        return sentences

    def _clean_content(self, text):
        text = re.sub(r"\s+", " ", text)
        text = re.sub(r'"', " ", text)
        text = text.replace(" . ", ". ")
        text = text.replace(".. ", ". ")
        text = re.sub(r"\s+", " ", text)
        return text

    def _valid_token(self, token):
        return token.isalnum() and token not in stopwords.words('english')

    def _filter_tokens(self, doc_tokens):
        return [token for token in doc_tokens if self._valid_token(token)]

    def _get_corpus(self):
        all_tokens = [word_tokenize(sent) for sent in self.sentences]
        filtered_tokens = [self._filter_tokens(doc_tokens) for doc_tokens in all_tokens]
        dictionary = Dictionary(filtered_tokens)
        self.__token_doc_id_count = [dictionary.doc2bow(doc) for doc in filtered_tokens]
        self.__token_corpus_id_count = defaultdict(int)
        for doc in self.__token_doc_id_count:
            seen = []
            for token_id, count in doc:
                if token_id in seen:
                    continue
                seen.append(token_id)
                self.__token_corpus_id_count[token_id] += 1

    def _cal_doc_id_score(self):
        self.__doc_score = []
        for ind, doc in enumerate(self.__token_doc_id_count):
            total_score = 0
            for token_id, count in doc:
                w = count * math.log(len(self.sentences)/self.__token_corpus_id_count[token_id])
                total_score += w
            self.__doc_score.append((ind, total_score))
        self.__sentence_score = []
        for ind, score in self.__doc_score:
            self.__sentence_score.append((self.sentences[ind], score))
        self.__sentence_score = sorted(self.__sentence_score, key=lambda x: x[1], reverse=True)

    def _get_summary_sentences(self):
        temp = []
        ind = 0
        while ind < min(len(self.__sentence_score), self.sent_count):
            temp.append(self.__sentence_score[ind][0])
            ind += 1
        return " ".join(temp)

    def get_sumary(self, **kwargs):
        content = kwargs.get('content', "")
        sent_count = kwargs.get('sent_count', 4)
        self.sent_count = sent_count
        if self.sent_count is None or isinstance(self.sent_count, int) is False:
            raise MyException("The sent_count type is not a valid interger")
            return ""
        if self.sent_count < -1:
            raise MyException("The sent_count can't be less than 1")
            return ""
        self.content = content
        if self.content == "":
            with open(content_file_path, 'r') as file:
                content = file.read()
            self.content = content
        if self.content is None or isinstance(self.content, str) is False:
            raise MyException("The content type is not a valid string")
            return ""
        self.cleaned_text = self._clean_content(self.content)
        self.sentences = self._get_sentences(self.cleaned_text)
        if len(self.sentences) < 5:
            raise MyException("The Content is too short less than 5 sentences!")
            return ""
        self._get_corpus()
        self._cal_doc_id_score()
        return self._get_summary_sentences()


if __name__ == '__main__':
    summary = Summary().get_sumary()
    print(summary)