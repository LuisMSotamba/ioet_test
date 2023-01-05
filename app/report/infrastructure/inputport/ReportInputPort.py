from typing import List

from report.domain.Report import Report
import abc

class ReportInputPort(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def build_report(self, path:str) -> Report:
        raise NotImplementedError
    
    
