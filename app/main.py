import sys
print(sys.path)

from report.usecases.ReportGeneration import ReportGeneration
from report.infrastructure.inputadapter.ReportApi import ReportApi
from report.infrastructure.outputadapter.ConsoleReportRepository import ConsoleReportRepository

if __name__ == '__main__':
    print("Working!")
    while True:
        print("===== MENU =====")
        print("1. Enter the name of the file")
        print("2. Exit")
        option = input("> ")
        match option:
            case "1":
                path = input("File name: ")
                consoleRepository = ConsoleReportRepository()
                reportUseCase = ReportGeneration(consoleRepository)
                reportApi = ReportApi(reportUseCase)
                reportApi.get_report(path)
            case "2":
                break
            case _:
                print("Puuum!")
        
