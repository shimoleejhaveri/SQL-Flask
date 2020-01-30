"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)

    grades = hackbright.get_grades_by_github(github)

    html = render_template('student_info.html', 
                            first=first, 
                            last=last, 
                            github=github,
                            grades=grades)

    # return "{} is the GitHub account for {} {}".format(github, first, last)

    return html

@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")

@app.route("/project")
def project_info():
    """Lists out project information for each project title"""

    title = request.args.get('title')

    title, description, max_grade = hackbright.get_project_by_title(title)

    project_title_html = render_template('project.html', title=title,
                                        description=description,
                                        max_grade=max_grade)

    return project_title_html


if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True, host="0.0.0.0")
