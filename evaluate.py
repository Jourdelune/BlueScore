from nltk.translate.bleu_score import SmoothingFunction
from nltk.translate import bleu
import jieba


smoothie = SmoothingFunction().method4


def evaluate(target:str, translation:str):
    '''
    Return the bleu score of a translation.
    '''

    score = bleu([jieba.lcut(target)], jieba.lcut(translation), smoothing_function=smoothie)

    return score
