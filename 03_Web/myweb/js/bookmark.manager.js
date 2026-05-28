/**
 * 북마크 데이터 관리 및 정렬 로직
 */
const BOOKMARK_KEY = "cinemook_bookmarks";

const BookmarkManager = {
    // 1. 전체 북마크 가져오기 (최신순)
    getAll() {
        const data = localStorage.getItem(BOOKMARK_KEY);
        try {
            return data ? JSON.parse(data) : [];
        } catch {
            return [];
        }
    },

    // 2. 북마크 여부 확인
    isBookmarked(movieId) {
        const bookmarks = this.getAll();
        return bookmarks.some(m => String(m.id) === String(movieId));
    },

    // 3. 북마크 토글 (있으면 삭제, 없으면 최신순으로 맨 앞에 추가)
    toggle(movieData) {
        if (!movieData || !movieData.id) return false;

        let bookmarks = this.getAll();
        const isExist = bookmarks.some(m => String(m.id) === String(movieData.id));

        if (isExist) {
            bookmarks = bookmarks.filter(m => String(m.id) !== String(movieData.id));
            localStorage.setItem(BOOKMARK_KEY, JSON.stringify(bookmarks));
            return false; // 북마크 해제됨
        } else {
            const newBookmark = {
                id: movieData.id,
                title: movieData.title,
                poster_path: movieData.poster_path,
                timestamp: Date.now()
            };
            bookmarks.unshift(newBookmark); // 최신 북마크를 맨 앞으로
            localStorage.setItem(BOOKMARK_KEY, JSON.stringify(bookmarks));
            return true; // 북마크 등록됨
        }
    },

    // 4. 메인 화면용 무한 확장 기반 데이터 결합 (기본 17개 + 알파)
    getMainGridMovies() {
        const bookmarks = this.getAll();

        // 북마크가 없으면 초기 기본값 17개 그대로 반환
        if (bookmarks.length === 0) {
            return [...defaultMovies];
        }

        // 중복 제거를 위해 북마크된 ID 세트 생성
        const bookmarkedIds = new Set(bookmarks.map(m => String(m.id)));

        // 기본 17개 영화 중 북마크와 겹치지 않는 것만 필터링
        const filteredDefaults = defaultMovies.filter(m => !bookmarkedIds.has(String(m.id)));

        // [최신 북마크 목록] 뒤에 [중복 제거된 기본 영화]를 이어 붙여 무한 확장용 배열 리턴
        // 북마크 개수만큼 기본 포스터 제거
        const remainDefaultCount = Math.max(17 - bookmarks.length, 0);
        // 남길 기본 포스터만 잘라냄
        const slicedDefaults = filteredDefaults.slice(0, remainDefaultCount);
        // 최종 조합
        return [...bookmarks, ...slicedDefaults];
    },
    // 전체 삭제
    clearAll() {
        localStorage.removeItem(BOOKMARK_KEY);
    },
};