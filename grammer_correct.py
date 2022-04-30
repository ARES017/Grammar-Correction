import torch
from nltk.tokenize import sent_tokenize, word_tokenize


def set_seed(seed):
  torch.manual_seed(seed)
  if torch.cuda.is_available():
    torch.cuda.manual_seed_all(seed)


def tokenize_sentences(long_sentence):
    sentence_list = sent_tokenize(long_sentence)
    sentence_list = [x.replace('\n', '') for x in sentence_list]
    return sentence_list
    

def grammer_correct(gf, sentence_list):
  corrected_sentece_list = []
  corrected_sentece_edit_list = []
  sentence_count = 1

  for sentence in sentence_list:
    corrections = gf.correct(sentence, max_candidates=1)
    
    for corrected_sentence in corrections:
      edit_list = gf.get_edits(sentence, corrected_sentence)
      corrected_sentece_edit_list.append(
        "\n".join(
          [f"Sentence {sentence_count}: {edits[1]} -> {edits[4]}" for edits in edit_list]
          )
        )

    corrected_sentece_list.append(corrected_sentence)
    sentence_count += 1

  updated_sentence = " ".join(corrected_sentece_list)
  sentence_edits = "\n".join(corrected_sentece_edit_list)

  return updated_sentence, sentence_edits
