from typing import List, Any

from app.report.domain.ReportRepository import ReportRepository
from app.schedule.domain.Schedule import Schedule
from app.employee.domain.Employee import Employee

import datetime

class ConsoleReportRepository(ReportRepository):

    def __init__(self) -> None:
        self.results = []
    
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
            start_time = datetime.datetime.strptime(final_time[START_TIME_INDEX], "%H:%M") 
            end_time = datetime.datetime.strptime(final_time[END_TIME_INDEX], "%H:%M") 
            start_time_in_minutes = self.convert_time_to_minutes(start_time)
            end_time_in_minutes = self.convert_time_to_minutes(end_time)
            employee = Employee(name=user_name)
            schedule = Schedule(
                user=employee,
                start_time=start_time,
                end_time=end_time,
                name_day=day,
                start_time_in_minutes=start_time_in_minutes,
                end_time_in_minutes=end_time_in_minutes
            )
            schedule_list.append(schedule)
        
        return schedule_list
    
    def convert_time_to_minutes(self, time:datetime.time):
        MINUTES = 60
        return (time.hour * MINUTES) + time.minute

    def get_hours_in_minutes(self):

        DAYS_IN_WEEK = 7
        HOURS_IN_MINUTES = 1439

        days_hours:List[List[str]] = []
        i = 0
        day = -1

        while i < (HOURS_IN_MINUTES * DAYS_IN_WEEK):
            position = i % HOURS_IN_MINUTES
            i += 1
            if position == 0:
                day += 1
                days_hours.append([])
            days_hours[day].append('')

        return days_hours
            
            