# Copyright (c) 2026, kunnoh and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class FlightPassenger(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		date_of_birth: DF.Date
		first_name: DF.Data
		full_name: DF.ReadOnly | None
		last_name: DF.Data | None
		name: DF.Int | None
	# end: auto-generated types

	def before_save(self):
		self.set_full_name()

	def set_full_name(self):
		if self.first_name or self.last_name:
			self.full_name = f"{self.first_name or ''} {self.last_name or ''}".strip()
