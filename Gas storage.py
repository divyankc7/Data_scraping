from typing import Final

from bs4 import BeautifulSoup
import requests
import calendar
import pandas as pd

result = []

for year in range(2011, 2025):
    for month in range(1, 13):  # Note: Changed to 13 to include December
        month_str = f"{month:02d}"
        last_day = calendar.monthrange(year, month)[1]
        url = f"https://datahub.ren.pt/en/natural-gas/monthly-balance/?date={year}-{month_str}-{last_day}"

        page = requests.get(url, verify=False)
        soup = BeautifulSoup(page.text, 'html.parser')
        table = soup.find_all('table')[3]
        table_rows = table.find_all("td")
        Final_table_rows = [rows.text.strip() for rows in table_rows]


        injection_value = None
        input_value = None

        for x in range(len(Final_table_rows)):
            if Final_table_rows[x] == "INPUTS":
                input_value = Final_table_rows[x + 1]
            if Final_table_rows[x] == "Injection":
                injection_value = Final_table_rows[x + 1]
            if Final_table_rows[x] == "OUTPUTS":
                output_value = Final_table_rows[x + 1]
            if Final_table_rows[x] == "Withdrawal":
                Withdrawal_value = Final_table_rows[x + 1]
            if Final_table_rows[x] == "STORAGE":
                Storage_value = Final_table_rows[x + 1]
            if Final_table_rows[x] == "[%]":
                Percent_Value = Final_table_rows[x + 1]


        if injection_value is not None and input_value is not None:
            result.append({
                "Date": f"{year}-{month:02d}",  # Format month as two digits
                "Input": input_value,
                "Injection": injection_value,
                "Output": output_value,
                "Withdrawl": Withdrawal_value,
                "Storage": Storage_value,
                "[%]": Percent_Value
            })

        print(f"Date: {year}-{month:02d}, Input: {input_value}, Injection: {injection_value}, Output: {output_value}, Withdrawl: {Withdrawal_value}, Storage: {Storage_value}, [%]: {Percent_Value}")

result_df = pd.DataFrame(result)
result_df.to_excel(r"CC:\Users\divyank.chaudhary\PycharmProjects\Data scraping\storage.xlsx", index=False)