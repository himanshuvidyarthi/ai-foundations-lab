# to do 
# email classification -> (category, urgency_score, requires_reply)
# create a BaseModel -> "", int, Bool

from pydantic import BaseModel, ValidationError

class EmailClassification(BaseModel):
    category: str 
    urgency_score: int
    requires_reply: bool 

def analyze_email():
    try: 
        mock_llm_output = { 
            "category": "support",
            "urgency_score": "8",
            "requires_reply": "1"
        }

        email_res = EmailClassification(**mock_llm_output)

        print(email_res)

        if email_res.requires_reply:
            print("Reply to this email ASAP!")

        else: 
            print("Reply is not imp!")
    except ValidationError as e:
        print(e.json()) 

analyze_email()