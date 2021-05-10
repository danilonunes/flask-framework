from flask import Blueprint
from .views.teste import home
from .views.contact import contact

bp_home = Blueprint('teste', __name__)
bp_home.add_url_rule('/', view_func=home, methods=['GET']) 

bp_contact = Blueprint('contacts', __name__)
bp_contact.add_url_rule('/contacts/', view_func=contact, defaults={'contact_id': None}, methods=['GET'])
bp_contact.add_url_rule('/contacts/<int:contact_id>', view_func=contact, methods=['GET'])
bp_contact.add_url_rule('/contacts/incluir/', view_func=contact, defaults={'contact_id': None}, 
                        methods=['GET','POST'])