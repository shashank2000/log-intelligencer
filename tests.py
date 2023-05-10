# embedder tests

from unittest import TestCase
from embedder import Embedder
import numpy as np

class TestEmbedder(TestCase):
    def test_simple_sentence(self):
        embedder = Embedder()
        sentence = 'This is a simple sentence.'
        embedding = embedder.embed(sentence)
        self.assertEqual(len(embedding), 768)
        self.assertEqual(type(embedding), np.ndarray)
        self.assertEqual(embedding.shape, (768,))

    def test_simple_similarity(self):
        # test that a query is more similar to the log we care about
        embedder = Embedder()
        sentence = 'This is a simple sentence.'
        embedding = embedder.embed(sentence)
        self.assertEqual(len(embedding), 768)
        self.assertEqual(type(embedding), np.ndarray)
        self.assertEqual(embedding.shape, (768,))
