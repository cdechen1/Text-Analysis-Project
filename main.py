from article_analyzer import analyze_article

articles = {
    "article1": "https://www.theguardian.com/business/2023/mar/17/what-happening-financial-markets-could-global-crisis",
    "article2": "https://www.nytimes.com/2023/03/17/business/economy/economy-banks-recession.html",
    "article3": "https://www.nytimes.com/2008/09/18/business/18markets.html",
}

for articleName, articleUrl in articles.items():
    print(f"Now analyzing article {articleName}")
    analyze_article(articleUrl)
