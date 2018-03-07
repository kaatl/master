#!/usr/bin/env python
# -*- coding: utf-8 -*-
from summa import summarizer



from sumy.parsers.plaintext import PlaintextParser #We’re choosing a plaintext parser here, other parsers available for HTML etc.
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer #We’re choosing Lexrank, other algorithms are also built in

from gensim.summarization.summarizer import summarize

def getSummary(text):
    summarized_text = summarizer.summarize(text, words=30, language="norwegian")

    if len(summarized_text) == 0:
        summarized_text = summarizer.summarize(text, words=50, language="norwegian")

    return summarized_text

def write_textsum_tofile(label, text, textrank_summary, lexrank_summary):
    with open('training_data_summarized.tsv', 'a') as file:
        file.write(text + '\t' + textrank_summary + '\t' + str(lexrank_summary) + '\t' + label)

def main():
    with open('training_data.tsv', 'r') as file:
        texts = file.readlines()


        for t in texts:
            textline = t.split('\t')
            text = ". ".join([textline[0], textline[1]])
            label = textline[3]

            text = text.replace('- ', '')
            text_length = len(text.split())

            # Gensim TextRank - only English language
            # gensim_textrank_summary = summarize(t, word_count = 30)




            if text_length > 50:
                # LexRank
                parser = PlaintextParser(text, Tokenizer("norwegian"))
                summarizer = LexRankSummarizer()
                lexrank_summary = summarizer(parser.document, 2)
                lexrank_summary = " ".join(str(sentence) for sentence in lexrank_summary)

                # TextRank
                textrank_summary = getSummary(text).replace('\n', '. ')
                textrank_summary_list = textrank_summary.split()

                if len(textrank_summary_list) > 50:

                    textrank_summary_sentence = textrank_summary.split('.')

                    if len(textrank_summary_sentence) > 2:
                        textrank_summary = ". ".join([textrank_summary_sentence[0], textrank_summary_sentence[1]])
                    else:
                        textrank_summary = ". ".join(textrank_summary_sentence)

                    if len(textrank_summary.split()) > 50:
                        textrank_summary = " ".join(textrank_summary.split()[:50])



            else:
                textrank_summary = text
                lexrank_summary = text

            write_textsum_tofile(label, text, textrank_summary, lexrank_summary)



main()
