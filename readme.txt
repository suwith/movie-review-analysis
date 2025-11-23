CGV 실관람평 리뷰 크롤링 자동화 코드 안내문
================================================

📌 1. 개요 (Overview)
------------------------------------------------
본 코드는 CGV 웹사이트에서 특정 영화의 "실관람평(리뷰)" 데이터를 
자동으로 수집하기 위한 Selenium 기반 크롤러입니다.

실행 시 다음 기능을 수행합니다:

- CGV 영화 상세 리뷰 페이지 접속
- 스크롤을 반복해 모든 리뷰 로딩
- 특정 UL 요소(`cnms01020_reviewList__UuNuN`) 내부에서 리뷰 텍스트 추출
- 리뷰를 CSV 파일(`movie_81774_reviews.csv`)로 저장
- 전체 리뷰 수 및 전체 실행 시간 출력

이번 실행 기준:
- 총 1005개의 리뷰 수집
- 총 소요 시간: 약 27분


📌 2. 사용된 라이브러리 (Dependencies)
------------------------------------------------
아래 Python 라이브러리 및 드라이버가 필요합니다.

### 필수 Python 패키지
- selenium  
- webdriver-manager  
- pandas  

### Python 기본 내장
- time

### 웹브라우저 드라이버
- ChromeDriver (webdriver-manager가 자동 설치)

### 지원 환경
- **로컬 PC 환경에서만 실행 가능**
  - Colab, Kaggle 등 클라우드 환경에서는 Selenium + GUI Chrome 실행이 제한됨
  - 실제 Chrome 브라우저와 ChromeDriver가 필요함


📌 3. 실행 환경 설명
------------------------------------------------

### 권장 Python 버전
- Python 3.8 ~ 3.11

### Chrome 설치 필수
- 실제 Chrome 브라우저가 PC에 설치되어 있어야 함
- webdriver-manager가 자동으로 버전 대응 ChromeDriver를 설치함

### Mac / Windows 모두 가능
- 단, Mac의 경우 시스템 보안 정책에 의해 ChromeDriver 실행 허용 필요


📌 4. 환경 세팅 방법
------------------------------------------------

1) Python 및 pip 설치 확인
   - macOS:
     ```
     python3 --version
     pip3 --version
     ```
   - Windows:
     ```
     python --version
     pip --version
     ```
   - Python 또는 pip이 없다면 python.org에서 Python 설치 필요


2) 패키지 설치  (pip 또는 pip3)
pip install selenium
pip install webdriver-manager
pip install pandas

4) 코드 파일 준비  
- Python 파일: `review_crawler.py`
- 동일 폴더에서 실행

5) Chrome 설치 확인  
- 최신 버전을 권장

6) 실행  
python3 review_crawler.py

markdown
코드 복사

실행 후 생성 파일:
- `movie_81774_reviews.csv` (크롤링된 리뷰 데이터)


📌 5. 코드 작동 흐름 설명
------------------------------------------------

1. ChromeDriver 로드 후 CGV 페이지 접속  
2. 초기 로딩 대기 (10~15초)  
3. 스크롤 100회 반복하여 리뷰 로딩  
4. 리뷰 리스트 ul(`ul.cnms01020_reviewList__UuNuN`) 탐색  
5. li > p 요소 중 리뷰 텍스트 추출  
6. CSV 파일로 저장  
7. 전체 리뷰 개수 및 실행 시간 출력  

해당 구조는 CGV 사이트의 HTML DOM에 의존하므로  
DOM 변경 시 셀렉터 수정이 필요할 수 있습니다.


📌 6. 주의사항
------------------------------------------------

- CGV 페이지 구조 변경 시 코드 수정 필요  
- 스크롤 속도가 너무 빠르면 리뷰 누락 가능  
- PC 성능 및 인터넷 속도에 따라 실행 시간 달라질 수 있음  
- Colab/서버 환경에서는 Selenium GUI 실행이 불가능하여 작동 안 됨  

권장 PC 환경:
- RAM 8GB 이상
- Chrome 최신 버전
- 안정적인 인터넷 환경


📌 작성자: 박수연