import frappe
from sync.frappeclient import FrappeClient


def compare_fields(fields_1, fields_2):
    for field in fields_1:
        if not field_exists(field, fields_2):
            frappe.throw(field + ' is not found in the slave db')


def field_exists(field, fields):
    for data in fields:
        if data[0] == field[0] and data[1] == field[1]:
            return True
    return False


def sync_doctype():
    master_url = frappe.db.get_value("Synchronization Settings", None, "master_url")
    username = frappe.db.get_value("Synchronization Settings", None, "username")
    password = frappe.db.get_value("Synchronization Settings", None, "password")
    sync_mode = frappe.db.get_value("Synchronization Settings", None, "sync_mode")

    if sync_mode == 'Slave':
        client = FrappeClient(master_url, username, password)

        if client:
            doc_name = 'tabSynchronization DocType'
            doctypes = client.get_api("sync.rest.download_data?doc_name=" + doc_name + "&date=2013-01-01&page=1")
            fields = frappe.db.sql('DESCRIBE `' + doc_name + '`')
            compare_fields(doctypes['fields'], fields)

            str_field = ''
            for field in doctypes['fields']:
                if not str_field:
                    str_field = str(field[0])
                else:
                    str_field = str_field + ', ' + str(field[0])

            frappe.db.sql('DELETE FROM `' + doc_name + '`')
            for datas in doctypes['data']:
                str_data = ''
                for record in datas:
                    if str(record) == 'None':
                        value = 'NULL'
                    else:
                        value = "'" + str(record) + "'"
                    if not str_data:
                        str_data = value
                    else:
                        str_data = str_data + ', ' + value

                sql_statement = 'INSERT INTO `' + doc_name + '` (' + str_field + ') VALUES (' + str_data + ')'
                frappe.db.sql(sql_statement)
