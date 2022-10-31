import typing
import strawberry
from config import SessionLocal
from models.models import Post as posts, Comment as comments
from sqlalchemy.orm import Session


@strawberry.type
class Post:
    id: int
    description: str
    video_url: str
    created_at: str

@strawberry.type
class Comment:
    id: int
    description: str
    created_at: str
    post_id: int

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def all_posts(db: Session):
    return db.query(posts).all()

def all_comments_filtrados(id: int, db: Session):
    return db.query(comments).filter(comments.post_id == id).all()

@strawberry.type
class Query:
    @strawberry.field
    def obtener_post_by_id(self, id: int) -> Post:
        session = next(get_db())
        result = session.query(posts).filter(posts.id == id).first()

        return Post(id = result.id, description= result.description, video_url = result.video_url, created_at = result.created_at)

    @strawberry.field
    def obtener_posts(self) -> typing.List[Post]:
        results = all_posts(next(get_db()))

        return [Post(id = result.id, description= result.description, video_url = result.video_url, created_at = result.created_at) for result in results]

    @strawberry.field
    def obtener_comment_by_id(self, id: int) -> Comment:
        session = next(get_db())
        result = session.query(comments).filter(comments.id == id).first()

        return Comment(id = result.id, description= result.description, created_at = result.created_at, post_id = result.post_id)

    @strawberry.field
    def obtener_comments_by_posts_id(self, id: int) -> typing.List[Comment]:
        results = all_comments_filtrados(id,next(get_db()))

        return [Comment(id = result.id, description= result.description, created_at = result.created_at, post_id = result.post_id) for result in results]



@strawberry.type
class Mutation:
    @strawberry.mutation
    def crear_post(self, description: str, video_url: str, created_at: str) -> int:
        post_obj = posts(
            description = description,
            video_url = video_url,
            created_at = created_at)

        session = next(get_db())
        session.add(post_obj)
        session.commit()
        session.refresh(post_obj)

        return post_obj.id

    @strawberry.mutation
    def crear_comment(self, description: str, post_id: int, created_at: str) -> int:
        comment_obj = comments(
            description = description,
            created_at = created_at,
            post_id = post_id
        )

        session = next(get_db())
        session.add(comment_obj)
        session.commit()
        session.refresh(comment_obj)

        return comment_obj.id
