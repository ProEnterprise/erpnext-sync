# -*- coding: utf-8 -*-
# Copyright (c) 2015, Bai Web and Mobile Lab and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document


class SynchronizationDocType(Document):
    pass
    # def validate(self):
    #     mode = frappe.db.get_value("Synchronization Settings", None, "sync_mode")
    #     if mode == 'Slave':
    #         frappe.throw('Sync mode is slave. Add/Edit is not allowed')
