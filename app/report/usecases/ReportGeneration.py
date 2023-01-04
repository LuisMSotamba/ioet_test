from dataclasses import dataclass
from typing import List

from app.schedule.domain.Schedule import Schedule
from app.report.infrastructure.inputport.ReportInputPort import ReportInputPort
from app.report.domain.ReportRepository import ReportRepository

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