from domain.entities.developer import Developer

class TalkGeneratorService:
    def generate(
            self,
            dev: Developer
    ) -> str:
        
        parts = []

        if dev.done:
            parts.append(f"Ontem eu trabalhei em: {', '.join(dev.done)}.")
        if dev.todo:
            parts.append(f"Estou com bloqueios em: {', '.join(dev.blockers)}.")

        return " ".join(parts)