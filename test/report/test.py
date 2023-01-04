from app.report.domain.Report import Report
from app.report.infrastructure.outputadapter.ConsoleReportRepository import ConsoleReportRepository
from app.schedule.domain.Schedule import Schedule

import uuid
import datetime

def test_report_existing_id():
    test_id = uuid.uuid4().hex
    report = Report(
        name='Test report',
        version='1.0.0',
        id=test_id
    )

    assert report.id == test_id

def test_report_defaults():
    test_id = uuid.uuid4().hex
    report = Report(
        name='Test report',
        version='1.0.0',
    )

    assert report.id != test_id
    assert report.result == ''


def test_read_file(input_file_3_rows):
    console_repo = ConsoleReportRepository()
    response = console_repo.read(input_file_3_rows)
    assert isinstance(response,list), f'{response.__class__} is not instance of list' 
    assert isinstance(response[0],Schedule)


def test_convert_hour():
    console_repo = ConsoleReportRepository()
    time = datetime.datetime.strptime('12:32','%H:%M')
    expected_time = 752
    time_converted = console_repo.convert_time_to_minutes(time.time())

    assert expected_time==time_converted

def test_get_hours_array():
    console_repo = ConsoleReportRepository()
    array = console_repo.get_hours_in_minutes()
    expected_width = 1439
    expected_height = 7

    assert len(array) == expected_height
    assert len(array[0]) == expected_width