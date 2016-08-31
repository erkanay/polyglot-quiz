# polyglot-quiz

It helps *lazy linguistics to generate simple questionaries for any purposes.

Basically, it takes a text in any language then produce number of questions by given grammar subject.

## Installation

```sh
$ git clone https://github.com/erkanay/polyglot-quiz.git
$ cd polyglot-quiz
$ pip install -r requirements.txt
$ python test.py
```

## Usage
```python
>>> from quiz import PolyglotQuiz

>>> text = open('anystory.txt', 'rt').read()
>>> # IN --> Preposition or subordinating conjunction
>>> polyglot = PolyglotQuiz(text, _type='IN', regexp=r'\w+')
>>> polyglot.generate_quiz()
```
```
Q.1) Cinderella, who saw all this, and
knew her slipper, said to them, laughing:
"Let me see ___ it will not fit me."

    a) out  b) if  c) unknown  d) among
    
Q.2) They threw themselves at her feet to beg pardon ___ all the
ill-treatment they had made her undergo.

    a) for  b) As  c) without  d) behind

Q.3) The guards ___ the palace gate were asked: 
If they had not seen a princess go out.

    a) at  b) after  c) appear  d) among
    
...

A.1) if  A.2) for  A.3) at

...
```

Please see full list of part of speech tags to generate different types of questionaries:

http://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html

Or learn more details about tags by following method:
```python
>>> polyglot.read_manual()

```

*note: thanks to [NLTK](http://www.nltk.org/).
