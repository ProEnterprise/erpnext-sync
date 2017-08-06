# -*- coding: utf-8 -*-
# Copyright (c) 2015, Bai Web and Mobile Lab and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from sync.frappeclient import FrappeClient
from frappe.utils.password import get_decrypted_password


class SynchronizationSettings(Document):

    def validate(self):
        if self.sync_mode == 'Slave':
            if not self.master_url or not self.username or not self.password:
                frappe.throw('URL, username and password should have a value')

            password = get_decrypted_password(self.doctype, self.doctype, 'password', False)

            try:
                FrappeClient(self.master_url, self.username, password)
            except:
                frappe.throw('Error connecting server')






