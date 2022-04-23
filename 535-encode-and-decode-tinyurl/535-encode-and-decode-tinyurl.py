class Codec:
    def __init__(self):
        self.lookup = []
    
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.lookup.append(longUrl)
        N = len(self.lookup)
        return "http://tinyurl.com/" + str(N)

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        r = int(shortUrl.split("/")[-1])
        return self.lookup[r-1]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))