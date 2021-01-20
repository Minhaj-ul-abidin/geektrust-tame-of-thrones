from pathlib import Path
class FileProcessor:
    def __init__(self, file_path):
        self.file_path = file_path

    def parse_line(self,line):
        arr = line.split(" ")
        message = ""
        kingdom_name , message =  arr[0], message.join(arr[1:])

        return kingdom_name, message

    def process_file(self) -> tuple:
        kingdoms_and_messsages = []
        with Path(self.file_path).open('r') as f :
            line = f.readline()
            while line:
                line = line.strip()
                kingdom_name , enc_message = self.parse_line(line)
                kingdoms_and_messsages.append((kingdom_name,enc_message))
                line = f.readline()
        
        return kingdoms_and_messsages


