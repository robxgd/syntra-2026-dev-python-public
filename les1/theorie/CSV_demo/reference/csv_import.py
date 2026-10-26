"""Import orders from a small CSV file."""

import csv
import io
from datetime import date
from decimal import Decimal, InvalidOperation


def import_orders(csv_text: str) -> tuple[list[dict], list[str]]:
    reader = csv.reader(io.StringIO(csv_text))
    header = next(reader, None)
    if header != ["date", "amount"]:
        raise ValueError("Expected CSV header: date,amount")

    orders: list[dict] = []
    errors: list[str] = []
    for row in reader:
        if not row or all(not cell.strip() for cell in row):
            continue

        line_number = reader.line_num
        if len(row) != 2:
            errors.append(f"Line {line_number}: expected 2 columns")
            continue

        raw_date, raw_amount = row
        try:
            parsed_date = date.fromisoformat(raw_date)
        except ValueError:
            errors.append(f"Line {line_number}: invalid date '{raw_date}'")
            continue

        try:
            parsed_amount = Decimal(raw_amount)
        except InvalidOperation:
            errors.append(f"Line {line_number}: invalid amount '{raw_amount}'")
            continue

        orders.append({"date": parsed_date, "amount": parsed_amount})
    return orders, errors
