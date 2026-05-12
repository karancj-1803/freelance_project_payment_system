class Payment:
    def __init__(
        self,
        payment_id=0,
        project_id=0,
        client_id=0,
        amount=0.0,
        payment_date="",
        payment_status="PENDING"
        ):
        
        if amount <= 0:
            raise ValueError("Amount cannot be less than or equal to zero.")
        
        self.payment_id = payment_id
        self.project_id = project_id
        self.client_id = client_id
        self.amount = amount
        self.payment_date = payment_date
        self.payment_status = payment_status