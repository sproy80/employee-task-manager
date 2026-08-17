

class AppException(Exception):
    def __init__(
        self,
        message: str,
        error_code: str,
        status_code: int = 400
    ):
        self.message = message
        self.error_code = error_code
        self.status_code = status_code

        super().__init__(message)


class EmployeeNotFoundException(AppException):
    def __init__(self, employee_id: int):
        super().__init__(
            message=f"Employee with ID {employee_id} was not found",
            error_code="EMPLOYEE_NOT_FOUND",
            status_code=404
        )