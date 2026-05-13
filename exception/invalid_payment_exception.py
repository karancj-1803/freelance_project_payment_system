class InvalidPaymentException(Exception):
    def __init__(self, message="Invalid Payment."):
        self.message = message
        super().__init__(message)