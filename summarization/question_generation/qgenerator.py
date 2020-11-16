if __package__ is None or __package__ == '':
    from question_generator.questiongenerator import QuestionGenerator
else :
    from .question_generator.questiongenerator import QuestionGenerator
qg = QuestionGenerator()

def generate(text):
    try:
        return qg.generate(text, num_questions=1)[0]['question']
    except:
        return ''

def main():
    s = input('>')
    print(generate(s))

if __name__ == '__main__':
    main()