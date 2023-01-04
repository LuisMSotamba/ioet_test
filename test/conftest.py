import pytest
from app.employee.domain.Employee import Employee

@pytest.fixture
def employee() -> Employee:
    """
    Employe for testing
    """
    return Employee(name='Lionel')