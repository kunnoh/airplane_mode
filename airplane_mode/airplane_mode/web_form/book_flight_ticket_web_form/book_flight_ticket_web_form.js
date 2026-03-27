frappe.ready(function() {
	// bind events here
	frappe.web_form.set_value("flight_price", 1000);
	const flight = frappe.utils.get_url_arg("flight");

	console.log(flight)
	if(flight){
		frappe.web_form.set_value("flight", flight);
		frappe.call({
			method: "frappe.client.get",
			args: {
				doctype: "Airplane Flight",
				name: flight,
			},
			callback: function (r) {
				// console.log(r)
				if (r.message) {
					console.log("💰 Price fetched:", r.message);
					// frappe.web_form.set_value("flight_price", r.message.price || 1000);
				}
			},
		});
	}
})

// frappe.web_form.after_load = () => {
// 	console.log("✅ Script loaded");


// 	if (flight) {
// 		console.log("🌐 URL param 'flight':", flight);

// 		frappe.web_form.set_value("flight", flight);

// 		frappe.call({
// 			method: "frappe.client.get",
// 			args: {
// 				doctype: "Airplane Flight", // not "Airplane Ticket" here!
// 				name: flight,
// 			},
// 			callback: function (r) {
// 				if (r.message) {
// 					console.log("💰 Price fetched:", r.message.price);
// 					frappe.web_form.set_value("flight_price", r.message.price || 1000);
// 				}
// 			},
// 		});
// 	}
// };
