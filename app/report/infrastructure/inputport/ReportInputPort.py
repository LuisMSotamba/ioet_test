from typing import List

from app.schedule.domain.Schedule import Schedule

import abc

class ReportInputPort(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def build_report(self, path:str) -> List[Schedule]:
        raise NotImplementedError
    
    
