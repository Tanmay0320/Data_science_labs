from nltk.sentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
from nltk.tokenize import sent_tokenize, word_tokenize
from collections import Counter


def read_comments_from_file(file_path):
    comments = []

    with open(file_path, 'r') as file:
        for line in file:
            comment = line.strip()
            if comment:
                comments.append(comment)

    return comments

def analyze_sentiment(comments):
    sia = SentimentIntensityAnalyzer()
    
    positive = []
    negative = []
    neutral = []
    
    for comment in comments:
        score = sia.polarity_scores(comment)
        compound_score = score['compound']
        
        if compound_score >= 0.05:
            positive.append(comment)
        elif compound_score <= -0.05:
            negative.append(comment)
        else:
            neutral.append(comment)
    
    positive_count = len(positive)
    negative_count = len(negative)
    neutral_count = len(neutral)
    
    return positive, negative, neutral, positive_count, negative_count, neutral_count

def plot_sentiment_counts(positive_count, negative_count, neutral_count):
    categories = ['Positive', 'Negative', 'Neutral']
    counts = [positive_count, negative_count, neutral_count]

    plt.figure(figsize=(8, 5))
    plt.bar(categories, counts, color=['green', 'red', 'gray'])
    plt.title('Sentiment Analysis of Comments')
    plt.xlabel('Sentiment Category')
    plt.ylabel('Number of Comments')
    plt.ylim(0, max(counts) + 5)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    for i, count in enumerate(counts):
        plt.text(i, count + 0.2, str(count), ha='center')

    plt.show()

def summarize(comments, num_sentences=5):
    if not comments:
        return "No comments to summarize."

    text = ' '.join(comments)
    sentences = sent_tokenize(text)

    words = word_tokenize(text.lower())
    word_freq = Counter(words)

    sentence_scores = {}
    for sentence in sentences:
        sentence_score = sum(word_freq[word] for word in word_tokenize(sentence.lower()) if word in word_freq)
        sentence_scores[sentence] = sentence_score

    summarized_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]

    paragraph_summary = ' '.join(summarized_sentences)

    return paragraph_summary

def save_summary_to_file(summary, file_name):
    with open(file_name, 'w') as file:
        file.write(summary)

file_path = 'comments.txt'
comments_list = read_comments_from_file(file_path)
positive_comments, negative_comments, neutral_comments, pos_count, neg_count, neu_count = analyze_sentiment(comments_list)
plot_sentiment_counts(pos_count, neg_count, neu_count)

positive_summary = summarize(positive_comments)
negative_summary = summarize(negative_comments)
neutral_summary = summarize(neutral_comments)
save_summary_to_file(positive_summary, 'positive_summary.txt')
save_summary_to_file(negative_summary, 'negative_summary.txt')
save_summary_to_file(neutral_summary, 'neutral_summary.txt')
print("NLTK paragraph summaries saved to positive_summary.txt, negative_summary.txt, and neutral_summary.txt.")