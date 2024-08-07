import math

import frappe
from frappe import _
from frappe.query_builder import Order
from frappe.query_builder.functions import Count
from frappe.utils import pretty_date


def get_context(context):
	context.no_cache = 1
	context.parents = [{"name": _("My Account"), "route": "/"}]
	context.body_class = "clinic-page"
	page_len = 20
	# filters, txt, sort, offset = get_filters_txt_sort_offset(page_len)
	context.job_openings = get_job_openings(filters, txt, sort, page_len, offset)
	# context.no_of_pages = get_no_of_pages(filters, txt, page_len)
	# context.all_filters = get_all_filters(filters)
	# context.sort = sort


def get_job_openings(filters=None, txt=None, sort=None, limit=20, offset=0):
	clinics = frappe.qb.DocType("Clinic")
	doctors = frappe.qb.DocType("Doctor")

	query = (
		frappe.qb.from_(clinics)
		.left_join(doctors)
		.on(clinics.doctor == doctors.name)
		.select(
			clinics.name,
			clinics.contact_number,
			clinics.is_published,
			clinics.address,
			doctors.full_name,
			doctors.qualification,
			doctors.specialty,
			doctors.shifts
		)
		.where(clinics.publish == 1)
		.groupby(clinics.name)
		.limit(limit)
		.offset(offset)
	)


