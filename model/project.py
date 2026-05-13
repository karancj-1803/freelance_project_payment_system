class Project:
    def __init__(
        self,
        project_id=0,
        client_id=0,
        freelancer_id=0,
        project_name="",
        description="",
        deadline="",
        status="OPEN"
        ):
        self.project_id = project_id
        self.client_id = client_id
        self.freelancer_id = freelancer_id
        self.project_name = project_name
        self.description = description
        self.deadline = deadline
        self.status = status

    def __str__(self):
        return (
            f"Project ID: {self.project_id}\n"
            f"Client ID: {self.client_id}\n"
            f"Freelance ID: {self.freelancer_id}\n"
            f"Project Name: {self.project_name}\n"
            f"Description: {self.description}\n"
            f"Deadline: {self.deadline}\n"
            f"Status: {self.status}\n"
        )
