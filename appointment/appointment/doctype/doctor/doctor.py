# Copyright (c) 2024, shivam and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Doctor(Document):
	def on_update(self):
		if self.first_name:
			if self.last_name:
				self.full_name = self.first_name + " " +self.last_name
			else:
				self.full_name = self.first_name