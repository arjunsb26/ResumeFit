# import streamlit as st
# from hypermindz.crew import HypermindzCrew
# import PyPDF2
# import json

# st.set_page_config(page_title="Personalized Message Generator")
# st.title("Personalized Message Generator")

# # --- File upload section ---
# uploaded_file = st.file_uploader("Upload a file (e.g., cover letter)", type=["txt", "md", "pdf"])
# user_bio = ""
# if uploaded_file is not None:
#     if uploaded_file.type == "application/pdf":
#         reader = PyPDF2.PdfReader(uploaded_file)
#         user_bio = "\n".join(page.extract_text() for page in reader.pages if page.extract_text())
#     else:
#         user_bio = uploaded_file.read().decode("utf-8")

# # --- Prompt input ---
# prompt = st.text_area("Enter your request:", height=200)

# # --- UI rendering helpers ---
# def load_template(file_path):
#     with open(file_path, "r", encoding="utf-8") as file:
#         template = file.read()
#     return template

# def email_html(message, subject, recipient):
#     template = load_template("templates/email_ui.html")

#     subject = subject.replace("\"", "&quot;")
#     template = template.replace("{subject}", subject)

#     template = template.replace("{message}", message)
#     template = template.replace("{recipient}", recipient)
#     return template

# def linkedin_html(message, recipient, recipient_title):
#     template = load_template("templates/linkedin_ui.html")

#     template = template.replace("{message}", message)
#     template = template.replace("{recipient}", recipient)
#     template = template.replace("{recipient_title}", recipient_title)
#     return template

# def text_html(message, recipient):
#     template = load_template("templates/text_ui.html")

#     template = template.replace("{message}", message)
#     template = template.replace("{firstname}", recipient.split(' ')[0])
#     return template

# def x_html(message, recipient):
#     template = load_template("templates/x_ui.html")

#     template = template.replace("{message}", message)
#     template = template.replace("{contactname}", recipient)

#     return template

# def render_ui(json_dict):
#     format_ = json_dict["format_"].lower()

#     message = json_dict["message"]
#     message = message.replace("<", "&lt;").replace(">", "&gt;").replace("\"", "&quot;").replace("\n", "<br>")

#     subject = json_dict["subject"]
#     subject = subject.replace("<", "&lt;").replace(">", "&gt;").replace("\"", "&quot;").replace("\n", "<br>")

#     # sender = json_dict["sender"]
#     recipient = json_dict["recipient"]
#     recipient_title = json_dict["recipient_title"]

#     if format_ == "email": template = email_html(message, subject, recipient)
#     elif format_ == "linkedin": template = linkedin_html(message, recipient, recipient_title)
#     elif format_ == "text": template = text_html(message, recipient)
#     elif format_ == "x": template = x_html(message, recipient)

#     st.html(template)

# # --- Main Generation Button ---
# if st.button("Generate Message"):
#     if prompt.strip():
#         with st.spinner("Generating message..."):
#             inputs = {"bio": user_bio, "prompt": prompt}
#             crew_output = HypermindzCrew().crew().kickoff(inputs=inputs)

#             # Parse output
#             if isinstance(crew_output.json_dict, dict): render_ui(crew_output.json_dict)
#             else:
#                 format_, message = "text", str(crew_output.raw)
#                 st.write("Unknown format. Here's the message:")
#                 st.write(message)

#     else:
#         st.warning("Please enter a prompt first.")



# streamlit_app.py
import streamlit as st

import os
# import sys
# sys.path.append(os.path.abspath("src"))

from Hypermindz.crew import HypermindzCrew

st.set_page_config(page_title="Hypermindz Resume Grader")

st.title("🧠 Hypermindz Resume Grader")
st.markdown("Upload your resume in **Markdown (.md)** format to get AI-generated feedback.")

# File uploader
uploaded_file = st.file_uploader("Upload your resume (.md)", type=["md"])

# Output file path used by the crew
output_path = "outputs/feedback.txt"

# Run CrewAI when button is pressed
if uploaded_file is not None:
    with open("inputs/uploaded-resume.md", "wb") as f:
        f.write(uploaded_file.read())
    
    if st.button("Generate Feedback"):
        with st.spinner("Running the crew..."):
            crew = HypermindzCrew().crew()
            inputs = {"resume": "inputs/uploaded-resume.md"}  # If you need to pass this in
            crew.kickoff(inputs=inputs)

        # Display output if available
        if os.path.exists(output_path):
            with open(output_path, "r") as f:
                feedback = f.read()
            st.success("✅ Feedback generated!")
            st.text_area("AI Feedback", feedback, height=400)
        else:
            st.error("Something went wrong. Feedback file not found.")
