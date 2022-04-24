# No encoding
class Codec:

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        return longUrl
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return shortUrl
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))



# Some encoding
import random
class Codec:
    
    shortlong = {}
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        # we need a list of all characters in 0-9A-Za-z
        chars = [chr(d) for d in range(ord('0'), ord('9')+1)]
        chars.extend([chr(d) for d in range(ord('A'), ord('Z')+1)])
        chars.extend([chr(d) for d in range(ord('a'), ord('z')+1)])

        # ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
        # 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
        # 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 
        # 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 
        # 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
        # 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 
        # 'y', 'z']

        
        length = 6          # a length of tinyurl you would like, can be determined
        ans = ""            # this is what we will reply
        	     
        for i in range(length):
            ans += chars[random.randint(0,61)]
        self.shortlong[ans]=longUrl

        return "https://tinyurl/"+ans        

    def decode(self, shortUrl):
        last = shortUrl.split("/")[-1]
        return self.shortlong[last]