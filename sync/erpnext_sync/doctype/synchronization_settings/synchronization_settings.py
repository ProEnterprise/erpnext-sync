# -*- coding: utf-8 -*-
# Copyright (c) 2015, Bai Web and Mobile Lab and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from sync.frappeclient import FrappeClient
from sync.utils import compare_fields


class SynchronizationSettings(Document):

    def validate(self):
        if self.sync_mode == 'Slave':
            if not self.master_url or not self.username or not self.password:
                frappe.throw('URL, username and password should have a value')
            client = None
            try:
                client = FrappeClient(self.master_url, self.username, self.password)
            except:
                frappe.throw('Error connecting server')
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





