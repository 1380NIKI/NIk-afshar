class MemeRequestManager:
    def __init__(self):
        self.requests = []

    def add_request(self, meme_name):
        self.requests.append(meme_name)
        print(f'Meme {meme_name} added successfully')

    def cancel_request(self, meme_name):
        if meme_name in self.requests:
            self.requests.remove(meme_name)
            print('Meme deleted successfully')
        else:
            print('This meme is not available')

    def view_requests(self):
        for i, meme_name in enumerate(self.requests, 1):
            print(f'{i}. {meme_name}')
