#!/usr/bin/env python
import shutil
from ResumeFit.crew import ResumeFitCrew

def run():
    """
    Run the resume fitting crew with hardcoded resume and job link.
    """

    resume_src_path = "inputs/jakes-resume.md"
    resume_dest_path = "inputs/better-resume.md"
    job_url = "https://job-boards.greenhouse.io/ctccampusboard/jobs/4545359005"

    # Ensure resume is placed where the FileReadTool expects it
    shutil.copy(resume_src_path, resume_dest_path)

    inputs = {
        "resume_path": resume_dest_path,
        "job_url": job_url
    }

    ResumeFitCrew().crew().kickoff(inputs=inputs)


if __name__ == "__main__":
    run()
