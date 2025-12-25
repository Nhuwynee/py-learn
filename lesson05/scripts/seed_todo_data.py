from configs.database import SessionLocal, engine, Base
from models.todo import Todo


def seed_todos():

    Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    try:
        existing_count = db.query(Todo).count()
        if existing_count > 0:
            print(f"Database already has {existing_count} todos. Skipping seed.")
            return

        sample_todos = [
            Todo(
                title="Learn Python FastAPI",
                description="Study FastAPI framework with SQLAlchemy ORM",
                priority=5,
                done=False
            ),
            Todo(
                title="Setup PostgreSQL Database",
                description="Configure PostgreSQL with Docker and create initial schema",
                priority=4,
                done=True
            ),
            Todo(
                title="Create API Endpoints",
                description="Build CRUD endpoints for Todo application",
                priority=5,
                done=False
            ),
            Todo(
                title="Write Unit Tests",
                description="Create comprehensive unit tests for all services",
                priority=3,
                done=False
            ),
            Todo(
                title="Deploy Application",
                description="Deploy application to production environment",
                priority=2,
                done=False
            ),
        ]

        db.add_all(sample_todos)
        db.commit()
        print(f"Successfully seeded {len(sample_todos)} todos into the database")

    except Exception as e:
        print(f"Error seeding data: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    seed_todos()
