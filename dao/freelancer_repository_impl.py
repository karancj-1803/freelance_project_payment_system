from dao.freelancer_repository import FreelancerRepository

from exception.client_not_found_exception import ClientNotFoundException
from exception.freelancer_not_found_exception import FreelancerNotFoundException
from exception.invalid_payment_exception import InvalidPaymentException
from exception.project_closure_exception import ProjectClosureException

from model.freelancer import Freelancer
from model.client import Client
from model.project import Project
from model.task import Task
from model.payment import Payment

from util.db_connection import DBConnection


class FreelancerRepositoryImpl(FreelancerRepository):
    def __init__(self):
        self.con = DBConnection.get_connection()
        self.cursor = self.con.cursor()

    def close(self):
        self.con = DBConnection.close_connection()

    def add_freelancer(self, freelancer):
        try:
            query = "INSERT INTO Freelancers(name, email, phone, skills, experience_years) VALUES(?,?,?,?,?)"
            values = (
                freelancer.name,
                freelancer.email,
                freelancer.phone,
                freelancer.skills,
                freelancer.experience_years,
            )
            self.cursor.execute(query, values)
            self.con.commit()
            return True
        except Exception as e:
            print("Error: ", e)
            return False

    def get_freelancer_by_id(self, freelancer_id):
        query = "SELECT * FROM Freelancers WHERE freelancer_id = ?"
        self.cursor.execute(query, (freelancer_id,))
        row = self.cursor.fetchone()
        if row:
            return Freelancer(*row)
        else:
            raise FreelancerNotFoundException()

    def update_freelancer(self, freelancer):
        old_freelancer = self.get_freelancer_by_id(freelancer.freelancer_id)

        query = "UPDATE Freelancers SET name = ?, email = ?, phone = ?, skills = ?, experience_years = ? WHERE freelancer_id = ?"
        values = (
            freelancer.name,
            freelancer.email,
            freelancer.phone,
            freelancer.skills,
            freelancer.experience_years,
            freelancer.freelancer_id,
        )
        self.cursor.execute(query, values)
        self.con.commit()
        return True

    def delete_freelancer(self, freelancer_id):
        old_freelancer = self.get_freelancer_by_id(freelancer_id)
        query = "DELETE FROM Freelancers WHERE freelancer_id = ?"
        values = (freelancer_id,)
        self.cursor.execute(query, values)
        self.con.commit()
        return True

    def add_client(self, client):
        try:
            query = "INSERT INTO Clients(name, email, phone, company, address) VALUES(?,?,?,?,?)"
            values = (
                client.name,
                client.email,
                client.phone,
                client.company,
                client.address,
            )
            self.cursor.execute(query, values)
            self.con.commit()
            return True
        except Exception as e:
            print("Error: ", e)
            return False

    def get_client_by_id(self, client_id):
        query = "SELECT * FROM Clients WHERE client_id = ?"
        self.cursor.execute(query, (client_id,))
        row = self.cursor.fetchone()
        if row:
            return Client(*row)
        else:
            raise ClientNotFoundException()

    def update_client(self, client):
        old_client = self.get_client_by_id(client.client_id)

        query = "UPDATE Clients SET name = ?, email = ?, phone = ?, company = ?, address = ? WHERE client_id = ?"
        values = (
            client.name,
            client.email,
            client.phone,
            client.company,
            client.address,
            client.client_id,
        )
        self.cursor.execute(query, values)
        self.con.commit()
        return True

    def delete_client(self, client_id):
        old_client = self.get_client_by_id(client_id)
        query = "DELETE FROM Clients WHERE client_id = ?"
        values = (client_id,)
        self.cursor.execute(query, values)
        self.con.commit()
        return True

    def create_project(self, project):
        old_freelancer = self.get_freelancer_by_id(project.freelancer_id)
        old_client = self.get_client_by_id(project.client_id)
        try:
            query = "INSERT INTO Projects(client_id, freelancer_id, project_name, description, deadline, status) VALUES(?,?,?,?,?,?)"
            values = (
                project.client_id,
                project.freelancer_id,
                project.project_name,
                project.description,
                project.deadline,
                project.status,
            )
            self.cursor.execute(query, values)
            self.con.commit()
            return True
        except Exception as e:
            print("Error: ", e)
            return False

    def update_project_status(self, project_id, status):
        statuses = ["OPEN", "IN PROGRESS", "COMPLETED", "CANCELLED"]
        if status not in statuses:
            raise ProjectClosureException("Invalid status type.")

        query = "UPDATE Projects SET status = ? WHERE project_id = ?"
        values = (status, project_id)
        self.cursor.execute(query, values)
        self.con.commit()
        return True

    def get_projects_by_freelancer(self, freelancer_id):
        query = "SELECT * FROM Projects WHERE freelancer_id = ?"
        self.cursor.execute(query, (freelancer_id,))
        rows = self.cursor.fetchall()
        if rows:
            projects = [Project(*row) for row in rows]
            return projects
        else:
            raise FreelancerNotFoundException()
        
    def get_projects_by_client(self, client_id):
        query = "SELECT * FROM Projects WHERE client_id = ?"
        self.cursor.execute(query, (client_id,))
        rows = self.cursor.fetchall()
        if rows:
            projects = [Project(*row) for row in rows]
            return projects
        else:
            raise ClientNotFoundException()