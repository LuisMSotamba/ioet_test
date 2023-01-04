from dataclasses import dataclass, field

import uuid

@dataclass
class Employee:

    name: str
    id: str = field(default_factory=lambda:uuid.uuid4().hex)
