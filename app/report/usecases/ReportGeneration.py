from dataclasses import dataclass
from typing import List

from schedule.domain.Schedule import Schedule
from report.infrastructure.inputport.ReportInputPort import ReportInputPort
from report.domain.ReportRepository import ReportRepository

import os

@dataclass
class ReportGeneration(ReportInputPort):

    reportRepository: ReportRepository

    def build_report(self, path: str) -> List[Schedule]:
        if not os.path.isfile(path):
            print('The file is not valid')
            return None

        schedules = self.reportRepository.read(path)
        self.reportRepository.process(schedules)
        self.reportRepository.output()

        return schedules 