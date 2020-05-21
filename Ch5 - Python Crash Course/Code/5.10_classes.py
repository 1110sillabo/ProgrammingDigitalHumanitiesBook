class SocialMediaAccount():

    # Initialization
    def __init__(self, name, category):
        self.name = name
        self.category = category


# Initialize the Trump object
account_trump = SocialMediaAccount('Trump', 'politician')
# Initialize the Imogen object
account_imogen = SocialMediaAccount('Imogen Heap', 'singer')
# Test that account_imogen.name() = 'Imogen Heap'
