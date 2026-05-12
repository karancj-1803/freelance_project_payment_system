class Task:
    def __init__(
        self,
        task_id=0,
        project_id=0,
        task_name="",
        assigned_to="",
        due_date="",
        task_status="PENDING"
        ):
        if task_name.strip() == "":
            raise ValueError("Task name cannot be empty.")
        
        if assigned_to.strip() == "":
            raise ValueError("Assigned to cannot be empty.")
        
        self.task_id = task_id
        self.project_id = project_id
        self.task_name = task_name
        self.assigned_to = assigned_to
        self.due_date = due_date
        self.task_status = task_status
    
    def __str__(self):
        return (
            f"Task ID: {self.task_id}"
            f"Project ID: {self.project_id}"
            f"Task Name: {self.task_name}"
            f"Assigned to: {self.assigned_to}"
            f"Due Date: {self.due_date}"
            f"Task status: {self.task_status}"
        )