from typing import List, Any

from app.report.domain.ReportRepository import ReportRepository
from app.schedule.domain.Schedule import Schedule
from app.employee.domain.Employee import Employee

import datetime

class ConsoleReportRepository(ReportRepository):
    
    def read(self, path: str) -> List[Schedule]:
        USER_NAME = 0
        schedule_list:List[Schedule] = []

        with open(path, 'r') as file:
            for line in file.readlines():
                line = line.strip()
                name_separation_list:list = line.split("=")
                days_times:list = name_separation_list[1].split(",")
                schedule_list.extend(self._get_schedule(days_times, name_separation_list[USER_NAME])) 

        return schedule_list
    
    def process(self, schedules: List[Schedule]) -> None:
        pass
    
    def output(self) -> None:
        pass

    def _get_schedule(self, days_times: List[str], user_name: str) -> List[Schedule]:
        DAY = 2
        START_TIME_INDEX = 0
        END_TIME_INDEX = 1

        schedule_list: List[Schedule] = []
        for day_time in days_times:
            day = day_time[:DAY]
            time = day_time[DAY:]
            final_time = time.split("-")
            start_time = final_time[START_TIME_INDEX]
            end_time = final_time[END_TIME_INDEX]
            employee = Employee(name=user_name)
            schedule = Schedule(
                user=employee,
                start_time=datetime.datetime.strptime(start_time, "%H:%M"),
                end_time=datetime.datetime.strptime(end_time, "%H:%M"),
                name_day=day
            )
            schedule_list.append(schedule)
        
        return schedule_list
