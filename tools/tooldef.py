from dotenv import load_dotenv
from langchain_tavily import TavilySearch
from pydantic import BaseModel, Field
from langchain_core.tools import tool
import os

load_dotenv()

# --- 1. Define a structured output schema for the tool's result ---
class ContactLookupResult(BaseModel):
    """Output structure for the contact_lookup tool."""
    found: bool = Field(description="True if the contact was found, False otherwise.")
    email: str = Field(default="", description="The email address if found, otherwise an empty string.")
    phone: str = Field(default="", description="The phone number if found, otherwise an empty string.")
    message: str = Field(description="A descriptive message about the result.")

# Define a structured input schema for the tool
class ContactLookupInput(BaseModel):
    """Input for the contact_lookup tool."""
    name: str = Field(description="The full name of the person whose contact information is needed.")
    email: str = Field(default=None, description="The email of the person whose contact information is needed.")
    
@tool(args_schema=ContactLookupInput, return_direct=False) # return_direct=False is default, but good to be explicit
def contact_lookup(name: str) -> ContactLookupResult:
    """
    Looks up the contact information (email and phone) for a specified person.
    
    Returns a structured result indicating if the contact was found and the details.
    
    Use this tool ONLY if the user asks for a person's contact details, 
    and you need the data to complete their request.
    """
    # Simulate a database/API lookup
    if "alice" in name.lower():
        return ContactLookupResult(
            found=True, 
            email="alice.j@corp.com", 
            phone="555-123-4567",
            message=f"Contact info found for {name}."
        )
    elif "bob" in name.lower():
        return ContactLookupResult(
            found=True, 
            email="bob.k@corp.com", 
            phone="555-987-6543",
            message=f"Contact info found for {name}."
        )
    else:
        # --- 2. Return a structured NOT FOUND result ---
        return ContactLookupResult(
            found=False, 
            email="", 
            phone="",
            message=f"Contact information **NOT FOUND** for {name}. The subsequent action (like sending an email) cannot proceed."
        )

class EmailPerson(BaseModel):
    """Input for the email_person tool."""
    email: str = Field(description="The email address of the person to email.")
    name: str = Field(description="The full name of the person to email.")
    subject: str = Field(description="The subject of the email.")
    body: str = Field(description="The body content of the email.")

@tool(args_schema=EmailPerson)
def email_person(email: str, name: str, subject: str, body: str) -> str:
    """
    Sends an email to the specified person using the email retrieved in contact_lookup with the given subject and body.
    
    Use this tool ONLY if the user requests to send an email to someone.
    """
    if not email:
        return f"Cannot send email to {name}. The email address provided was empty or invalid. You must first find the email."
        
    print(f"Sending email to {name}... using email: {email}")
    print(f"Subject: {subject}")
    print(f"Body: {body}")
    print("Email sent successfully.")
    # Simulate sending an email
    return f"Email sent to {name} with subject '{subject}'."

search = TavilySearch(api_key=os.getenv("TAVILY_API_KEY"))