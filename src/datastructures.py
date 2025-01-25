
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = []

    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id
    
    def add_member(self, member):
        if "id" not in member:  
            member["id"] = self._generate_id() 
        self._members.append(member)

    def delete_member(self, id):
        new_members = []
        for m in self._members:
            if m["id"] != id:
                new_members.append(m)
        self._members = new_members

    def get_member(self, id):
        return next((m for m in self._members if m["id"] == id), None)

    
    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
