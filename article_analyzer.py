keywords = set(["crisis", "2008", "fear"])


def analyze(text: str):
    import nltk
    nltk.download('vader_lexicon')

    from nltk.sentiment.vader import SentimentIntensityAnalyzer

    print(SentimentIntensityAnalyzer().polarity_scores(text))

    rawWords = text.split(" ")

    words = list[str]()
    for word in rawWords:
        words.append(word.lower())

    counts: dict[str, int] = {}

    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

    # words is a dictionary of words to counts
    # example:
    # {
    #   the: 78
    #   the: 78
    #   the: 78
    # }

    words = list(counts.keys())

    words.sort(key=lambda word: counts[word], reverse=True)

    print(words[0:5])

    for keyword in keywords:
        count = counts.get(keyword)

        if count == None:
            count = 0

        print(f"The word {keyword} occurs {count} times")

    from collections import Counter

    counter = Counter(text)
    print(counter.most_common(5))


def analyze_article(url: str):
    from newspaper import Article

    article = Article(url)

    article.download()
    article.parse()

    analyze(article.text)
