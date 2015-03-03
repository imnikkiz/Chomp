from sys import argv
import csv, nltk, numpy



def main(ingredient_file):
    default_tagger = nltk.data.load(nltk.tag._POS_TAGGER)
    model = {}
    tagger = nltk.tag.UnigramTagger(model=model, backoff=default_tagger)
    with open(ingredient_file) as f:
        reader = csv.reader(f)
        word_dict = {}
        for row in reader:
            row = row[0].decode('utf-8').strip()
            text = nltk.word_tokenize(row)
            tagged = tagger.tag(text)

            amount_list = []
            noun_list = []
            other_list = []

            for tag_entry in tagged:
                word, tag = tag_entry

                if tag == "CD" or tag == "LS":
                    amount_list.append(word)
                elif tag == "NNS" or tag == "NN":
                    noun_list.append(word)
                else:
                    other_list.append(word)
            
            print amount_list
            print noun_list
            print other_list



if __name__ == "__main__":
    ingredient_file = argv[1]
    main(ingredient_file)