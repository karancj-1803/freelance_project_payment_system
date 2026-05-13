class ClientNotFoundException(Exception):
    def __init__(self, message="Client not found."):
        self.message = message
        super().__init__(message)