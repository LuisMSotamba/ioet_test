from dataclasses import dataclass
from report.infrastructure.inputport.ReportInputPort import ReportInputPort

@dataclass
class ReportApi:

    reportInputPort: ReportInputPort

    def get_report(self, path: str):
        return self.reportInputPort.build_report(path)