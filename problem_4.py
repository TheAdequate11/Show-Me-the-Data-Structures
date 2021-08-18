"""
-------------------------------------------------------------------------------
                            Defining Classes
-------------------------------------------------------------------------------
"""
class Group(object):

    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        #Appends 'group' to 'groups' array
        self.groups.append(group)
    def add_user(self, user):
        #Appends 'user' to 'users' array
        self.users.append(user)

    #Getters, setters, and condition checkers
    def get_groups(self):
        return self.groups
    def get_users(self):
        return self.users
    def get_name(self):
        return self.name

"""
-------------------------------------------------------------------------------
                            Defining Functions
-------------------------------------------------------------------------------
"""
def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    in_group = False
    if user in group.get_users():
        return True
    for item in group.get_groups():
        in_group = is_user_in_group(user,item)
        if in_group:
            break
    return in_group


"""
-------------------------------------------------------------------------------
                            Running Test Case #1
-------------------------------------------------------------------------------
"""
print("Test Run #1:")
print()

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

print(is_user_in_group(sub_child_user,parent))
#Expected: True

print('_______________________________________________________________________')

"""
-------------------------------------------------------------------------------
                            Running Test Case #2
-------------------------------------------------------------------------------
"""
print("Test Run #2:")
print()

parent = Group("parent")
child1 = Group("child1")
child2 = Group("child2")
child3 = Group("child3")
child4 = Group("child4")
child5 = Group("child5")
child6 = Group("child6")
subchild1 = Group("subchild1")
subchild2 = Group("subchild2")
subchild3 = Group("subchild3")
subchild4 = Group("subchild4")
subchild5 = Group("subchild5")
subchild6 = Group("subchild6")
subchild7 = Group("subchild7")
subchild8 = Group("subchild8")


sub_child_user = "sub_child_user"
subchild5.add_user(sub_child_user)

parent.add_group(child1)
parent.add_group(child2)
parent.add_group(child3)
parent.add_group(child4)
parent.add_group(child5)
parent.add_group(child6)

child1.add_group(subchild1)
child1.add_group(subchild2)
child1.add_group(subchild3)
child3.add_group(subchild4)
child4.add_group(subchild5)
child6.add_group(subchild6)
child6.add_group(subchild7)
child2.add_group(subchild8)

print(is_user_in_group(sub_child_user,parent))
#Expected: True

print('_______________________________________________________________________')


"""
-------------------------------------------------------------------------------
                            Running Test Case #3
-------------------------------------------------------------------------------
"""
print("Test Run #3:")
print()
parent = Group("parent")
file = 'user'
print(is_user_in_group(file,parent))
#Expected: False

print('_______________________________________________________________________')

"""
-------------------------------------------------------------------------------
                            Running Test Case #4
-------------------------------------------------------------------------------
"""
print("Test Run #4:")
print()
parent = Group("")
file = ''
print(is_user_in_group(file,parent))
#Expected: False

print('_______________________________________________________________________')
"""
-------------------------------------------------------------------------------
                            Running Test Case #5
-------------------------------------------------------------------------------
"""
print("Test Run #5:")
print()
parent = Group(None)
file = None
print(is_user_in_group(file,parent))
#Expected: False

print('_______________________________________________________________________')
