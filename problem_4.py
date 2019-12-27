'''
Show me the data structures
Problem 3: Active Directory
'''


class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    # Check if user in group
    if user in group.users:
        return True

    # If not recursively check child groups
    for child_group in group.groups:
        if is_user_in_group(user, child_group):
            return True

    return False


if __name__ == '__main__':
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    assert is_user_in_group(sub_child_user, parent), 'Failing to detect user in child group'
    assert not is_user_in_group('non-user', parent), 'Passing non-existent user'
    print('All tests passed!')