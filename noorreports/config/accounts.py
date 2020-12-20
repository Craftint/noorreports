from __future__ import unicode_literals
from frappe import _
import frappe


def get_data():
	config = [
		{
			"label": _("Accounts Receivable"),
			"items": [
				{
					"type": "report",
					"name": "Statement Of Accounts",
					"doctype": "Account",
					"is_query_report": True
				},
				{
					"type": "report",
					"name": "PDC-Register",
					"doctype": "Payment Entry",
					"is_query_report": True
				},
			]
		   }
		]