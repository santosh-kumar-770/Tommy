from app.memory.conversation_memory import (
    ConversationMemory
)


memory_store = {}


def get_memory(person_name: str):

    if person_name not in memory_store:

        memory_store[person_name] = (
            ConversationMemory(
                person_name=person_name
            )
        )

    return memory_store[person_name]