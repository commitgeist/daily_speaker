from domain.entities.developer import Developer
from domain.services.talk_generator import TalkGeneratorService

class GenerateDailyTalkUseCase:
    def __init__(self):
        self.generator = TalkGeneratorService()
    
    def execute(self, name: str, done: list, todo: list, blockers: list) -> str:
        dev = Developer(name, done, todo, blockers)
        return self.generator.generate(dev)