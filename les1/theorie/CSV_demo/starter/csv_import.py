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
        try:
            raw_date, raw_amount = row
            orders.append(
                {"date": date.fromisoformat(raw_date), "amount": Decimal(raw_amount)}
            )
        except (ValueError, InvalidOperation):
            errors.append("Invalid record")
    return orders, errors
