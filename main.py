from dao.freelancer_repository import FreelancerRepository
from dao.freelancer_repository_impl import FreelancerRepositoryImpl
from model.freelancer import Freelancer
from model.client import Client
from model.project import Project
from model.task import Task
from model.payment import Payment

repo = FreelancerRepositoryImpl()

payment1 = Payment(
    project_id=1,
    client_id=1,
    amount=50000,
    payment_date="2026-10-01",
    payment_status="PAID",
)

print(*repo.get_all_payments())
