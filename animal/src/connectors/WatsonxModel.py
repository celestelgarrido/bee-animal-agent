from beeai_framework.adapters.watsonx.backend.chat import WatsonxChatModel

class WatsonxModel():
    def __init__(self):
        self.wx_model_id = "meta-llama/llama-3-1-8b-instruct"

        self.llm = WatsonxChatModel(
            self.wx_model_id
        )
