import json
from random import randrange
CONTACTS_FILE = 'contacts.json'

class Contact:
    def __init__(self,name,phon,groups,contact_id,email=None):
        self.contact_id = contact_id
        self.name = name
        self.phon = phon
        self.groups = groups
        self.email = email

    def to_dict(self):
        return {'contact id:':self.contact_id ,'name:':self.name,'phon number:':self.phon,'groups':self.groups,'email:':self.email}

class ContactsManager:
    def __init__(self):
        self.contacts = self.load_contact()

    def load_contact(self):
        try:
            with open(CONTACTS_FILE,'r') as file:
                return json.load(file)
        except (FileNotFoundError,json.JSONDecodeError):
            return {}

    def save_contacts(self):
        with open(CONTACTS_FILE,'w') as file:
            json.dump(self.contacts,file,indent=4)

    def add_contact(self,contact):
        if contact.contact_id in self.contacts:
            print('contact id already exist')
            return
        self.contacts[contact.contact_id] = contact.to_dict()
        self.save_contacts()
        print('contact added')


    def pop_contact(self,contact_id):
        for contact in self.contacts:
            if contact.ID == contact_id:
                return f'name: {contact.name} \nphon_list: {contact.phon_list} \ngroups: {contact.groups} \nemail: {contact.email}'

        return "contact ID is not found"

    def viewing_contacts(self):
        for contact in self.contacts:
            print(contact.__dict__)

    def delete_contact(self,contact_id):
        for contact in self.contacts:
            if contact.ID == contact_id:
                self.contacts.remove(contact)
                return True
        return False

