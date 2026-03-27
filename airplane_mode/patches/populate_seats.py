import frappe
import random

def execute():
	"""
    One-time script to assign random seat numbers to existing Airplane Tickets.
    Seat format: 1A to 99E (e.g., 42C, 7A, 15D)
    """
    tickets = frappe.get_all("Airplane Ticket", fields=["name", "passenger"])
    for ticket in tickets:
        # Generate a seat number in the format: <random-integer><random-letter A-E>
        number = random.randint(1, 99)
        letter = random.choice(['A', 'B', 'C', 'D', 'E'])
        seat = f"{number}{letter}"

        frappe.db.set_value("Airplane Ticket", ticket.name, "seat", seat)




	# # Fetch only necessary fields. Skip already assigned seats (idempotent)
	# tickets = frappe.get_all(
	# 	"Airplane Ticket",
	# 	fields=["name"],
	# 	filters={"seat": ["is", "not set"]}
	# )

	# updated_count = 0
	# for ticket in tickets:
	# 	# Generate seat: number 1-99 + letter A-E
	# 	number = random.randint(1, 99)
	# 	letter = random.choice(['A', 'B', 'C', 'D', 'E'])
	# 	seat = f"{number}{letter}"

	# 	frappe.db.set_value(
	# 		"Airplane Ticket",
	# 		ticket.name,
	# 		"seat",
	# 		seat
	# 	)
	# 	updated_count += 1

	frappe.db.commit()
	frappe.log(f"Successfully assigned seat numbers to {updated_count} Airplane Tickets.")
	frappe.log("=== populate_seats patch completed ===")
