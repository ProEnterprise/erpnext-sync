# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "sync"
app_title = "ERPNext Sync"
app_publisher = "Bai Web and Mobile Lab"
app_description = "Sync Database Master/Slave"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "ccfiel@bai.ph"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/sync/css/sync.css"
# app_include_js = "/assets/sync/js/sync.js"

# include js, css files in header of web template
# web_include_css = "/assets/sync/css/sync.css"
# web_include_js = "/assets/sync/js/sync.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "sync.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "sync.install.before_install"
# after_install = "sync.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "sync.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

scheduler_events = {
    # "all": [
    #     "sync.tasks.all"
    # ],
    # "daily": [
    #     "sync.tasks.daily"
    # ],
    "hourly": [
        "sync.utils.sync_doctype"
    ],
    # "weekly": [
    #     "sync.tasks.weekly"
    # ],
    # "monthly": [
    #     "sync.tasks.monthly"
    # ]
}

# Testing
# -------

# before_tests = "sync.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "sync.event.get_events"
# }
