from dataclasses import dataclass, asdict

@dataclass
class Task:
    id: int
    description: str
    status: str
    createdAt: str
    updatedAt: str

    def to_dict(self):
        return asdict(self)
    
    @staticmethod
    def from_dict(data):
        return Task(
            id = data["id"],
            description=data["description"],
            status=data["status"],
            createdAt=data["createdAt"],
            updatedAt=data["updatedAt"]
        )
