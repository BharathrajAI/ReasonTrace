import sqlite3
import os


DB_PATH = "data/memories.db"


def get_connection():
    os.makedirs("data", exist_ok=True)
    return sqlite3.connect(DB_PATH)


def create_database():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS memories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()
    connection.close()


def add_memory(content: str):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO memories (content) VALUES (?)",
        (content,)
    )

    connection.commit()
    connection.close()


def get_all_memories():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT id, content, created_at FROM memories"
    )

    memories = cursor.fetchall()

    connection.close()

    return memories

def get_memory_texts():
    memories = get_all_memories()

    return [memory[1] for memory in memories]

if __name__ == "__main__":
    create_database()

    add_memory("Bharath lives in Chennai")
    add_memory("Bharath moved to Bangalore")
    add_memory("Bharath likes Python")

    memories = get_all_memories()

    print("\nStored memories:")

    for memory in memories:
        print(memory)