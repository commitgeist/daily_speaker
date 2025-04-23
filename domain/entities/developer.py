from typing import List

class Developer:
    def __init__(self, 
                 name: str, 
                 done: List[str], 
                 todo: List[str], 
                 blockers: List[str]):
        
        self.name = name
        self.done = done
        self.todo = todo
        self.blockers = blockers