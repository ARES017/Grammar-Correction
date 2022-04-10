from gramformer import Gramformer
import torch
from nltk.tokenize import sent_tokenize, word_tokenize


def set_seed(seed):
  torch.manual_seed(seed)
  if torch.cuda.is_available():
    torch.cuda.manual_seed_all(seed)


def tokenize_long_sentences(long_sentence):
    sentence_list = sent_tokenize(long_sentence)
    sentence_list = [x.replace('\n', '') for x in sentence_list]
    return sentence_list
    

def grammer_correct(influent_sentences):
  for influent_sentence in influent_sentences:
    corrected_sentences = gf.correct(influent_sentence, max_candidates=1)
    print("[Input] ", influent_sentence)
    
    for corrected_sentence in corrected_sentences:
      print("[Correction] ", corrected_sentence)
      edit_list = gf.get_edits(influent_sentence, corrected_sentence)
      
      for edits in edit_list: 
        print(f"[Edits] {edits[1]} -> {edits[4]}")

    print("-" *100)
