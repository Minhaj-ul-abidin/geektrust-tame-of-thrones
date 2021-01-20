from utils.cipher import Cipher
from utils.process_file import FileProcessor

from kingdoms import ALL_KINGDOMS
from messages import Message , MessageProcessor

class Runner:
    def __init__(self,file_path,candidate_ruler = "SPACE"):
        self.candidate_ruler = candidate_ruler
        self.file_path = file_path
        self.run()
        
    

    def run(self):
        kingdoms_and_encMessages = FileProcessor(self.file_path).process_file()
        kingdoms_in_support = []
        for k , encM in kingdoms_and_encMessages:
            kingdom = ALL_KINGDOMS[k]
            will_support = MessageProcessor.check_for_emblem(Message(kingdom,encM),kingdom.emblem)
            if will_support:
                kingdoms_in_support.append(kingdom)

        if len(kingdoms_in_support) >= 3 :
            print(self.candidate_ruler , *kingdoms_in_support)
        else :
            print("NONE")