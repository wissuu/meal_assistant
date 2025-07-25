from langgraph.prebuilt import create_react_agent
from langchain.chat_models import init_chat_model
from langchain.schema import AIMessage
from .prompts import MEAL_PLANNING_PROMPT
from .api import get_meal_suggestions

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
    "messages": [{"role": "user", "content": "I need a high protein breakfast with around 400 calories"}]
})

assistant_messages = [
    msg for msg in response["messages"]
    if isinstance(msg, AIMessage) and isinstance(msg.content, str)
]

for msg in assistant_messages:
    print(msg.content)