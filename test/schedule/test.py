from app.schedule.domain.Schedule import Schedule

import uuid
import datetime

def test_schedule_existing_id(employee):
    test_id = str(uuid.uuid4().hex)
    time = datetime.datetime.now()
    schedule = Schedule(
        id=test_id,
        name_day='MO',
        start_time=time,
        end_time=time,
        user=employee,
        start_time_in_minutes=0,
        end_time_in_minutes=0
    )
    
    assert schedule.id == test_id

def test_schedule_defaults(employee):
    test_id = str(uuid.uuid4().hex)
    time = datetime.datetime.now()
    schedule = Schedule(
        name_day='MO',
        start_time=time,
        end_time=time,
        user=employee,
        start_time_in_minutes=0,
        end_time_in_minutes=0
    )

    assert schedule.id != test_id