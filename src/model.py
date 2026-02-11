from random import choices # from standard library
from weights import weight # from source folder (naive_word_generating_model/src/weights.py)
class NaiveWordGeneratingModel:
  def __init__(self):
    """
    A reinforcement learning agent that learns to recreate 5 letter words from a huge dataset
    """
    self.weights = weight
    self.word_structure = [None, None, None, None, None]
    self.total_error = 0
    self.is_training = False
    self.generated_words = []

def generate(self): # generate word
  pass
  
def feedback(self): # feedback word
  pass

def iteration(self): # repeatedly train/generate
  pass
