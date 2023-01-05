from employee.domain.Employee import Employee

import pytest
import os

@pytest.fixture
def employee() -> Employee:

    return Employee(name='Lionel')

@pytest.fixture
def input_file_3_rows(tmp_path):
    target_output = os.path.join(tmp_path,'input.txt')
    with open(target_output, 'w+') as f:

        f.write('RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00\n')
        f.write('ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00\n')
        f.write('ANDRES=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00\n')
    return target_output

@pytest.fixture
def input_file_5_rows(tmp_path):
    target_output = os.path.join(tmp_path,'input.txt')
    with open(target_output, 'w+') as f:

        f.write('RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00\n')
        f.write('ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00\n')
        f.write('ANDRES=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00\n')
        f.write('JAMILA=MO20:00-22:00,TH11:00-11:45,SU09:00-21:00\n')
        f.write('CAMILA=MO1:00-02:00,TH02:00-04:00,SU20:00-21:00\n')
    return target_output