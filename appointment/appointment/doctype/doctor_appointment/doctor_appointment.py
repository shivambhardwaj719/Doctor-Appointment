# Copyright (c) 2024, shivam and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class DoctorAppointment(Document):
	def after_insert(self):
		print("Your queue number")
	
	def add_to_appointment_queue(self):
		q = frappe.new_doc("Doctor Appointment")
		q.update({
				"patient_name": self.patient_name,
				"date" : self.date,
				"shift" : self.shift,
				"clinic" : self.clinic,
			}),
		
		q.insert(ignore_permissions= True)
		q.save()
		return q.name
