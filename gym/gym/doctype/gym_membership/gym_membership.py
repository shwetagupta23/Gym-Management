# Copyright (c) 2024, SHWE and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
from dateutil.relativedelta import relativedelta
from datetime import datetime


class GymMembership(Document):
    def before_save(self):
        start_date = datetime.strptime(self.start_date, "%Y-%m-%d") 
        end_date = datetime.strptime(self.end_date, "%Y-%m-%d")

        difference = relativedelta(end_date, start_date)
        self.how_many_months = difference.years * 12 + difference.months + (1 if difference.days > 0 else 0)

        self.total_amount = self.how_many_months * self.price
