# Copyright (c) 2026, kunnoh and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class AirplaneFlight(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		airplane: DF.Link
		date_of_departure: DF.Date
		destination_airport: DF.Link
		destination_airport_code: DF.ReadOnly | None
		duration: DF.Duration
		source_airport: DF.Link
		source_airport_code: DF.ReadOnly | None
		status: DF.Literal["Scheduled", "Cancelled", "Completed"]
		time_of_departure: DF.Time
	# end: auto-generated types

	pass
