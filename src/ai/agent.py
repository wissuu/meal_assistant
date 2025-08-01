from langgraph.prebuilt import create_react_agent
from langchain.chat_models import init_chat_model
from langchain.schema import AIMessage
from .prompts import MEAL_PLANNING_PROMPT, CHAT_PROMPT
from src.ai.tools.meal_suggestions import get_meal_suggestions
from src.db.meals_repository import log_meal

class MealPlanningChat:
    def __init__(self):
        self.model = init_chat_model(
            "anthropic.claude-3-sonnet-20240229-v1:0",
            model_provider="bedrock_converse"
        )
        self.agent = create_react_agent(
            model=self.model,  
            tools=[get_meal_suggestions, log_meal],  
            prompt=CHAT_PROMPT
        )
        self.conversation_history = []
    
    def add_message(self, role: str, content: str):
        self.conversation_history.append({"role": role, "content": content})
    
    def get_response(self, user_input: str) -> str:
        self.add_message("user", user_input)
        
        response = self.agent.invoke({
            "messages": self.conversation_history
        })
        
        assistant_messages = [
            msg for msg in response["messages"]
            if isinstance(msg, AIMessage) and isinstance(msg.content, str)
        ]
        
        if assistant_messages:
            assistant_response = assistant_messages[-1].content
            self.add_message("assistant", assistant_response)
            return assistant_response
        
        return "I'm sorry, I couldn't generate a response. Please try again."

def get_meal_suggestions_command(meal_type: str, target_protein: float = 30, target_calories: int = 400):
    model = init_chat_model(
        "anthropic.claude-3-sonnet-20240229-v1:0",
        model_provider="bedrock_converse"
    )

    agent = create_react_agent(
        model=model,  
        tools=[get_meal_suggestions],  
        prompt=MEAL_PLANNING_PROMPT
    )

    response = agent.invoke({
        "messages": [{"role": "user", "content": f"I need a {meal_type} with {target_protein}g protein and around {target_calories} calories"}]
    })

    assistant_messages = [
        msg for msg in response["messages"]
        if isinstance(msg, AIMessage) and isinstance(msg.content, str)
    ]

    for msg in assistant_messages:
        print(msg.content)