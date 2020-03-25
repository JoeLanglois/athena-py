#! .venv/bin/python

from athena.extractor import Extractor
from athena.reports import Amounts, MonthData
import json
import sys

def generate_report(file, days_opened=None):
    extractor = Extractor()
    extractor.parse_file(file)
    data = extractor.data

    month_data = MonthData(
        data.get('date'),
        revs=Amounts(data.get('revenues')),
        direct_costs=Amounts(data.get('direct')),
        operational_costs=Amounts(data.get('op')))

    report = None
    if not days_opened:
        report = month_data.to_report()
    else:
        report = month_data.to_days_aware_report(days_opened)

    return report    


if __name__ == "__main__":
    file_path = sys.argv[1]
    days_opened = None
    if(len(sys.argv) > 2):
        days_opened = int(sys.argv[2])

    report = generate_report(file_path, days_opened=days_opened)
    
    print(json.dumps(report, indent=1, ensure_ascii=False))
    