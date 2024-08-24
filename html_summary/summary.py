from dotenv import load_dotenv
import dspy

from prepare import extract_article_content

load_dotenv()


# Set up the LM.
gpt4o = dspy.OpenAI(model="gpt-4o-2024-08-06", max_tokens=1024)
dspy.configure(lm=gpt4o)


class Summary(dspy.Signature):
    """Summarize a document:
    1. Identify the language of the document.
    2. Write the summary in the same language.
    3. The summary should list 3~5 key points from the document.
    4. Each key point has its own line.
    4. The summary should not miss the information that the author wants to highlight.
    """

    document = dspy.InputField(desc="The document to summarize.")
    summary = dspy.OutputField(desc="The summary of the document.")


def summarize(link: str) -> str:
    document = extract_article_content(link)
    summary = dspy.ChainOfThought(Summary)
    response = summary(document=document.content)
    output = f"{document.title}:\n{'-'*10}\n{response.summary}"

    print(output)

    return output


# print(
#     summarize(
#         "https://blog.dteam.top/posts/2024-06/something-about-farcaster-development.html"
#     )
# )
