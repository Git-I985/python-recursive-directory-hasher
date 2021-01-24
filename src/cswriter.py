import csv

class CsvWriter:
    def __init__(self, fname='export.csv'):
        self.f = open(fname, 'w', newline='')
        self.cw = csv.writer(self.f, delimiter=';')

    def set_columns(self, columns: list):
        self.cw.writerow(columns)
    
    def write_row(self, row: list):
        self.cw.writerow(row)
        
    def save(self):
        self.f.close()
