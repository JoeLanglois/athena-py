import sqlite3
import json

class ReportStore:
    def __init__(self):
        self.conn = sqlite3.connect('./data/reports.sqlite')
        self.conn.execute("""CREATE TABLE IF NOT EXISTS reports (
            id integer primary key,
            month integer not null,
            year integer not null,
            report text not null
        );""")
    
    def store(self, report, month, year=2020):
        report_json = json.dumps(report)
        cursor = self.conn.execute("""
            INSERT INTO reports (month, year, report) VALUES (?,?,?);
        """, (month, year, report_json))

        self.conn.commit()

    def get_report(self, month, year):
        c = self.conn.cursor()
        c.execute("""
            SELECT month, year, report from reports
            WHERE month = ? AND year = ?;""", (month, year))
        data = c.fetchone()
        return json.loads(data[2])