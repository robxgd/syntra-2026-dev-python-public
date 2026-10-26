import unittest
from datetime import date
from decimal import Decimal

from csv_import import import_orders


class ImportOrdersTests(unittest.TestCase):
    def test_valid_rows(self):
        orders, errors = import_orders("date,amount\n2026-10-01,12.50\n")
        self.assertEqual(orders, [{"date": date(2026, 10, 1), "amount": Decimal("12.50")}])
        self.assertEqual(errors, [])

    def test_blank_line_is_ignored(self):
        orders, errors = import_orders("date,amount\n2026-10-01,12.50\n\n2026-10-02,7.00\n")
        self.assertEqual(len(orders), 2)
        self.assertEqual(errors, [])

    def test_invalid_date_reports_physical_line(self):
        orders, errors = import_orders("date,amount\n\n2026-02-30,12.50\n")
        self.assertEqual(orders, [])
        self.assertEqual(errors, ["Line 3: invalid date '2026-02-30'"])

    def test_invalid_amount_reports_physical_line(self):
        orders, errors = import_orders("date,amount\n2026-10-01,abc\n")
        self.assertEqual(orders, [])
        self.assertEqual(errors, ["Line 2: invalid amount 'abc'"])

    def test_bad_header_still_fails(self):
        with self.assertRaisesRegex(ValueError, "Expected CSV header"):
            import_orders("when,amount\n2026-10-01,12.50\n")


if __name__ == "__main__":
    unittest.main()
