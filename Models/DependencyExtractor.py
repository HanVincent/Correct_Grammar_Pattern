import logging
from Models.Constant import COMMON_WORDS, PRONOUNS
from .VerbPatternExtractor import VerbPatternExtractor


class DependencyExtractor:

    def __init__(self):
        self.verb_pattern_extractor = VerbPatternExtractor()

    # TODO: consider noun chunk could be better
    def process(self, token):
        if self.verb_pattern_extractor.is_processable(token.tag_):
            try:
                pattern, ngram, indices = self.verb_pattern_extractor.extract_pattern(
                    token)
                norm_pattern = self.verb_pattern_extractor.normalize(pattern)

                # sent can be sorted by sent_score
                info = {
                    'norm_pattern': norm_pattern,
                    'pattern': pattern,
                    'ngram': ngram,
                    'indices': indices
                }

                return info
            except ValueError as e:
                logging.debug(e)

    def score(self, tokens):
        labels = [tk.text.lower() in COMMON_WORDS and tk.text.lower()
                  not in PRONOUNS for tk in tokens]
        return sum(labels) / len(tokens)
