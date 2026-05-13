class FreelancerNotFoundException(Exception):
    def __init__(self, message="Freelancer not found."):
        self.message = message
        super().__init__(message)