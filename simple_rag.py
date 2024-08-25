from dotenv import load_dotenv
import dspy

load_dotenv()


class RAGSignature(dspy.Signature):
    """
    Given a context, question, answer the question.
    """

    context = dspy.InputField()
    question = dspy.InputField()
    answer = dspy.OutputField()


class RAG(dspy.Module):
    def __init__(self, num_passages=3):
        super().__init__()

        self.retrieve = dspy.Retrieve(k=num_passages)
        self.generate_answer = dspy.ChainOfThought(RAGSignature)

    def forward(self, question):
        context = self.retrieve(question).passages
        prediction = self.generate_answer(context=context, question=question)
        return dspy.Prediction(context=context, answer=prediction.answer)


# Set up the LM.
turbo = dspy.OpenAI(model="gpt-3.5-turbo-instruct", max_tokens=250)
colbert = dspy.ColBERTv2(url="http://20.102.90.50:2017/wiki17_abstracts")
dspy.configure(lm=turbo, rm=colbert)

qa = RAG()
response = qa(
    question="Who was the president of the United States in 1960?",
)

print(response.answer)
