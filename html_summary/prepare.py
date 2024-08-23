from newspaper import Article


def extract_article_content(url):
    try:
        # Create an Article object
        article = Article(url)
        article.download()
        article.parse()

        # Extract the main content
        title = article.title
        text = article.text

        return {
            "title": title,
            "content": text,
        }

    except Exception as e:
        return f"An error occurred: {str(e)}"


# print(
#     extract_article_content(
#         "https://blog.dteam.top/posts/2024-06/something-about-farcaster-development.html"
#     )
# )
