class fakeDB(object):
    def __init__(self):
        self.users = []
        self.emails = []
        self.counter = 0

    def add_user(self, user):
        # user dict { name, email ...}
        pass
        # return id
    
    def del_user(self, id):
        pass
        # return error

    def get_users(self, limit=10):
        pass
    
    def get_user(self, id):
        pass