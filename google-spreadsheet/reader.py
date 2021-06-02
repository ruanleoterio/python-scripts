import os
import gspread


def read_spreadsheet(filename='./credentials.json'):
    spreadsheet = gspread.service_account(filename=filename)
    spreadsheet_key = os.environ.get('SPREADSHEET_KEY', None)
    if spreadsheet_key:
        customer_database = spreadsheet.open_by_key(spreadsheet_key)
        sheet = customer_database.get_worksheet(3)
        [print(line) for line in sheet.get_all_values()]


if __name__ == '__main__':
    read_spreadsheet()
