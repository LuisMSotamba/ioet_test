from typing import List, Any

from report.domain.ReportRepository import ReportRepository
from schedule.domain.Schedule import Schedule
from employee.domain.Employee import Employee

import datetime
import uuid

class ConsoleReportRepository(ReportRepository):

    def __init__(self) -> None:
        self.results = {}
    
    def read(self, path: str) -> List[Schedule]:

        USER_NAME = 0
        SCHEDULE = 1
        schedule_list:List[Schedule] = []

        with open(path, 'r') as file:

            lines = file.readlines()
            if len(lines)<5:
                print('The file contains less than 5 registers') 
                return []
                
            for line in lines:
                line = line.strip()
                name_separation_list:list = line.split("=")
                days_times:list = name_separation_list[SCHEDULE].split(",")
                employee = Employee(name=name_separation_list[USER_NAME], id=uuid.uuid4().hex)
                schedule_list.extend(self.get_schedule(days_times, employee)) 

        return schedule_list
    
    def process(self, schedules: List[Schedule]):

        schedules.sort(key=lambda item: item.start_time_in_minutes)
        employee_matching = {}
        tam_schedules = len(schedules)

        for i in range(tam_schedules):
            for j in range(i+1, tam_schedules):
                if schedules[i].end_time_in_minutes >= schedules[j].start_time_in_minutes and schedules[i].name_day == schedules[j].name_day:
                    key = f"{schedules[i].user.name} - {schedules[j].user.name} | {schedules[j].user.name} - {schedules[i].user.name}"
                    if not key in employee_matching:
                        employee_matching[key] = 0
                    employee_matching[key] += 1

        self.results = employee_matching


    def output(self):
        output = ''
        for [key, value] in self.results.items():
            output = output + f"{key} : {value}\n"
        
        return output

    def get_schedule(self, days_times: List[str], employee: Employee) -> List[Schedule]:

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
