import spacy
#from spacy import displacy

#https://jpboost.com/2018/02/06/creating-a-chatbot-with-rasa-nlu-and-rasa-core/

nlp = spacy.load('en')

docx = nlp(u"spaCy is an amazing tool like nltk")
print(docx)

my_file = open("my_spacy_file.txt").read()
doc_file = nlp(my_file)
print(doc_file)
print("*****************************")

for num, sentence in enumerate(doc_file.sents):
    print(f'{num}: {sentence}')

for token in docx:
    print(token.text)

print("**************************")
token_list = [token.text for token in docx]
print(token_list)

token_list = docx.text.split(" ")
print(token_list)


print("**************************")
#word shape
for word in docx:
    print(word.text, word.shape, word.shape_)

#Part of Speech Tagging
print("**************************")
ex1 = nlp("He drinks a drink.")
for word in ex1:
    print(word.text, word.pos_, word.pos)

print("**************************")
ex2 = nlp("I fish a fish.")
for word in ex2:
    print(word.text, word.pos_, word.tag_)


#spacy.explain("VBP")
print("**************************")
ex01 = nlp(u"All the faith he had had had had no effect on the outcome of his life.")
for word in ex01:
    print((word.text, word.tag_, word.pos_))


print("**************************")
ex02 = nlp(u"The man the professor the student has studies Rome.")
for word in ex02:
    print((word.text, word.tag_, word.pos_))

print("**************************")
#Syntactic Dependency
#It helps us to know the relation between tokens.
ex03 = nlp("Sally likes Sam.")
for word in ex03:
    print((word.text, word.tag_, word.pos_, word.dep_))

#Visualizing dependency using displaCy



#Lemmatizing
#Text Normalization
#Word inflection == syntactic differences between word forms
#Reducing a word to its base/root form
#Lemmatization
#a word based on its intended meaning
#Stemming
# cutting of the prefixes/suffixes to reduce a word to base form
print("**************************")
docx = nlp("study studying studious studio student")
for word in docx:
    print(word.text, word.lemma_, word.pos_)

print("**************************")
docx = nlp("walking walks walk walker")
for word in docx:
    print(word.text, word.lemma_, word.pos_)

print("**************************")
docx = nlp("good goods run running runner runny was be were")
for word in docx:
    print(word.text, word.lemma_, word.pos_)

#Named Entity Recognition or Detection
"""
Classifying a text into predefined categories or real world object entities.
takes a string of text(sentence or paragraph) as input and identifies relevant nouns
(people, places, and organizations) that are mentioned
in that string

Uses
classifying or Categorizing contents by getting the relevant tags
Improve search algorithms
For content recommendations
For info extraction

.ents

.label

"""
print("**************************")

wikitext = nlp("By 2020 the telecom company Orange will relocate from Trukey to Orange County in U.S. close to Apple.  It will cost them 2 million dollers.")

for word in wikitext.ents:
    print(word.text, word.label_)

print("**************************")
some_txt = nlp("Linus Benedict Tarvalds is a Finnish American software engineer who is the creator and lone developer of the Linux kernel, which became the Linux operating systems such as the Linux operating sysstem.")

for word in some_txt.ents:
    print(word.text, word.label_)

print("**************************")
docx = nlp("The rat the cat the dog chased killed ate the malt.")

for word in docx:
    print(word.text, word.pos_, word.dep_)

#displacy.serve(docx, style='dep')

