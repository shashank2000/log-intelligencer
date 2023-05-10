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

# make an Embedder that uses huggingface transformers to make quick embeddings 
# of logs/queries/traces

class Embedder:
    def __init__(self, ckpt_path, model_name, model_type, model_params):
        self.model = load_from_checkpoint(model_name, model_type, model_params, ckpt_path)

    def get_embedding(text: str, engine="text-similarity-davinci-001") -> List[float]:
        # replace newlines, which can negatively affect performance.
        text = text.replace("\n", " ")
        return openai.Embedding.create(input=[text], engine=engine)["data"][0]["embedding"]

    def embed(item):
        return self.model(item)