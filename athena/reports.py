class Amounts:
    def __init__(self, amounts=[]):
        self.items = amounts

    def total(self):
        tot = 0

        for item in self.items:
            tot += item[1] # amount of the amount

        return round(tot)

class MonthData:
    def __init__(self, date, revs = Amounts(), direct_costs = Amounts(), operational_costs=Amounts()):
        self.date = date
        self.revs = revs
        self.direct_costs = direct_costs
        self.operational_costs = operational_costs
        self.report = self.to_report()
        

    def to_report(self):
        total_revs = self.revs.total()
        total_costs = self.direct_costs.total() + self.operational_costs.total()

        return {
            "month": [self.date.month, self.date.year],
            "revenues": {
                "items": self.revs.items,
                "total": total_revs
            },
            "costs": {
                "total": total_costs,
                "percent": round((total_costs * 100) / total_revs, 1),
                "direct": {
                    "total": self.direct_costs.total(),
                    "items": self.direct_costs.items,
                    "percent": round((self.direct_costs.total() * 100) / total_revs, 1)
                },
                "operational": {
                    "total": self.operational_costs.total(),
                    "items": self.operational_costs.items,
                    "percent": round((self.operational_costs.total() * 100) / total_revs, 1)
                }
            },
            "profits": {
                "total": total_revs - total_costs,
                "percent": round(((total_revs - total_costs) * 100) / total_revs, 1)
            }
        }
    
    def to_days_aware_report(self, days_opened):
        report = self.report

        report["revenues"]["perDay"] = round(report.get('revenues').get('total') / days_opened, 1)
        report["profits"]["perDay"] = round(report.get('profits').get('total') / days_opened, 1)
        return report
