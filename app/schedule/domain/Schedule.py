from dataclasses import dataclass, field
from datetime import datetime

from employee.domain.Employee import Employee

import uuid

@dataclass
class Schedule:

    user: Employee
    start_time_in_minutes: int
    end_time_in_minutes: int
    start_time: datetime
    end_time: datetime
    name_day: str
    id: str = field(default_factory=lambda:uuid.uuid4().hex)
