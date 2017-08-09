import frappe
from sync.utils import sync_doctype
import time
import datetime


def daily():
    sync_mode = frappe.db.get_value("Synchronization Settings", None, "sync_mode")
    if sync_mode == 'Slave':
        sync_doctype('Synchronization DocType', '1976-01-01', 1)


def sync_download_doctypes():
    doctypes = frappe.db.sql('''SELECT sync_doctype FROM `tabSynchronization DocType` WHERE sync_direction="Download"''')
    for doctype in doctypes:
        date = frappe.db.sql('''SELECT date_last_sync, last_batch_sync, name FROM `tabSynchronization Date` WHERE sync_doctype=%s''', doctype[0])
        if not date:
            value_date = '1976-01-01'
            last_batch = 0
            sync = frappe.get_doc({
                "doctype": "tabSynchronization Date",
                "date_last_sync": value_date,
                "last_batch_sync": 0,
            })
            sync.insert(ignore_permissions=True)
        else:
            value_date = str(date[0][0])
            last_batch = int(date[0][1])
            sync = frappe.get_doc('Synchronization Date', date[0[2]])
        value = 0
        while value != 2:
            value = sync_doctype(doctype[0], value_date, last_batch)
            if value == 1:
                last_batch += 1
                sync.last_batch_sync = last_batch
                sync.save()

        if value_date == '1976-01-01':
            t_date = time.strftime("%d/%m/%Y")
        else:
            t_date = date(value_date) + datetime.timedelta(days=1)

        sync.last_batch_sync = t_date
        sync.last_batch_sync = 0
        sync.save()





