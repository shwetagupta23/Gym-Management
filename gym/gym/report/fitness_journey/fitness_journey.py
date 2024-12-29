# Copyright (c) 2024, SHWE and contributors
# For license information, please see license.txt


import frappe
from frappe.utils import flt

def execute(filters=None):
    columns = [
        {"label": "Date", "fieldname": "date", "fieldtype": "Date", "width": 120},
        {"label": "Weight (kg)", "fieldname": "weight", "fieldtype": "Float", "width": 100},
        {"label": "Calories Burned", "fieldname": "calories_burned", "fieldtype": "Float", "width": 120},
    ]
    
    # if not filters:
    #     filters = {}
        

    # customer = filters.get("customer")
    # if not customer:
    #     frappe.msgprint("Please select a customer to view their fitness journey.")
    #     return [], [], "No data to display. Please select a customer.", None

    # fitness_data = frappe.db.get_list(
    #     "Customer",
    #     fields=["date", "weight", "calories_burned"],
    #     filters={"customer": filters.customer},
    #     order_by="date asc"
    # )

    # if not fitness_data:
    #     frappe.msgprint(f"No fitness data found for the selected customer: {customer}")
    #     return [], [], "No data found for the selected customer.", None

    # columns = [
    #     {"label": "Date", "fieldname": "date", "fieldtype": "Date", "width": 120},
    #     {"label": "Weight (kg)", "fieldname": "weight", "fieldtype": "Float", "width": 100},
    #     {"label": "Calories Burned", "fieldname": "calories_burned", "fieldtype": "Float", "width": 120},
    # ]

    # data = []
    # weights = []
    # calories_burned = []
    # dates = []

    # for entry in fitness_data:
    #     data.append({
    #         "date": entry["date"],
    #         "weight": flt(entry["weight"]),
    #         "calories_burned": flt(entry["calories_burned"]),
    #     })
    #     weights.append(entry["weight"])
    #     calories_burned.append(entry["calories_burned"])
    #     dates.append(entry["date"])

    # chart = {
    #     "data": {
    #         "labels": dates,
    #         "datasets": [
    #             {"name": "Weight (kg)", "values": weights},
    #             {"name": "Calories Burned", "values": calories_burned},
    #         ]
    #     },
    #     "type": filters.get("chart_type", "line"),  # Default to "line" chart
    #     "colors": ["#3498db", "#e74c3c", "#2ecc71"]
    # }

    # return columns, data, None, chart

