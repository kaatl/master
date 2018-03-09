#!/usr/bin/env python
# -*- coding: utf-8 -*-
from summa import summarizer



from sumy.parsers.plaintext import PlaintextParser #We’re choosing a plaintext parser here, other parsers available for HTML etc.
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer #We’re choosing Lexrank, other algorithms are also built in

from gensim.summarization.summarizer import summarize

def getTextrankSum(text):
    summarized_text = summarizer.summarize(text, words=30, language="norwegian")

    if len(summarized_text) == 0:
        summarized_text = summarizer.summarize(text, words=50, language="norwegian")

    return summarized_text

def getLexRankSum(text):
    parser = PlaintextParser(text, Tokenizer("norwegian"))
    summarizer = LexRankSummarizer()
    lexrank_summary = summarizer(parser.document, 2)

    return lexrank_summary

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
                lexrank_summary = getLexRankSum(text)
                lexrank_summary = " ".join(str(sentence) for sentence in lexrank_summary)
                lexrank_summary_list = lexrank_summary.split()
                if len(lexrank_summary_list) > 50:
                    lexrank_summary = " ".join(lexrank_summary_list[:50])

                # TextRank
                textrank_summary = getTextrankSum(text).replace('\n', '. ')
                textrank_summary_list = textrank_summary.split()

                # If number of words are over 50
                if len(textrank_summary_list) > 50:

                    # Split for each sentence
                    textrank_summary_sentence = textrank_summary.split('.')

                    # Include only the two first sentences
                    if len(textrank_summary_sentence) > 2:
                        textrank_summary = ". ".join([textrank_summary_sentence[0], textrank_summary_sentence[1]])
                    else:
                        textrank_summary = ". ".join(textrank_summary_sentence)

                    textrank_summary_list = textrank_summary.split()
                    # If the two sentences still are over 50 words, cut sentence after 50 words.
                    if len(textrank_summary_list) > 50:
                        textrank_summary = " ".join(textrank_summary_list[:50])



            else:
                textrank_summary = text
                lexrank_summary = text

            # print len(lexrank_summary.split())
            write_textsum_tofile(label, text, textrank_summary, lexrank_summary)



main()
