from kingdoms import Kingdom
from utils.cipher import Cipher
from collections import defaultdict
class Message:
    def __init__(self,kingdom: Kingdom , encrypted_message : str):
        self.encrypted_message = encrypted_message
        self.kingdom = kingdom
        
class MessageProcessor:
    @staticmethod
    def check_for_emblem(message:Message, emblem: str) -> bool:
        real_message = Cipher.decrypt(message.encrypted_message, len(emblem))
        emblem_char_count = defaultdict(int)
        emblem_char_count_in_real_message = defaultdict(int)
        for ch in emblem :
            emblem_char_count[ch] += 1
        for ch in real_message:
            if ch in emblem_char_count:
                if emblem_char_count[ch] > emblem_char_count_in_real_message[ch]:
                    emblem_char_count_in_real_message[ch] += 1
        return emblem_char_count == emblem_char_count_in_real_message