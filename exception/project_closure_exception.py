class ProjectClosureException(Exception):
    def __init__(self, message="Project cannot be closed"):
        self.message = message
        super().__init__(message)