from app.report.domain.Report import Report

import uuid

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