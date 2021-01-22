from rich.console import Console
from rich.table import Table

# def printTable(columns, data):
#     console = Console()
#     table = Table(header_style="bold")
#     for column in columns:
#         table.add_column(column)
#     for item in data:
#         table.add_row(*item)
#     console.print(table)

class TableIO():
    def __init__(self, cols: list):
        self.console = Console()
        self.table = Table()
        for col in cols:
            self.table.add_column(col)
    
    def append_row(self, row):
        self.table.add_row(*row)

    def print_table(self):
        self.console.print(self.table)
    