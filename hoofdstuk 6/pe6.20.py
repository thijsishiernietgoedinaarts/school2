phonebook = {'Smith, Jane':'123-45-67','Doe, John':'987-65-43','Baker,David':'567-89-01'}

def reversephonebook(x):
    mbook = {v: k for k, v in x.items()}
    print( mbook)

reversephonebook(phonebook)
