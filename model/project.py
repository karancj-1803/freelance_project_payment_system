class Project:
    def __init__(
        self,
        project_id=0,
        client_id=0,
        freelance_id=0,
        project_name="",
        description="",
        deadline="",
        status="OPEN"
        ):
        self.project_id = project_id
        self.client_id = client_id
        self.freelance_id = freelance_id
        self.project_name = project_name
        self.description = description
        self.deadline = deadline
        self.status = status
    
    def __str__(self):
        return (
            f"Project ID: {self.project_id}"
            f"Client ID: {self.client_id}"
            f"Freelance ID: {self.freelance_id}"
            f"Project Name: {self.project_name}"
            f"Description: {self.description}"
            f"Deadline: {self.deadline}"
            f"Status: {self.status}"
        )