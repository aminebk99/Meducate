 
from core import BafLog
from prompts import GetDataPrompt
from api import GetDataAPI

# Optionally, import any other required modules or packages
# E.g., from api import YourAPI
# E.g., from prompts import YourPrompt

class GetData:
  def __init__(self):
     self.logger = BafLog

  def execute(self, data):
    # Process data here
    response = GetDataAPI.process(data)

    prompt = GetDataPrompt.get_data_prompt(response)
    return prompt


        