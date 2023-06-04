# embeds a given log/query/trace into a vector space

import numpy as np
import pandas as pd
import os
import sys
import pickle
import argparse
import time
import math
import random
import json
import re
import openai
from sentence_transformers import SentenceTransformer
from typing import List
# make an Embedder that uses huggingface transformers to make quick embeddings 
# of logs/queries/traces


class Embedder:
    # TODO: all-mpnet-base-v2
    def __init__(self, ckpt_path='distilbert-base-nli-stsb-mean-tokens', use_openai=False):
        # Load a pre-trained SBERT model
        # TODO: GPU inference and batched inference and caching and on a serverless GPU?
        self.model = SentenceTransformer(ckpt_path)
        self.use_openai = use_openai

    def embed(self, text: str, engine="text-similarity-davinci-001") -> List[float]:
        if self.use_openai:
            return openai.Embedding.create(input=[text], engine=engine)["data"][0]["embedding"]
        else:
            return self.model.encode(text)