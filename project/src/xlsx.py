def save_to_xlsx(file: str, columns: list, data: list):
    from openpyxl import Workbook
    from openpyxl.styles import Font

    wb = Workbook()
    ws = wb.active
    ws.title = "export"
    ws.append(columns)

    # customize cells
    for cell in ws["1:1"]:
        cell.font = Font(bold=True)

    for row in data:
        ws.append(row)

    # save
    wb.save(file)
