// Copyright (c) 2016, craft and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["PDC-Register"] = {

        "filters": [
		{
			"fieldname":"payment_type",
			"label": __("Payment Type"),

			"fieldtype": "Select",
			"options": [
			     " ","Pay", "Receive"
				//{ "value": "Pay", "label": __("Pay") },
				//{ "value": "Receive", "label": __("Receive") }

			],
		},
		{
                        "fieldname":"company",
                        "label": __("Company"),
                        "fieldtype": "Link",
                        "options": "Company",

                },




	]
};