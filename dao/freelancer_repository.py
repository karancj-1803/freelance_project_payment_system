from abc import ABC, abstractmethod

class FreelancerRepository(ABC):
    @abstractmethod
    def add_freelancer(self, freelancer):
        pass
    
    @abstractmethod
    def update_freelancer(self, freelancer):
        pass
    
    @abstractmethod
    def delete_freelancer(self, freelancer_id):
        pass
    
    @abstractmethod
    def get_freelancer_by_id(self, freelancer_id):
        pass
    
    @abstractmethod
    def add_client(self, client):
        pass
    
    @abstractmethod
    def update_client(self, client):
        pass
    
    @abstractmethod
    def delete_client(self, client_id):
        pass
    
    @abstractmethod
    def get_client_by_id(self, client_id):
        pass
    
    @abstractmethod
    def create_project(self, project):
        pass
    
    @abstractmethod
    def update_project_status(self, project_id, status):
        pass
    
    @abstractmethod
    def get_projects_by_freelancer(self, freelancer_id):
        pass
    
    @abstractmethod
    def get_projects_by_client(self, client_id):
        pass
    
    @abstractmethod
    def add_task(self, task):
        pass
    
    @abstractmethod
    def update_task_status(self, task_id, task_status):
        pass
    
    @abstractmethod
    def get_tasks_by_project(self, project_id):
        pass
    
    # @abstractmethod
    # def process_payment(self, payment):
    #     pass
    
    # @abstractmethod
    # def get_payments_by_project(self, project_id):
    #     pass
    
    # @abstractmethod
    # def get_all_payments(self):
    #     pass