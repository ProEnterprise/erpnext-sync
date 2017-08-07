import frappe
from sync.utils import sync_doctype


def daily():
    sync_mode = frappe.db.get_value("Synchronization Settings", None, "sync_mode")
    if sync_mode == 'Slave':
        sync_doctype('Synchronization DocType', '1976-01-01', 1)
