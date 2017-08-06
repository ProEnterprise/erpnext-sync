import frappe

record_per_page = 200


@frappe.whitelist(allow_guest=True)
def download_data(doc_name, date, page):
    fields = frappe.db.sql('''DESCRIBE %s''', doc_name)
    count = frappe.db.sql('''SELECT count(*) from %s WHERE creation>=%s and modified>=%s''', (doc_name, date, date))
    data = frappe.db.sql('''SELECT * from %s WHERE creation>=%s and modified>=%s LIMIT %s OFFSET %s''',
                         (doc_name, date, date, record_per_page, page * count[0][0]))

    return {"fields": fields, "data": data, "count": count[0][0]}
