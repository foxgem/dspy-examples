from dotenv import load_dotenv

import dspy
from prepare import extract_article_content

load_dotenv()


# Set up the LM.
gpt4o = dspy.OpenAI(model="gpt-4o-2024-08-06", max_tokens=1024)
dspy.configure(lm=gpt4o)


class Summary(dspy.Signature):
    """Summarize a document. The requirements are as follows:
    - Show the language used by the document, then use it for the result.
    - The summary should list 3~5 key points from the document.
    - The summary should not miss the information that the author wants to highlight.
    - End with 3~5 key words that summarize the document.
    - All key points and key words should be separated by a newline.
    """

    document = dspy.InputField()
    summary = dspy.OutputField()


def summarize(link: str) -> str:
    document = extract_article_content(link)
    summary = dspy.ChainOfThought(Summary)
    response = summary(
        document=document.content,
    )
    output = f"{document.title}:\n{'-'*10}\n{response.summary}"
    return output


# print(summarize("https://blog.dteam.top/posts/2024-03/farcaster-hub-internal.html"))
