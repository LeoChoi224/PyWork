"""샘플 데이터 생성. 단독 실행: python samples.py"""

from databases import engine, SessionLocal
from models import Base, Member, Post, Comment

def create_sample_data():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(engine)

    with SessionLocal() as db:   
        # 1. Members 데이터 (id 자동 매칭: 1~5)
        m1 = Member(username="alice", name="엘리스")
        m2 = Member(username="bob", name="밥")
        m3 = Member(username="carol", name="캐롤")
        m4 = Member(username="dave", name="데이브")
        m5 = Member(username="eve", name="이브")
        db.add_all([m1, m2, m3, m4, m5])
        db.flush()

        # 2. Posts 데이터 (viewcnt -> view_cnt 로 필드명 수정 완료 🛠️)
        p1 = Post(title="앨리스의 첫 글", content="안녕하세요 앨리스입니다.", author=m1, view_cnt=0)
        p2 = Post(title="앨리스의 두번째 글", content="오늘 날씨가 좋네요.", author=m1, view_cnt=0)
        p3 = Post(title="밥의 글", content="밥이 작성한 게시글입니다.", author=m2, view_cnt=0)
        p4 = Post(title="캐롤의 글", content="캐롤의 게시글 내용.", author=m3, view_cnt=0)
        p5 = Post(title="데이브의 공지", content=None, author=m4, view_cnt=0) 
        db.add_all([p1, p2, p3, p4, p5])
        db.flush()

        # 3. Comments 데이터 (id 자동 매칭: 1~7)
        c1 = Comment(content="좋은 글이네요!", post=p1, author=m2)  
        c2 = Comment(content="환영합니다.", post=p1, author=m3)   
        c3 = Comment(content="동의합니다.", post=p1, author=m4)   
        c4 = Comment(content="저도 그렇게 생각해요.", post=p3, author=m1) 
        c5 = Comment(content="잘 봤습니다.", post=p3, author=m5)   
        c6 = Comment(content="캐롤 화이팅", post=p4, author=m1)    
        c7 = Comment(content="앨리스 두번째 글 댓글", post=p2, author=m5) 
        db.add_all([c1, c2, c3, c4, c5, c6, c7])
        db.flush()

        # 4. Post_Likes 데이터 매핑 (M:M 관계 추가)
        m1.liked_posts.extend([p3, p4]) 
        m2.liked_posts.append(p1)       
        m3.liked_posts.append(p1)       
        m4.liked_posts.append(p1)       
        m5.liked_posts.append(p3)       

        db.commit()

if __name__ == "__main__":
    create_sample_data()