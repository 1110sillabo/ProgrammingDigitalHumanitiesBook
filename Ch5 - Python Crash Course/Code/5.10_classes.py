class SocialMediaAccount():

    #initialization
    def __init__(self, name, category):
        self.name = name
        self.category = category


#initialize the Trump object
account_trump = SocialMediaAccount('Trump', 'politician')
#initialize the Imogen object
account_imogen = SocialMediaAccount('Imogen Heap', 'singer')
#test that account_imogen.name() = 'Imogen Heap'
