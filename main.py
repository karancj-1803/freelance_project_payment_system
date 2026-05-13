from dao.freelancer_repository import FreelancerRepository
from dao.freelancer_repository_impl import FreelancerRepositoryImpl
from model.freelancer import Freelancer
from model.client import Client
from model.project import Project
from model.task import Task
from model.payment import Payment


class FreelancerApp:
    def __init__(self):
        self.repo = FreelancerRepositoryImpl()

    def display_menu(self):
        print("==================================================")
        print("  FREELANCER PROJECT AND PAYMENT TRACKING SYSTEM  ")
        print("==================================================")
        print("  ---Freelancer Management---  ")
        print("  1.  Add Freelancer")
        print("  2.  Update Freelancer")
        print("  3.  Delete Freelancer")
        print("  4.  View Freelancer by ID")
        print("  ---Client Management---  ")
        print("  5.  Add Client")
        print("  6.  Update Client")
        print("  7.  Delete Client")
        print("  ---Project Management---  ")
        print("  8.  Create Project")
        print("  9.  Update Project Status")
        print("  10. View Projects by Freelancer")
        print("  11. View Projects by Client")
        print("  ---Task Management---  ")
        print("  12. Add Task")
        print("  13. Update Task Status")
        print("  14. View Tasks by Project")
        print("  ---Payment Management---  ")
        print("  15. Process Payment")
        print("  16. View Payments by Project")
        print("  ---System Management---  ")
        print("  17. View All Payments")
        print("  18. Exit")
        print("==================================================")

    def add_freelancer(self):
        print("---Add Freelancer---")
        name = input("Enter name: ").strip()
        email = input("Enter email: ").strip()
        phone = input("Enter phone: ").strip()
        skills = input("Enter skills: ").strip()
        experience_years = int(input("Enter years of experience:  ").strip())
        freelancer = Freelancer(
            name=name,
            email=email,
            phone=phone,
            skills=skills,
            experience_years=experience_years,
        )
        if self.repo.add_freelancer(freelancer):
            print("Freelancer added successfully!")
        else:
            print("Failed to add freelancer.")

    def update_freelancer(self):
        print("---Update Freelancer---")
        freelancer_id = int(input("Enter freelancer id: ").strip())
        name = input("Enter new name: ").strip()
        email = input("Enter new email: ").strip()
        phone = input("Enter new phone: ").strip()
        skills = input("Enter new skills: ").strip()
        experience_years = int(input("Enter new years of experience:  ").strip())
        freelancer = Freelancer(
            freelancer_id=freelancer_id,
            name=name,
            email=email,
            phone=phone,
            skills=skills,
            experience_years=experience_years,
        )
        if self.repo.update_freelancer(freelancer):
            print("Freelancer updated successfully!")
        else:
            print("Failed to update freelancer.")

    def delete_freelancer(self):
        print("---Delete Freelancer---")
        freelancer_id = int(input("Enter freelancer id: ").strip())
        if self.repo.delete_freelancer(freelancer_id):
            print("Freelancer deleted successfully!")
        else:
            print("Failed to delete freelancer.")

    def get_freelancer_by_id(self):
        print("---View Freelancer by ID---")
        freelancer_id = int(input("Enter freelancer id: ").strip())
        print(f"\n{self.repo.get_freelancer_by_id(freelancer_id)}")

    def add_client(self):
        print("---Add Client---")
        name = input("Enter name: ").strip()
        email = input("Enter email: ").strip()
        phone = input("Enter phone: ").strip()
        company = input("Enter company: ").strip()
        address = input("Enter address: ").strip()
        client = Client(
            name=name,
            email=email,
            phone=phone,
            company=company,
            address=address,
        )
        if self.repo.add_client(client):
            print("Client added successfully!")
        else:
            print("Failed to add client.")

    def update_client(self):
        print("---Update Client---")
        client_id = int(input("Enter client id: ").strip())
        name = input("Enter name: ").strip()
        email = input("Enter email: ").strip()
        phone = input("Enter phone: ").strip()
        company = input("Enter company: ").strip()
        address = input("Enter address: ").strip()
        client = Client(
            client_id=client_id,
            name=name,
            email=email,
            phone=phone,
            company=company,
            address=address,
        )
        if self.repo.update_client(client):
            print("Client updated successfully!")
        else:
            print("Failed to update client.")

    def delete_client(self):
        print("---Delete Client---")
        client_id = int(input("Enter client id: ").strip())
        if self.repo.delete_client(client_id):
            print("Client deleted successfully!")
        else:
            print("Failed to delete client.")

    def create_project(self):
        print("---Create Project---")
        client_id = int(input("Enter client id:"))
        freelancer_id = int(input("Enter freelancer id:"))
        project_name = input("Enter project name: ").strip()
        description = input("Enter description: ").strip()
        deadline = input("Enter deadline: ").strip()
        project = Project(
            client_id=client_id,
            freelancer_id=freelancer_id,
            project_name=project_name,
            description=description,
            deadline=deadline,
        )
        if self.repo.create_project(project):
            print("Project created successfully with OPEN status!")
        else:
            print("Failed to create project.")

    def update_project_status(self):
        print("---Update Project Status---")
        project_id = int(input("Enter project id: "))
        print("1.  OPEN 2.  IN PROGRESS 3.  COMPLETED 4.  CANCELLED")
        option = int(input("Enter option: "))
        statuses = {1: "OPEN", 2: "IN PROGRESS", 3: "COMPLETED", 4: "CANCELLED"}
        status = statuses[option]
        if self.repo.update_project_status(project_id, status):
            print(f"Project status updated to {status} succesfully!")
        else:
            print("Failed to update project status.")

    def get_projects_by_freelancer(self):
        print("---View Projects by Freelancer---")
        freelancer_id = int(input("Enter freelancer id:"))
        projects = self.repo.get_projects_by_freelancer(freelancer_id)
        if projects:
            print(f"PROJECTS FOR FREELANCER {freelancer_id}")
            for project in projects:
                print("\n---------------------------------------------")
                print(
                    f"ID={project.project_id} ClientID={project.client_id} Name={project.project_name} Deadline={project.deadline} Status={project.status}"
                )
                print("---------------------------------------------\n")
        else:
            print(f"Freelancer with ID {freelancer_id} not found.")

    def get_projects_by_client(self):
        print("---View Projects by Client---")
        client_id = int(input("Enter client id:"))
        projects = self.repo.get_projects_by_client(client_id)
        if projects:
            print(f"PROJECTS FOR CLIENT {client_id}")
            for project in projects:
                print("\n---------------------------------------------")
                print(
                    f"ID={project.project_id} FreelancerID={project.freelancer_id} Name={project.project_name} Deadline={project.deadline} Status={project.status}"
                )
                print("---------------------------------------------\n")
        else:
            print(f"Client with ID {client_id} not found.")

    def add_task(self):
        print("---Add Task---")
        project_id = int(input("Enter project id:"))
        task_name = input("Enter task name: ").strip()
        assigned_to = input("Enter assigned to: ").strip()
        due_date = input("Enter duedate: ").strip()
        print("1.  PENDING 2.  IN PROGRESS 3.  COMPLETED 4.  CANCELLED")
        option = int(input("Enter option: "))
        statuses = {1: "PENDING", 2: "IN PROGRESS", 3: "COMPLETED", 4: "CANCELLED"}
        status = statuses[option]
        task = Task(
            project_id=project_id,
            task_name=task_name,
            assigned_to=assigned_to,
            due_date=due_date,
            task_status=status,
        )
        if self.repo.add_task(task):
            print("Task added successfully!")
        else:
            print("Failed to add task.")

    def update_task_status(self):
        print("---Update Task Status---")
        task_id = int(input("Enter task id: "))
        print("1.  PENDING 2.  IN PROGRESS 3.  COMPLETED 4.  CANCELLED")
        option = int(input("Enter option: "))
        statuses = {1: "PENDING", 2: "IN PROGRESS", 3: "COMPLETED", 4: "CANCELLED"}
        status = statuses[option]
        if self.repo.update_task_status(task_id, status):
            print(f"Task status updated to {status} succesfully!")
        else:
            print("Failed to update task status.")

    def get_tasks_by_project(self):
        print("---View Tasks by Projects---")
        project_id = int(input("Enter project id:"))
        tasks = self.repo.get_tasks_by_project(project_id)
        if tasks:
            fmt = "{:<10} {:<50} {:<20} {:<15} {:<15}"
            print(
                fmt.format("Task ID", "Task Name", "Assigned To", "Due Date", "Status")
            )
            print("-" * 120)
            for task in tasks:
                print(
                    fmt.format(
                        task.task_id,
                        task.task_name,
                        task.assigned_to,
                        task.due_date,
                        task.task_status,
                    )
                )
        else:
            print(f"Project with ID {project_id} not found.")

    def process_payment(self):
        print("---Process Payment---")
        project_id = int(input("Enter project id:"))
        client_id = int(input("Enter client id: ").strip())
        amount = float(input("Enter Amount: "))
        payment_date = input("Enter payment date: ").strip()
        payement_status = input("Enter payement status: ").strip()
        payment = Payment(
            project_id=project_id,
            client_id=client_id,
            amount=amount,
            payment_date=payment_date,
            payment_status=payement_status
        )
        if self.repo.process_payment(payment):
            print("Payment processed successfully!")
        else:
            print("Failed to process payment.")

    def get_payments_by_project(self):
        print("---View Payments by Project---")
        project_id = int(input("Enter project id:"))
        payments = self.repo.get_payments_by_project(project_id)
        if payments:
            fmt = "{:<10} {:<20} {:<20} {:<15} {:<15}"
            print(
                fmt.format("Pay ID", "Client ID", "Amount", "Date", "Status")
            )
            print("-" * 100)
            for payment in payments:
                print(
                    fmt.format(
                        payment.payment_id,
                        payment.client_id,
                        payment.amount,
                        payment.payment_date,
                        payment.payment_status,
                    )
                )
        else:
            print(f"Project with ID {project_id} not found.")

    def get_all_payments(self):
        print("---View All Payments---")
        payments = self.repo.get_all_payments()
        if payments:
            fmt = "{:<10} {:<20} {:<20} {:<15} {:<15}"
            print(
                fmt.format("Pay ID", "Client ID", "Amount", "Date", "Status")
            )
            print("-" * 80)
            for payment in payments:
                print(
                    fmt.format(
                        payment.payment_id,
                        payment.client_id,
                        payment.amount,
                        payment.payment_date,
                        payment.payment_status,
                    )
                )
        else:
            print(f"No payments found.")
        

    def run(self):
        while True:
            self.display_menu()
            try:
                choice = int(input("Enter your choice (1-18): "))
                print()
                if choice == 1:
                    self.add_freelancer()
                elif choice == 2:
                    self.update_freelancer()
                elif choice == 3:
                    self.delete_freelancer()
                elif choice == 4:
                    self.get_freelancer_by_id()
                elif choice == 5:
                    self.add_client()
                elif choice == 6:
                    self.update_client()
                elif choice == 7:
                    self.delete_client()
                elif choice == 8:
                    self.create_project()
                elif choice == 9:
                    self.update_project_status()
                elif choice == 10:
                    self.get_projects_by_freelancer()
                elif choice == 11:
                    self.get_projects_by_client()
                elif choice == 12:
                    self.add_task()
                elif choice == 13:
                    self.update_task_status()
                elif choice == 14:
                    self.get_tasks_by_project()
                elif choice == 15:
                    self.process_payment()
                elif choice == 16:
                    self.get_payments_by_project()
                elif choice == 17:
                    self.get_all_payments()
                elif choice == 18:
                    print("Thank you for using Freelancer Project and Payment Tracking System.Goodbye!")
                    self.repo.close()
                    break
            except ValueError :
                print("Invalid input!")
            except Exception as e:
                print("Error: ", e)

if __name__ == "__main__":
    app = FreelancerApp()
    app.run()
