"""필요한 동작 정의및 실행: python main.py"""
from sqlalchemy import select, func, desc
from databases import SessionLocal
from models import Member, Post, Comment, post_likes


def posts_by_member(db, member_id: int):
    """특정 회원이 작성한 게시글 목록"""
    member = db.get(Member, member_id)
    return member.posts if member else []


def author_of_post(db, post_id: int):
    """특정 게시글을 작성한 회원"""
    post = db.get(Post, post_id)
    return post.author if post else None


def increase_viewcnt(db, post_id: int):
    """게시글 조회수 +1"""
    post = db.get(Post, post_id)
    if post:
        post.view_cnt += 1
        db.commit()
    return post


def comments_of_post(db, post_id: int):
    """특정 게시글의 댓글 목록"""
    post = db.get(Post, post_id)
    return post.comments if post else []


def commenters_of_post(db, post_id: int):
    """특정 게시글에 댓글 작성한 회원 목록 (중복 제거)"""
    stmt = (
        select(Member)
        .join(Comment, Member.id == Comment.author_id)
        .where(Comment.post_id == post_id)
        .distinct()
    )
    return db.scalars(stmt).all()


def comments_by_member(db, member_id: int):
    """특정 회원이 작성한 모든 댓글"""
    member = db.get(Member, member_id)
    return member.comments if member else []


def like_count(db, post_id: int):
    """게시글 좋아요 개수"""
    stmt = select(func.count()).where(post_likes.c.post_id == post_id)
    return db.scalar(stmt)


def liked_members(db, post_id: int):
    """게시글에 좋아요 남긴 회원 목록"""
    post = db.get(Post, post_id)
    return post.liked_by_members if post else []


def toggle_like(db, member_id: int, post_id: int):
    """좋아요 토글. 추가되면 True, 제거되면 False 반환"""
    member = db.get(Member, member_id)
    post = db.get(Post, post_id)
    
    if not member or not post:
        return False
    
    # 회원의 좋아요 목록에 이 게시글이 이미 있다면?
    if post in member.liked_posts:
        member.liked_posts.remove(post)  # 좋아요 취소
        db.commit()
        return False
    else:                           # 없다면?
        member.liked_posts.append(post)  # 좋아요 추가
        db.commit()
        return True

def posts_with_like_counts(db):
    """게시글별 좋아요 개수 조회.
    출력: 게시글id | 제목 | 작성자 이름 | 좋아요 개수 (좋아요 개수 내림차순)
    """
    stmt = (
        select(
            Post.id,
            Post.title,
            Member.name,
            func.count(post_likes.c.member_id).label("like_cnt")
        )
        .join(Member, Post.author_id == Member.id)
        .outerjoin(post_likes, Post.id == post_likes.c.post_id)
        .group_by(Post.id, Member.name)
        .order_by(desc("like_cnt"), Post.id.asc())
    )
    return db.execute(stmt).all()


if __name__ == "__main__":
    """위 동작들을 실행하는 코드들을 작성해보세요"""
    with SessionLocal() as db:

        # print("== 🟡1. 회원 1번이 작성한 게시글 ==")
        # for p in posts_by_member(db, 1):
        #     print(f"  제목: {p.title} 내용: {p.content} (조회수: {p.view_cnt})")

        # print("\n== 🟡2. 게시글 1번 작성자 ==")
        # author = author_of_post(db, 1)
        # print(f"  작성자 이름: {author.name}")

        # print("\n== 🟡3. 게시글 1번 조회수 +1 ==")
        # updated_post = increase_viewcnt(db, 1)
        # if updated_post:
        #     print(f"  게시글 1번 조회수: {updated_post.view_cnt}회")

        # print("\n== 🟡4. 게시글 1번 댓글 목록 ==")
        # for c in comments_of_post(db, 1):
        #     print(f"  작성자: {c.author.name} - 내용: {c.content}")

        # print("\n== 🟡5. 게시글 1번에 댓글 단 회원 목록 ==")
        # for m in commenters_of_post(db, 1):
        #     print(f"  회원명: {m.name}")

        # print("\n== 🟡6. 회원 1번이 작성한 모든 댓글 ==")
        # for c in comments_by_member(db, 1):
        #     print(f"  [원문 ID: {c.post_id}] 댓글 내용: {c.content}")

        # print("\n== 🟡7. 게시글 1번 좋아요 개수 ==")
        # print(f"  좋아요 수: {like_count(db, 1)}개")

        # print("\n== 🟡8. 게시글 1번에 좋아요한 회원 목록 ==")
        # for m in liked_members(db, 1):
        #     print(f"  {m.name}")

        print("\n== 🟡9. 회원 5번이 게시글 1번 좋아요 토글 ==")
        result = toggle_like(db, 5, 1)
        print(f"  결과: {'좋아요 추가 완료' if result else '좋아요 취소 완료'}")

        # print("\n== 🟡10. 게시글별 좋아요 개수 (내림차순) ==")
        # print("게시글id | 제목 | 작성자 이름 | 좋아요 개수")
        # print("-" * 52)
        # for p_id, title, author_name, l_cnt in posts_with_like_counts(db):
        #     print(f" {p_id:^7} | {title:<13} | {author_name:^6} | {l_cnt}개")