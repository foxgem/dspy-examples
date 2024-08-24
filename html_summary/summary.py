from dotenv import load_dotenv
import dspy

from prepare import extract_article_content

load_dotenv()


# Set up the LM.
gpt4o = dspy.OpenAI(model="gpt-4o-2024-08-06", max_tokens=1024)
dspy.configure(lm=gpt4o)

summary = dspy.ChainOfThoughtWithHint("document -> summary")
document = extract_article_content(
    "https://blog.dteam.top/posts/2024-02/go-ethereum-cookbook.html"
)


response = summary(
    document=document.content,
    hint="the summary should be written in the same language used by document",
)

print(document.title, ":")
print("-" * 10)
print(response.summary)
