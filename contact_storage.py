#-*- coding: utf-8 -*-
import copy
import cPickle

class ContactNotInStorage(Exception):
    def __init__(contact):
        self.contact = contact
        Exception.__init__(self, "Contact {0} not in storage. Please insert first".format(contact))

class ContactsIntegrityError(Exception):
    pass

class ContactNotFound(Exception):
    pass

class ContactAlredyInStorage(Exception):
    def __init__(self, contact):
        self.contact = contact
        Exception.__init__(self, "Contact {0} already in storage".format(contact))

class ContactStorage(object):
    def __init__(self):
        self._contacts = []
        self._merges = {}

    def _check_contact(self, contact):
        if contact._id is None:
            raise ContactNotInStorage(contact)
        if contact._id + 1 > len(self._contacts):
            raise ContactsIntegrityError("Contacts shoud be already in storage, but not in it. Bad _id ?")

    def insert(self, contact):
        "Inserts new contact to storage. If contact already exists in storage, it will be dublicated"
        "If you want to update account which already exists and insert it if not, use update with upsert = True"
        "Returns contact id"

        if contact._id:
           raise ContactAlredyInStorage
        self._contacts.append(contact)
        contact._id = len(self._contacts)-1
        return contact._id
            
    def update(self, contact, upsert = False):
        "upsert = True means update contact if exists and insert if not"
        "Returns contact id"
        if contact._id is None:
            if upsert == False:
                raise ContactNotInStorage(contact)
            
            return self.insert(contact)

        if contact._id +1 > len(self._contacts):
            raise ContactsIntegrityError("Contacts shoud be already in storage, but not in it. Bad _id ?")
        self._contacts[contact._id] = contact
        return contact._id

    def drop_contact_by_id(self, contact):
	raise NotImplementedError

    def drop(self, contact):
        if contact._id is None:
            raise ContactNotInStorage(contact)
        self.drop_contact_by_id(contact._id)
    
    def get_contact(self, i):
        try:
            contact = copy.deepcopy(self._contacts[i])
        except IndexError:
            raise ContactNotFound("No contact with such id")
        
        return contact
    
    def count(self):
        return len(self._contacts)
    
    def get_contacts(self):
        return copy.deepcopy(self._contacts)
        
    def xget_contacts(self):
        for contact in self._contacts:
            yield copy.deepcopy(contact)

    def drop_all_contacts(self):
        self._contacts = []
        
    def drop_all_merges(self):
        self._merges = {}
        
    def save(self, filename):
        with open(filename, 'w') as fn:
            cPickle.dump(self.__dict__, fn)
    
    def load(self, filename):
        with open(filename) as fn:
            self.__dict__ = cPickle.load(fn)
    
    def _merge_one_way(self, contact_1_id, contact_2_id):
	if contact_1_id == contact_2_id:
	    return
        self._merges.setdefault(contact_1_id, [])
        if contact_2_id not in self._merges[contact_1_id]:
            self._merges[contact_1_id].append(contact_2_id)

    def merge_by_id(self, contact_id_1, contact_id_2):
        if (contact_id_1 + 1 > len(self._contacts)) or (contact_id_2 + 1 > len(self._contacts)):
             raise ContactsIntegrityError("Contacts shoud be already in storage, but not in it. Bad _id ?")
                
        self._merge_one_way(contact_id_1, contact_id_2)
        self._merge_one_way(contact_id_2, contact_id_1)
        
    def merge(self, contact_1, contact_2):
        self._check_contact(contact_1)
        self._check_contact(contact_2)

        self.merge_by_id(contact_1._id, contact_2._id)
    
    def _unmerge_one_way(self, contact_id_1, contact_id_2):
        if contact_id_1 not in self._merges:
            return
        try:
            self._merges[contact_id_1].remove(contact_id_2)
        except ValueError:
            pass
    
    def unmerge_by_id(self, contact_id_1, contact_id_2):
        if (contact_id_1 + 1 > len(self._contacts)) or (contact_id_2 + 1 > len(self._contacts)):
             raise ContactsIntegrityError("Contacts shoud be already in storage, but not in it. Bad _id ?")
             
        self._unmerge_one_way(contact_id_1, contact_id_2)
        self._unmerge_one_way(contact_id_2, contact_id_1)
    
    def unmerge(self, contact_1, contact_2):
        self._check_contact(contact_1)
        self._check_contact(contact_2)
        
        self.unmerge_by_id(contact_1._id, contact_2._id)
    
    def get_merged_with_ids(self, contact):
        self._check_contact(contact)
        if contact._id not in self._merges:
            return []
        
        return self._merges[contact._id][:]

    def get_merged_with(self, contact):
        merged_with = []
        for contact_id in self.get_merged_with_ids(contact):
            merged_with.append(self.get_contact(contact_id))
        return merged_with
    
    def xget_merged_with(self, contact):
        for contact_id in self.get_merged_with_ids(contact):
            yield self.get_contact(contact_id)
