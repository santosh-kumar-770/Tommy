from dataclasses import dataclass, field


@dataclass
class ConversationMemory:

    person_name: str

    company: str = ""

    relationship_score: int = 50

    last_topic: str = ""

    previous_messages: list = field(
        default_factory=list
    )

    notes: list = field(
        default_factory=list
    )