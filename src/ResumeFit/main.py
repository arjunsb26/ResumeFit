#!/usr/bin/env python
import shutil
from ResumeFit.crew import ResumeFitCrew

from langchain.document_loaders import PyPDFLoader

"""
Ideas:
- submit PDF, scrape job posting website
- integration with Word, Docs
"""

def run():
    """
    Run the resume fitting crew with hardcoded resume and job link.
    """

    """
    1. web-scrape job/comapany, find news, real-time
    """

    # Load your PDF file
    # This gives you one Document per page (we assume the resume is one page)

    # resume_loader = PyPDFLoader("inputs/jakes-resume.pdf").load()
    resume_loader = PyPDFLoader("inputs/arjun_S26_resume.pdf").load()

    resume_document = resume_loader[0]

    resume_content = resume_document.page_content


    job_url = "https://job-boards.greenhouse.io/ctccampusboard/jobs/4545359005"

    # Ensure resume is placed where the FileReadTool expects it
    # shutil.copy(resume_src_path, resume_dest_path)

    inputs = {
        "resume": resume_content,
        "job_url": job_url
    }

    ResumeFitCrew().crew().kickoff(inputs=inputs)


if __name__ == "__main__":
    run()
