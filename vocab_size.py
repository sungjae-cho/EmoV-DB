import os
import pandas as pd
import string
from nltk import sent_tokenize, word_tokenize


emov_db_csv_path = os.path.join('data_stat', 'emov_db.csv')

def load_emov_db():
    df = pd.read_csv(emov_db_csv_path)

    return df


def get_transcriptions(df):
    return df.transcription.tolist()


def get_vocab(transription_list):
    alpha_tokens = list()
    mixed_tokens = list()

    for t in transription_list:
        tokens = word_tokenize(t)
        alpha_tokens += [word.lower() for word in tokens if word.isalpha()]
        mixed_tokens += [word for word in tokens if not word.isalpha()]

    alpha_tokens = set(alpha_tokens)
    mixed_tokens = set(mixed_tokens)
    nonalpha_tokens = set()
    str_alphabets = string.ascii_lowercase + string.ascii_uppercase

    for token in mixed_tokens:
        if len(set(str_alphabets).intersection(set(token))) == 0:
            nonalpha_tokens.add(token)

    mixed_tokens = mixed_tokens.difference(nonalpha_tokens)

    return alpha_tokens, mixed_tokens, nonalpha_tokens

def save_vocab_size():
    df = load_emov_db()
    transcriptions = get_transcriptions(df)
    alpha_tokens, mixed_tokens, nonalpha_tokens = get_vocab(transcriptions)

    lines = list()
    lines.append("len(alpha_tokens) = {}\n".format(len(alpha_tokens)))
    lines.append("len(mixed_tokens) = {}\n".format(len(mixed_tokens)))
    lines.append("len(nonalpha_tokens) = {}\n".format(len(nonalpha_tokens)))
    lines.append("len(all_tokens) = {}\n".format(len(alpha_tokens) + len(mixed_tokens) + len(nonalpha_tokens)))

    txt_path = 'transcription_vocab_size.txt'
    with open(txt_path, 'w') as f:
        f.writelines(lines)
        print('Vocab size of transriptions saved in {}.'.format(txt_path))


if __name__ == "__main__":
    save_vocab_size()
