import frappe


def compare_fields(fields_1, fields_2):
    for field in fields_1:
        if not field_exists(field, fields_2):
            frappe.throw(field + ' is not found in the slave db')


def field_exists(field, fields):
    for data in fields:
        if data[0] == field[0] and data[1] == field[1]:
            return True
    return False