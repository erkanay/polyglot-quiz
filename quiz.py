"""
Polyglot Quiz generates simple questionary for linguistics.

It's easy to conduct questionary in any grammar subject.

Please see full list of part of speech tags:

http://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html

>>> from quiz import PolyglotQuiz
>>> polyglot = PolyglotQuiz(text, _type='JJ', regexp=r'\w+')
>>> polyglot.generate_quiz()

"""
import re
import random
import nltk
from collections import defaultdict
from nltk.tag import pos_tag
from nltk.tokenize import (sent_tokenize,
                           word_tokenize,
                           RegexpTokenizer)


class PolyglotQuiz(object):
    QUESTION_TEMPLATE = """
    \n\n
    Q.{}) {}\n
          a) {}  b) {}  c) {}  d) {}
    """
    ANSWER_TEMPLATE = """A.{}) {}"""

    def __init__(self, _text, _type='IN', language='english', regexp=None):
        self.text = _text
        self._type = _type
        self.language = language
        self.regexp = regexp
        self.answers = defaultdict()
        self.questions = defaultdict()

    def tokenize(self, _text):
        if self.regexp:
            return RegexpTokenizer(self.regexp).tokenize(_text)
        return word_tokenize(_text, language=self.language)

    def get_words(self, _text):
        return self.tokenize(_text)

    @property
    def _sentences(self):
        return sent_tokenize(self.text)

    @property
    def _questions(self):
        questions = defaultdict(list)
        for sentence in self._sentences:
            mapping = self.map_words(sentence)
            if self._type in mapping.keys():
                rep = mapping[self._type][0]
                questions[self._type].append(
                    (re.sub(re.compile(r'\b%s\b' % rep), '___', sentence), rep)
                )
        return questions

    def map_words(self, _text):
        mapping = defaultdict(list)
        tagged_words = pos_tag(set(self.get_words(_text)))
        for word, tag in tagged_words:
            mapping[tag].append(word)
        return mapping

    def generate_quiz(self):
        result = []
        questions = self.get_questions()
        answers = self.get_answers()
        for _, question in questions.items():
            print(question)
            result.append(self.ANSWER_TEMPLATE.format(_, answers[_]))
        print(self.format_columns(result, 3))

    def get_questions(self):
        mapping = self.map_words(self.text)
        for _type, question in self._questions.items():
            for i, _question in enumerate(question, 1):
                q = _question[0]
                answer = _question[1]
                self.answers[i] = answer
                choices = random.sample(set(mapping[_type]), 4)
                if answer not in choices:
                    choices[random.randint(0, 3)] = answer
                self.questions[i] = self.QUESTION_TEMPLATE.format(i, q, *choices)
        return self.questions

    def get_answers(self):
        return self.answers

    @staticmethod
    def format_columns(_list, cols):
        lines = ('\t'.join(_list[i:i + cols]) for i in range(0, len(_list), cols))
        return '\n'.join(lines)

    @staticmethod
    def read_manual():
        return nltk.help.upenn_tagset()
