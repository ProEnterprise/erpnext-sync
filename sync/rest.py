import frappe

record_per_page = 200


@frappe.whitelist(allow_guest=True)
def download_data(doc_name, date, page):
    fields = frappe.db.sql('DESCRIBE `' + doc_name + '`')
    count = frappe.db.sql('SELECT count(*) from `' + doc_name + '` WHERE creation>=%s and modified>=%s', (date, date))
    start = (int(page) - 1) * record_per_page
    data = frappe.db.sql('SELECT * from `' + doc_name +
                         '` WHERE creation>=%s and modified>=%s LIMIT ' +
                         str(record_per_page) + ' OFFSET ' + str(start), (date, date))

    return {"fields": fields, "data": data, "count": count[0][0]}
