from dataclasses import dataclass
from typing import List

from schedule.domain.Schedule import Schedule
from report.infrastructure.inputport.ReportInputPort import ReportInputPort
from report.domain.ReportRepository import ReportRepository
from report.domain.Report import Report

import os

@dataclass
class ReportGeneration(ReportInputPort):

    reportRepository: ReportRepository

    def build_report(self, path: str) -> Report:
        report = Report(
            name=path,
            result='',
            version='1.0.0'
        )   
        if not os.path.isfile(path):
            print('The file is not valid')
            return report

        schedules = self.reportRepository.read(path)
        self.reportRepository.process(schedules)
        output = self.reportRepository.output()
        report.result = output
        return report