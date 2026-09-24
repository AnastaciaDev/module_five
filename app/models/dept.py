from dataclasses import dataclass, field, asdict
from typing import Optional
import uuid


@dataclass
class Department:
    name: str

    # deactivation 
    is_active: bool = True
    id: str = field(default_factory=lambda: str(uuid.uuid4()))

    def to_dict(self) -> dict:
        return asdict(self)
