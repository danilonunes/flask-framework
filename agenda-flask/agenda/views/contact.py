from flask.views import MethodView
from agenda.models.model import Contact
from flask import render_template, redirect, url_for

class ContactView(MethodView):
    def get(self, contact_id):
        if contact_id is None:
            contacts = Contact.query.order_by(Contact.name).all()
            return render_template('contact/contact.html', contacts=contacts)
        else:
            contact = Contact.query.get(contact_id)
            print(contact)
            if contact:
                return render_template('contact/contact.html', contact=contact)
            else:
                return render_template('contact/contact.html')
    
    def post(self):
        contact = Contact.from_form_data(request.form)
        print(contact)
        contact.save()
        return redirect(url_for('contacts'))

contact = ContactView.as_view('contact')