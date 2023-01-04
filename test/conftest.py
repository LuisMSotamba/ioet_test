from app.employee.domain.Employee import Employee

import pytest
import os

@pytest.fixture
def employee() -> Employee:
    """
    Employe for testing
    """
    return Employee(name='Lionel')

@pytest.fixture
def input_file_3_rows(tmp_path):
    target_output = os.path.join(tmp_path,'input.txt')
    with open(target_output, 'w+') as f:
        # write stuff here
        f.write('RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00\n')
        f.write('ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00\n')
        f.write('ANDRES=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00\n')
    return target_output