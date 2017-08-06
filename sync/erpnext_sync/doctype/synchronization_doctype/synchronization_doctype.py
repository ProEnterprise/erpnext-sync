# -*- coding: utf-8 -*-
# Copyright (c) 2015, Bai Web and Mobile Lab and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document


class SynchronizationDocType(Document):

    def validate(self):
        mode = frappe.db.get_value("Synchronization Settings", None, "sync_mode")
        if mode == 'Slave':
            frappe.throw('Sync mode is slave. Add/Edit is not allowed')

        count = frappe.db.sql('''SELECT count(*) FROM `tabSynchronization DocType` WHERE sync_doctype=%s''', self.sync_doctype)
        if count[0][0] >= 1:
            frappe.throw(self.sync_doctype + ' is already exist')

    def on_trash(self):
        mode = frappe.db.get_value("Synchronization Settings", None, "sync_mode")
        if mode == 'Slave':
            frappe.throw('Sync mode is slave. Add/Edit is not allowed')
