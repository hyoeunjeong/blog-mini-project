

**🌕UNI.verse🌟** AI 기반 공부 블로그 입니다.

---


## 📖 프로젝트 소개
UNI.verse는 사용자가 입력한 공부 주제를 기반으로 AI가 개념 정리, 학습법, 예시, 연습문제, 복습 팁 등을 자동으로 생성하여, 요일별로 계획화하고 이를 블로그 형태로 저장·공유할 수 있는 통합형 학습 지원 플랫폼입니다. 사용자는 AI의 도움을 받아 체계적으로 공부하며 자신의 기록을 블로그에 일지 형태로 남길 수 있습니다. 또한 다양한 사용자와 상호소통하여 공부의 동기 부여를 얻을 수있습니다.


### 🎯 목적

* 대학생 및 전공 학습자에게 체계적인 학습 루틴 제공
* AI를 활용한 맞춤형 Day별 학습 계획 생성
* 커뮤니티 기능을 통한 학습 동기 부여

---

## ✨ 특징

* 🤖 **AI 학습 플래너**: 주제만 입력하면 요일별 공부 계획 자동 생성
* 💬 **블로그 기능**: 공부 일지 저장, 댓글, 좋아요, 해시태그 기능
* 👥 **소셜 기능**: 프로필 보기 및 수정
* 🔒 **보안 강화**: 권한 기반 접근 제어, CSRF 보호
* 🎨 **반응형 디자인**

---

## 🛠️ 기술 스택

| 구분       | 기술                               |
| -------- | -------------------------------- |
| Backend  | Django, Python, SQLite3          |
| Frontend | HTML, CSS, Bootstrap, JavaScript |
| AI API   | OpenAI GPT-3.5 / GPT-4 API       |
| 인증       | Django Auth, Custom User Model   |
| 저장소      | Django Media / Static Files      |

---

## 📁 프로젝트 구조

```
study-blog/
├── universe/        # 프로젝트 설정
├── account/         # 사용자 인증 및 소셜
├── blog/            # 게시글, 댓글, 좋아요
├── study/           # AI 학습 플래너
├── templates/       # HTML 템플릿
├── static/          # 정적 파일 (CSS, JS, 이미지 등)
└── manage.py
```

---

##  Study 앱 - AI 학습 플래너

AI가 생성한 학습 계획을 주제별, 요일별로 정리해 저장하고 조회하는 기능을 제공합니다.

### 기능

* `StudyAIView`: 사용자의 주제를 GPT에 전송해 계획 생성
* `parse_and_save_days()`: 응답을 Day별로 분리하여 저장
* `StudyPlanListView`: 사용자의 모든 학습 계획 목록 조회
* `StudyPlanDetailView`: 계획의 요일별 세부 내용 확인

### 프롬프트 예시

```
나는 대학교 공대생이고 전공은 반도체와 회로야.
'디지털 논리회로'라는 주제에 대해 공부할 계획이야.
1. 이 주제를 이해하기 위해 필요한 개념들을 기초부터 심화 순서로 정리해줘.
2. 각 개념마다 쉬운 설명, 학습법, 예시 제시
3. 연습문제 2개 이상과 풀이 팁
4. 복습 팁 제공
5. 마크다운이나 특수 기호 없이 순수 텍스트로 출력
```

### 관련 모델

```python
# StudyPlan
- user
- subject
- goal
- duration
- plan_type
- result_text
- created_at

# StudyDayPlan
- study_plan
- day
- content
- prompt_example
- concept_summary
```

---

## Blog 앱 - 게시글, 댓글, 좋아요 시스템

* 게시글 CRUD, 댓글/대댓글, 좋아요, 해시태그 기능 지원
* AJAX를 통한 실시간 상호작용 구현
* 사용자 권한 제어: 작성자만 수정/삭제 가능

### 관련 모델

```python
# Post
- title, content, image, views
- author, category, tags, likes

# Comment
- post, writer, content


# Like
- user, post

# Category / Tag
- name, slug
```

---

## 📊 데이터베이스 통합 구조

### CustomUser

```python
- username, email, bio, profile_image
- ai_usage_count
```


### AIUsageLog

```python
- user, feature_type, tokens_used, created_at
```

---

## 🔗 URL 구조 정리

### 루트 URL (universe/urls.py)

```python
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", main_view, name="main"),
    path("blog/", include("blog.urls")),
    path("accounts/", include("accounts.urls")),
    path("study/", include("study.urls")),
]
```

### 📝 Blog

| URL                              | View          | 설명     | 권한             |
| -------------------------------- | ------------- | ------ | -------------- |
| `/blog/`                         | Index         | 게시글 목록 | 공개             |
| `/blog/write/`                   | Write         | 새 글 작성 | 로그인            |
| `/blog/post/<pk>/`               | Detail        | 상세 보기  | 공개             |
| `/blog/post/<pk>/edit/`          | Update        | 글 수정   | 작성자            |
| `/blog/post/<pk>/delete/`        | Delete        | 글 삭제   | 작성자            |
| `/blog/post/<pk>/like/`          | ToggleLike    | 좋아요 토글 | 로그인            |
| `/blog/post/<pk>/comment/write/` | CommentWrite  | 댓글 작성  | 로그인            |
| `/blog/comment/<pk>/edit/`       | CommentEdit   | 댓글 수정  | 작성자            |
| `/blog/comment/<pk>/delete/`     | CommentDelete | 댓글 삭제  | 작성자 or 게시글 작성자 |

### Study

| URL              | View                | 설명       | 권한  |
| ---------------- | ------------------- | -------- | --- |
| `/study/`        | StudyPlanListView   | 학습 계획 목록 | 로그인 |
| `/study/create/` | StudyAIView         | AI 학습 생성 | 로그인 |
| `/study/<pk>/`   | StudyPlanDetailView | 계획 상세 보기 | 로그인 |

### 계정/소셜

| URL                            | View              | 설명     | 권한  |
| ------------------------------ | ----------------- | ------ | --- |
| `/accounts/login/`             | LoginView         | 로그인    | 공개  |
| `/accounts/signup/`            | SignupView        | 회원가입   | 공개  |
| `/accounts/profile/<user_id>/` | ProfileView       | 프로필 보기 | 공개  |
| `/accounts/profile/update/`    | ProfileUpdateView | 프로필 수정 | 본인만 |


---

## 권한 요약
* 🔐 로그인 필요: 글 작성, 댓글, 좋아요, 학습 계획
* 👤 작성자만: 글 및 댓글 수정/삭제
* 🛡️ 작성자 또는 글 소유자: 댓글 삭제

---


