from datetime import datetime
from core import BafLog
# Optionally, import any other required modules or packages

class GetDataPrompt:  # Replace GetData with the name of your prompt

    def get_data_prompt(data):
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        prompt = f"""

    Given a user message related to medication articles, instruct the model to conduct a comprehensive analysis of the content and extract specific information. The primary goal is to identify and provide insights into five key aspects: Data Classification Identifier (DCI), Categories (given), the country in which the event occurs or the mentioned country in articles, the date on which it occurs or is mentioned in the article, and if additional categories or DCIs are found, include them in the data.

    Additionally, the 'risk' key should contain a concise description of the consequences related to the identified DCI and provide news related to it, limited to 3 to 10 words. The results should be formatted in JSON with the following keys: dci, category, risk, country, date, title, laboratoire, and summary.

    GUIDELINES:

    REMEMBER THAT THE FOLLOWING ARTICLE IS EXTRACTED FROM A WEBSITE.
    Clearly define all DCIs in the article, considering only those from the provided DCI list.
    For each DCI, specify the risk and its category based on the article.
    Use the content of the 'risk' result to create a title.
    Find the source of the laboratoire that identified this risk.
    The summary should include a description of the risk based on the article, comprising 3 to 5 lines. Extract the specific country mentioned in the article and incorporate it into the summary.
    If you find in the article mentioned next year or 2 years ago or another timeframe, provide the exact date in the result {current_date}.
    If there are more than 1 DCI, encapsulate each in a JSON object with its category, risk, and summary. Each JSON object should contain keys: dci, category, risk, country, date, and summary.
    'data' will be an array containing JSON objects.
    If no DCI is found, do not return an object.
    """
        return prompt.format(data=data)

        