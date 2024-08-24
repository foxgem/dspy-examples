from newspaper import Article
from pydantic import BaseModel


class ExtractedContent(BaseModel):
    title: str
    content: str


def extract_article_content(url):
    try:
        # Create an Article object
        article = Article(url)
        article.download()
        article.parse()

        # Extract the main content
        title = article.title
        text = article.text

        return ExtractedContent(title=article.title, content=article.text)

    except Exception as e:
        return f"An error occurred: {str(e)}"


# print(
#     extract_article_content(
#         "https://blog.dteam.top/posts/2024-06/something-about-farcaster-development.html"
#     )
# )
