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
            f"Client ID: {self.client_id}"
            f"Name: {self.name}"
            f"Email: {self.email}"
            f"Phone: {self.phone}"
            f"Company: {self.company}"
            f"Address: {self.address}"
        )