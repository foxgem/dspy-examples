from dotenv import load_dotenv
import dspy

from prepare import extract_article_content

load_dotenv()


# Set up the LM.
gpt4o = dspy.OpenAI(model="gpt-4o-2024-08-06", max_tokens=1024)
dspy.configure(lm=gpt4o)


class Summary(dspy.Signature):
    """Summarize a document:
    1. The summary should be written in the same language used by the document.
    2. The summary should list 3~5 key points from the document.
    3. The summary should not miss the information that the author wants to highlight.
    """

    document = dspy.InputField(desc="The document to summarize.")
    summary = dspy.OutputField(desc="The summary of the document.")


summary = dspy.ChainOfThought(Summary)
document = extract_article_content(
    "https://towardsdatascience.com/automating-prompt-engineering-with-dspy-and-haystack-926a637a3f43"
)


response = summary(
    document=document.content,
)

print(document.title, ":")
print("-" * 10)
print(response.summary)
