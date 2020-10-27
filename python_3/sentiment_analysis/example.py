import random
import nltk
# nltk.download('twitter_samples')
# nltk.download('averaged_perceptron_tagger')
from nltk import classify, pos_tag
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.corpus import twitter_samples
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.classify.naivebayes import NaiveBayesClassifier

positive = twitter_samples.strings('positive_tweets.json')
negative = twitter_samples.strings('negative_tweets.json')
stop_words = list(set(stopwords.words('english')))

print(f"FIST EXAMPLE OF THE DATASET:\n################\n{positive[0]}\n################")

positive_tokens = twitter_samples.tokenized('positive_tweets.json')
negative_tokens = twitter_samples.tokenized('negative_tweets.json')

def clean(tokens):
    tokens = [x for x in tokens if not x in stop_words]

    l = WordNetLemmatizer()
    lemmatized = []

    for word, tag in pos_tag(tokens):
        if tag.startswith('NN'):
            pos = 'n'
        elif tag.startswith('VB'):
            pos = 'v'
        else:
            pos = 'a'
        lemmatized.append(l.lemmatize(word, pos))
    return lemmatized

positive_clean = []
negative_clean = []

for token in positive_tokens:
    positive_clean.append(clean(token))

for token in negative_tokens:
    negative_clean.append(clean(token))

def final_token_generator(tokens):
    for tokens in tokens:
        yield dict([token, True] for token in tokens)

positive_model_tokens = final_token_generator(positive_clean)
negative_model_tokens = final_token_generator(negative_clean)


positive_dataset = [(token, "Positive") for token in positive_model_tokens]
negative_dataset = [(token, "Negative") for token in negative_model_tokens]

dataset = positive_dataset + negative_dataset

random.shuffle(dataset)
random.shuffle(dataset)
random.shuffle(dataset)

training = dataset[:7000]
testing = dataset[7000:]

classifier = NaiveBayesClassifier.train(training)

print("Accuracy:", classify.accuracy(classifier, testing))
print(classifier.show_most_informative_features(10))

def analyze(input):
    custom_tokens = clean(word_tokenize(input))
    return classifier.classify(dict([token, True] for token in custom_tokens))

# def change_emote(self, event):
#     result = self.analyzer.analyze(self.text_field.get())
#     if result == 'Positive':
#         self.emote['text'] = self.positive
#     elif result == 'Negative':
#         self.emote['text'] = self.negative
#     else:
#         self.emote['text'] = self.neutral

if __name__ == "__main__":
    phrase = "nice to meet you"
    print(f"{phrase}:\nthe phrase is ->{analyze(phrase)}")