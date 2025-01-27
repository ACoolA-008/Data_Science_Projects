INSERT INTO Candidates (first_name, last_name, email, phone, resume_link)
VALUES
    ('John', 'Doe', 'john.doe@example.com', '123-456-7890', 'link_to_resume_1'),
    ('Jane', 'Smith', 'jane.smith@example.com', '987-654-3210', 'link_to_resume_2'),
    ('Michael', 'Brown', 'michael.brown@example.com', '555-678-1234', 'link_to_resume_3');

INSERT INTO Application (application_date, application_status, notes, candidate_id, job_id)
VALUES
    ('2025-01-20', 'Applied', 'Strong data analysis skills.', 1, 1),
    ('2025-01-21', 'Interviewing', 'Scheduled for the first round.', 2, 2),
    ('2025-01-22', 'Hired', 'Accepted offer.', 3, 3);

INSERT INTO JOB (POSTED_DATE, DEPARTMENT, JOB_TITLE, JOB_DESCRIPTIONS, SALARY_RANGE, LOCATION, PRIORITY, STATUS)
VALUES
    ('2025-01-15', 'IT', 'Data Analyst', 'Analyze data to generate insights.', '50K-70K', 'New York', 'High', 'Open');
