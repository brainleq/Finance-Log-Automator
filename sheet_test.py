import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(credentials)

sheet = client.open("UT Fall 2019 Scorecard").get_worksheet(1)

data = sheet.get_all_records()

row = sheet.row_values(375)

# 1     2         3            4       5       6       7   8     9      10
# date, category, description, record, T sign, P sign, DR, bank, venmo, cash
sheet.append_row([12/20, 'Dues', 'FA 19 (1)', '', 'Brian LeQuang', '', '', -3.00, ''])
