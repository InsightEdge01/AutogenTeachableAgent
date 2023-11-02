from autogen import UserProxyAgent
from autogen.agentchat.contrib.teachable_agent import TeachableAgent

# Load LLM inference endpoints from an env variable or a file
# See https://microsoft.github.io/autogen/docs/FAQ#set-your-api-endpoints

config_list = [
    {
        "model": "zephyr-7b-alpha.Q3_K_M.gguf", #the name of your running model
        "api_base": "http://localhost:1234/v1", #the local address of the api
        "api_type": "open_ai",
        "api_key": "NULL" # just a placeholder
    }
]
llm_config={"config_list": config_list, "request_timeout": 120}

#create the agent
teachable_agent = TeachableAgent(
    name="teachableagent",
    llm_config=llm_config,
    teach_config={
        "reset_db": False,  # Use True to force-reset the memo DB, and False to use an existing DB.
        "path_to_db_dir": "./tmp/interactive/teachable_agent_db"  # Can be any path.
    }
)

user = UserProxyAgent("user", human_input_mode="ALWAYS")

#Chat with TeachableAgent
# This function will return once the user types 'exit'.
teachable_agent.initiate_chat(user, message="Hi, I'm a teachable user assistant! What's on your mind?")

# Before closing the app, let the teachable agent store things that should be learned from this chat.
teachable_agent.learn_from_user_feedback()
teachable_agent.close_db()

#learning User Info---- what is my name and my mothers name?
#learning new facts---- define zephyr model"Zephyr is a series of language models that are trained to act as helpful assistants. Zephyr-7B-α is the first model in the series, and is a fine-tuned version of mistralai/Mistral-7B-v0.1 that was trained on on a mix of publicly available, synthetic datasets using Direct Preference Optimization (DPO).
#learning user preference----- summarize
#Learning new skills---- 
#Consider the identity:
#9 * 5 + 6 * 6 = 72
#Can you modify exactly one integer (and not more than that!) on the left hand side of the equation so the right hand side becomes 99?
#Let's think step-by-step, write down a plan, and then write down your solution as: "The solution is: A * B + C * D". 