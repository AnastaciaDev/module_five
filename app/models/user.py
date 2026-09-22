
from dataclasses import dataclass, field, asdict
from typing import Optional
import uuid


@dataclass
class User:
    username: str
    email: str
    employee_id: Optional[str] = None
    role: str = "employee"
    is_active: bool = True
    id: str = field(default_factory=lambda: str(uuid.uuid4()))

    def __post_init__(self):
        if self.role not in ("admin", "manager", "employee"):
            raise ValueError("role must be admin, manager, or employee")

    def to_dict(self) -> dict:
        # Never expose password_hash in serialization
        d = asdict(self)
        return d
