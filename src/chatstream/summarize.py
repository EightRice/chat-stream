from collections import deque, Counter
from typing import Tuple

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer

nltk.download('punkt', quiet=True)

class RollingSummary:
    def __init__(self, window_size: int = 100):
        self.window = deque(maxlen=window_size)
        self.sentiment = SentimentIntensityAnalyzer()

    def add(self, message: str):
        self.window.append(message)

    def compute(self) -> Tuple[str, float, float]:
        if not self.window:
            return "", 0.0, 0.0
        text = "\n".join(self.window)
        parser = PlaintextParser.from_string(text, Tokenizer("english"))
        summarizer = LsaSummarizer()
        summary_sentences = summarizer(parser.document, 2)
        summary = " ".join(str(s) for s in summary_sentences)
        # Sentiment
        scores = [self.sentiment.polarity_scores(m)["compound"] for m in self.window]
        avg_sentiment = sum(scores) / len(scores)
        # Confidence as ratio of top frequent bigram
        words = [w.lower() for msg in self.window for w in msg.split()]
        if not words:
            confidence = 0.0
        else:
            counts = Counter(words)
            confidence = counts.most_common(1)[0][1] / len(words)
        return summary, avg_sentiment, confidence
