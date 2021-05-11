from flask.views import MethodView
from agenda.models.model import Contact
from flask import render_template, redirect, url_for, request

class ConctactListDeleteView(MethodView):

    def get(self, contact_id):
        if contact_id is None:
            contacts = Contact.query.order_by(Contact.name).all()
            return render_template('contact/contact.html', contacts=contacts)

        contact = Contact.query.get(contact_id)
        if contact:
            return render_template('contact/contact.html', contact=contact)

        return render_template('contact/contact.html')
    

class ContactCreateView(MethodView):

    def get(self):
        return render_template('contact/include.html')
    
    def post(self, *args, **kwargs):
        name = request.form.get("name")
        
        # create model and apply on database
        contact = Contact(name=name)
        contact.save()

        return redirect(url_for('contacts.list'))

contact = ConctactListDeleteView.as_view('list')
contact_create = ContactCreateView.as_view('create')
