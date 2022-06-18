def generate_hashtag(s):
    if len(s) == 0 or len(s.strip()) > 139:
        return False
    else:
        s = '#'+s.title()
        s = ''.join(s.split())
        return s
