# Copyright (c) 2026, kunnoh and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import random
import string

class AirplaneTicket(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from airplane_mode.airplane_mode.doctype.airplane_ticket_add_on_item.airplane_ticket_add_on_item import AirplaneTicketAddonItem
		from frappe.types import DF

		add_ons: DF.Table[AirplaneTicketAddonItem]
		amended_from: DF.Link | None
		departure_date: DF.Date
		departure_time: DF.Time
		destination_airport_code: DF.Data
		duration_of_flight: DF.Duration
		flight: DF.Link
		flight_price: DF.Currency
		passenger: DF.Link
		seat: DF.Data | None
		source_airport_code: DF.Data
		status: DF.Literal["Booked", "Checked-In", "Boarded"]
		total_amount: DF.Currency
	# end: auto-generated types

	def validate(self):
		self.remove_duplicate_addons()
		self.calc_total_amount()

	def calc_total_amount(self):
		"""Calculate total amount = flight_price + sum of all add-on amounts"""
		if not self.get("add_ons"):
			self.total_amount = self.flight_price or 0
			return

		total_addons = sum(
			getattr(addon, 'amount', 0) or 0
			for addon in self.add_ons
		)

		self.total_amount = (self.flight_price or 0) + total_addons

	def remove_duplicate_addons(self):
		"""Remove duplicate add-ons based on the 'item' field, keeping the first occurrence."""
		if not self.get("add_ons"):
			return

		seen = {}
		uniq_rows = []

		for addon in self.add_ons:
			key = getattr(addon, 'item', None)
			if key and key not in seen:
				seen[key] = True
				uniq_rows.append(addon)

		# Replace child table with uniq entries
		self.set("add_ons", uniq_rows)

	def before_submit(self):
		"""Prevent submission unless the ticket status is 'Boarded'"""
		if self.status != "Boarded":
			frappe.throw(
				msg="Cannot submit ticket unless the passenger has boarded.",
				title="Submission Not Allowed!"
			)

	def before_save(self):
		self.set_seat()

	def set_seat(self):
		# Generate a seat number in the format: <random-integer><random-letter A-E>
		number = random.randint(1, 99)
		letter = random.choice(['A', 'B', 'C', 'D', 'E'])
		self.seat = f"{number}{letter}"
