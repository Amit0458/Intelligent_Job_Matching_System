# Intelligent Job Matching System

This project is a Flask-based web application that provides functionality for managing job postings, job seekers, hiring managers, job applications, and skill sets.

## ER Diagram

![ER Diagram](https://github.com/Amit0458/Intelligent_Job_Matching_System/blob/main/IJMS.png)

## Installation

### Prerequisites

Make sure you have Python installed. If not, download and install it from [python.org](https://www.python.org/downloads/).

### Setup

1. Clone the repository:
    ```bash
    git clone <repository_url>
    cd Intelligent_Job_Matching_System
    ```

2. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # For Linux/Mac
    # or
    .\venv\Scripts\activate   # For Windows
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Set up your environment variables in a `.env` file:
    ```plaintext
    DB_USERNAME=your_database_username
    DB_PASSWORD=your_database_password
    ```

2. Run the application:
    ```bash
    python run.py
    ```

## Endpoints

### Hiring Managers

- **Get all hiring managers**: `GET /hiring_managers/`
  - Returns a list of all hiring managers.
  
- **Get a specific hiring manager**: `GET /hiring_managers/<id>`
  - Returns details of a specific hiring manager identified by `id`.

- **Create a new hiring manager**: `POST /hiring_managers/`
  - Takes JSON data containing details of a new hiring manager and creates a new record.
  - Returns the newly created hiring manager's details.

- **Update an existing hiring manager**: `PUT /hiring_managers/<id>`
  - Takes JSON data containing updated details of a hiring manager identified by `id`.
  - Returns the updated hiring manager's details.

- **Delete a hiring manager**: `DELETE /hiring_managers/<id>`
  - Deletes the hiring manager identified by `id`.
  - Returns a success message if the deletion is successful.

### Job Applications

- **Create a new application for a job posting**: `POST /applications/<job_posting_id>`
  - Takes JSON data containing details of a new application for a specific job posting identified by `job_posting_id`.
  - Returns the details of the newly created application.

- **Get all applications for a specific job posting**: `GET /applications/<job_posting_id>`
  - Returns a list of all applications associated with the job posting identified by `job_posting_id`.

- **Get details of a specific application by ID**: `GET /applications/details/<application_id>`
  - Returns details of a specific application identified by `application_id`.

- **Update details of a specific application by ID**: `PATCH /applications/<application_id>`
  - Takes JSON data containing updated details of an application identified by `application_id`.
  - Returns the updated application's details.

- **Delete a specific application by ID**: `DELETE /applications/<application_id>`
  - Deletes the application identified by `application_id`.
  - Returns a success message if the deletion is successful.

### Job Postings

- **Get all job postings**: `GET /job_postings/`
  - Returns a list of all job postings.

- **Get a specific job posting by ID**: `GET /job_postings/<id>`
  - Returns details of a specific job posting identified by `id`.

- **Create a new job posting**: `POST /job_postings/`
  - Takes JSON data containing details of a new job posting.
  - Returns the details of the newly created job posting.

- **Update an existing job posting**: `PATCH /job_postings/<id>`
  - Takes JSON data containing updated details of a job posting identified by `id`.
  - Returns the updated job posting details.

- **Delete a job posting**: `DELETE /job_postings/<id>`
  - Deletes the job posting identified by `id`.
  - Returns a success message if the deletion is successful.

### Job Seekers

- **Get all job seekers**: `GET /job_seekers/`
  - Returns a list of all job seekers.

- **Get a specific job seeker by ID**: `GET /job_seekers/<id>`
  - Returns details of a specific job seeker identified by `id`.

- **Create a new job seeker profile**: `POST /job_seekers/`
  - Takes JSON data containing details of a new job seeker.
  - Returns the details of the newly created job seeker.

- **Update an existing job seeker profile**: `PATCH /job_seekers/<id>`
  - Takes JSON data containing updated details of a job seeker identified by `id`.
  - Returns the updated job seeker's details.

- **Delete a job seeker profile**: `DELETE /job_seekers/<id>`
  - Deletes the job seeker identified by `id`.
  - Returns a success message if the deletion is successful.

### Skill Sets

- **Create a new skill set linked to a specific job posting**: `POST /skill_sets/<job_posting_id>`
  - Takes JSON data containing details of a new skill set linked to a specific job posting identified by `job_posting_id`.
  - Returns the details of the newly created skill set.

- **Get all skill sets associated with a specific job posting**: `GET /skill_sets/<job_posting_id>`
  - Returns a list of all skill sets associated with the job posting identified by `job_posting_id`.

- **Get details of a specific skill set by ID**: `GET /skill_sets/details/<skill_set_id>`
  - Returns details of a specific skill set identified by `skill_set_id`.

- **Update details of a specific skill set by ID**: `PATCH /skill_sets/<skill_set_id>`
  - Takes JSON data containing updated details of a skill set identified by `skill_set_id`.
  - Returns the updated skill set's details.

- **Delete a specific skill set by ID**: `DELETE /skill_sets/<skill_set_id>`
  - Deletes the skill set identified by `skill_set_id`.
  - Returns a success message if the deletion is successful.

### Examples of JSON Objects for Each Table

#### Job Seeker JSON Object:

```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "phone_number": "1234567890",
  "status": 1,
  "skills": ["Python", "JavaScript"],
  "experience": "3 years",
  "bio": "Experienced software developer",
  "availability": "2023-12-01"
}
```
#### Hiring Manager JSON Object:

```json
{
  "title": "Software Engineer",
  "description": "Looking for a skilled software engineer...",
  "location": "Remote",
  "employment_type": "Full-time",
  "skills_required": ["Python", "JavaScript"],
  "posted_by": "John Smith"
}
```
#### Job Posting JSON Object :

```json
{
  "title": "Software Engineer",
  "description": "Looking for a skilled software engineer...",
  "location": "Remote",
  "employment_type": "Full-time",
  "skills_required": ["Python", "JavaScript"],
  "posted_by": "John Smith"
}

```
#### Skill Set JSON Object :

```json
{
  "name": "Python Development",
}

```
#### Job Application JSON Object :

```json
{
  "job_posting_id": 1,
  "job_seeker_id": 1,
  "status": "Pending",
  "application_date": "2023-12-10"
}
```

## Tech Stack

### Backend

- **Python 3**: Programming language used for the backend.
- **Flask**: Web framework
- **SQLAlchemy**: ORM for database interaction

### Frontend

- **Status**: Not implemented yet.

The project currently focuses on backend functionality and a frontend component has not been added. Plans may include the integration of a frontend to complement the backend APIs. Stay tuned for updates on the front-end development.


### Database

- **MySQL**: Database technology used for storage

### Other Tools/Libraries

- **MySQL**: Database used to store application data.
- **Flask-SQLAlchemy**: Flask extension that simplifies database integration.
- **dotenv**: Python library for managing environment variables.
- **Flask-CORS**: Flask extension for handling Cross-Origin Resource Sharing.



## Contributing

Thank you for considering contributing to our project! As this project is part of an assignment or guided learning, direct contributions via forks and pull requests might not be expected. However, contributions through feedback, ideas, or discussing improvements are highly encouraged and valued.

### How to Contribute

- **Feedback**: If you have any feedback, suggestions, or ideas to improve this project, feel free to create an issue detailing your thoughts. I appreciate all kinds of constructive feedback!

- **Ideas and Discussions**: Join the conversation by participating in discussions within existing issues. Share your ideas or thoughts on how to enhance the project.

- **Reporting Issues**: If you encounter any bugs, errors, or unexpected behavior, please report them by providing detailed information about the issue you faced.

### Code of Conduct

Please note that this project adheres to a Code of Conduct to ensure a welcoming and inclusive environment for all contributors.

### Get in Touch

If you have any questions or need further clarification, feel free to contact us via email or open an issue.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
