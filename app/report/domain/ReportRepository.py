from typing import List, Any

from app.schedule.domain.Schedule import Schedule

import abc

class ReportRepository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def read(self, path: str) -> List[Schedule]:
        raise NotImplementedError
    
    @abc.abstractmethod
    def process(self, schedules: List[Schedule]) -> Any:
        raise NotImplementedError
    
    @abc.abstractmethod
    def output(self) -> Any:
        raise NotImplementedError

