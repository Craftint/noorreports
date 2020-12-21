from __future__ import unicode_literals
from frappe import _


def get_data():
    return [{
        "label":
        _("Accounts Receivable"),
        "items": [
            {
                "type": "report",
                "name": "Statement Of Accounts",
                "is_query_report": True,
                "onboard": 1,
                "doctype": "Account"
            }

        ]
    }]
