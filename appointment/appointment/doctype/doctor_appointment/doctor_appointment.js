// Copyright (c) 2024, shivam and contributors
// For license information, please see license.txt

frappe.ui.form.on("Doctor Appointment", {
	refresh(frm) {
        frm.set_query("shift", (doc)=>{
            return{
                filters:{
                    "clinic" : doc.clinic
                }
            }            
        })
	},
});
