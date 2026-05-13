class Client:
    def __init__(
        self,
        client_id=0,
        name="",
        email="",
        phone="",
        company="",
        address=""
        ):
        self.client_id = client_id
        self.name = name
        self.email = email
        self.phone = phone
        self.company = company 
        self.address = address
    
    def __str__(self):
        return (
            f"Client ID: {self.client_id}\n"
            f"Name: {self.name}\n"
            f"Email: {self.email}\n"
            f"Phone: {self.phone}\n"
            f"Company: {self.company}\n"
            f"Address: {self.address}\n"
        )