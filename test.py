from quiz import PolyglotQuiz


def main():
    text = open('texts/cinderella_en.txt', 'rt').read()
    # IN --> Preposition or subordinating conjunction
    polyglot = PolyglotQuiz(text, _type='IN', regexp=r'\w+')
    polyglot.generate_quiz()


if __name__ == '__main__':
    main()
