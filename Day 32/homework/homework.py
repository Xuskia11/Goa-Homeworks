# code ewars
def generate_hashtag(s):
    
    s = '#'+s.title()
    s = ''.join(s.split())
    if len(s) in range(2,141):
        return s
    else:    
        return False