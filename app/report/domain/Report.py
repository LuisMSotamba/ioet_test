from dataclasses import dataclass, field

import uuid


@dataclass
class Report:
    
    name: str
    version: str
    result: str = field(default='')
    id: str = field(default_factory=lambda:uuid.uuid4().hex)


