# Senior Technical Recruiter 

# --PROMPT STRUCTURE 

#resume text: text extracted from resume (pdf format)

#brief 
#context
#requirements: 
#task 
# score logic : "python"--> 30, "ML"--> 30, "tools"-->10....
#output: 
# {
#     name, 
#     experience,
#     skills:[....],
#     match_score
#     shortlist,
#     justification
# }

#resume 

from google import genai 
import os 

gemini_api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key = gemini_api_key)
if not gemini_api_key:
    raise ValueError("API key is missing. Please use correct gemini api key")

resume = """
John Doe
Email: john@email.com

Experience:
- Worked as Software Engineer for 2 years
- Built ML model for predicting house prices using sklearn
- Used Python, Pandas, NumPy

Projects:
- Chatbot using NLP
- Recommendation system

Skills:
Python, Machine Learning, SQL, TensorFlow
"""

prompt = """
    You are a Senior Technical Recruiter hiring for a Machine Learning Engineer role.

    CONTENT: You are given a raw resume text extracted from PDFs, the formmating maybe in inconsistent

    Job Requirements:
    - Strong Python Programming 
    - Experience in Machine Learning (Supervised/Unsupervised/Deep Learning)
    - Experience with libraries like scikit-learn, Tensorflow, Pytorch, Keras
    - 2+ years of relevant experience preferred

    TASK:
    1. Analyze the candidate resume.
    2. Extract key information:
        - name 
        - years of exp
        - skills
        - projects
    3. Evaluate the candidate based on task requirements.
    4. Assign a match score(0-100)
    5. Decide whether to shortlist (YES/NO).
    6. Provide a brief description. 

    SCORING LOGIC:
    - Python (mandatory) : 30 points 
    - ML exp (mandatory) : 30 points 
    - Tools/frameworks : 10 points 
    - Bonus (SQL, deployment, real-world impact).

    RULES:
    - Do not guess missing data. 
    - Be strict in evaluation.
    - Penalize vague resumes.
    - Prefer practical experience over theoretical knowledge. 

    OUTPUT FORMAT (strict JSON):
    {
        "name":"",
        "experience_in_years" = "",
        "skills"= [],
        "match_score" = "",
        "shortlist" = "YES/NO",
        "Justification":""
    }

    Resume:
"""

response = client.models.generate_content(
    model = "gemini-2.5-flash",
    contents = prompt + resume
)

print(response.text)