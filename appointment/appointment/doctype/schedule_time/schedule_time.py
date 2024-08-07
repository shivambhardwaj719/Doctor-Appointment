# Copyright (c) 2024, shivam and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ScheduleTime(Document):
    def before_save(self):
        # Set the title field to "start time and end time"
        if self.start_time:
            if self.end_time:
                    self.title = f"{self.start_time} - {self.end_time}"
            else:
                 self.title = self.start_time