
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from tools.tooldef import contact_lookup, search, email_person
import os

load_dotenv()

GEMINI_MODEL_NAME = "gemini-2.5-flash"

llm = ChatGoogleGenerativeAI(
    model=GEMINI_MODEL_NAME,
    temperature=0,
    google_api_key=os.getenv("GEMINI_API_KEY") 
)

tools = [contact_lookup, search, email_person]

# --- 3. Optional: Add a more specific system prompt ---
system_prompt = (
    "You are a helpful assistant. You have access to tools to look up contacts, "
    "send emails, and search the web. "
    "**CRITICAL:** When you use the `contact_lookup` tool, **always inspect the result**. "
    "If the result indicates the contact was NOT FOUND, you must **stop the planned action** "
    "(e.g., sending an email) and **report the problem** back to the operator immediately. "
    "Do not attempt to use the `email_person` tool if the email is empty or the contact wasn't found."
)

agent = create_agent(llm, tools, system_prompt=system_prompt)

# Test the agent
if __name__ == "__main__":
    '''
    print("Agent is about to be invoked...")
    # Example that will FAIL to find a contact
    inputs_fail = {"messages": [{"role": "user", "content": "Please send a quick email to Charlie about the project status."}]}
    print("\n--- Test Case: Contact Not Found (Charlie) ---")
    for chunk in agent.stream(inputs_fail, stream_mode="updates"):
        print(chunk)
    print("Agent invocation has finished.")
    
    # Example that will SUCCEED
    inputs_success = {"messages": [{"role": "user", "content": "Please send an email to Alice with the subject 'Meeting Tomorrow' and the body 'Please confirm your availability for the 10 AM meeting'."}]}
    print("\n--- Test Case: Contact Found (Alice) ---")
    for chunk in agent.stream(inputs_success, stream_mode="updates"):
        print(chunk)
    print("Agent invocation has finished!")
    '''


    inputs_success = {"messages": [{"role": "user", "content": "I am changing the brakes on a ford fusion 2012. What tools do I need, lookup the part numbers and tell me how many shop hours it will take and what is the average cost based on Tampa, FL."}]}
    print("\n--- Test Case: Contact Found (Alice) ---")
    for chunk in agent.stream(inputs_success, stream_mode="updates"):
        print(chunk)
    print("Agent invocation has finished!")