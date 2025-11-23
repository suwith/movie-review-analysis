# CGV 리뷰 텍스트 분석 미니 프로젝트  
**Text Data Analysis Mini Project**

본 프로젝트는 CGV 영화 관람평 데이터를 기반으로 텍스트 분석 실습을 수행하기 위한 미니 프로젝트입니다.  
크롤링부터 형태소 분석, 빈도 분석, 시각화, LDA 토픽 모델링까지 전체 과정을 파이프라인 형태로 정리하였습니다.

---

# 📚 프로젝트 개요 (Project Overview)
본 레포지토리는 다음의 텍스트 분석 절차를 단계별로 수행합니다.

1. **크롤링 (Crawling)**  
   - Selenium 기반 자동 크롤러  
   - CGV 실관람평 리뷰 수집  
   - CSV 파일 저장

2. **형태소분석 (Morphological Analysis)**  
   - mecab / konlpy(Okt) / khaiii 중 선택  
   - 불용어 제거, 토큰 정제

3. **빈도분석 (Frequency Analysis)**  
   - 단어 등장 빈도  
   - 단어 상위 TOP 리스트  
   - 바 차트 / 테이블 분석

4. **워드클라우드 (Word Cloud)**  
   - 시각적으로 주요 단어 파악  
   - 한국어 폰트 적용 (NanumGothic 등)

5. **TF-IDF 분석**  
   - 문서-단어 행렬 생성  
   - TF-IDF 점수 산출  
   - 주요 키워드 및 단어 가중치 분석

6. **토픽 모델링 (Topic Modeling: LDA)**  
   - Latent Dirichlet Allocation 모델 적용  
   - 문서(리뷰)의 주제 구조 분석  
   - 주요 토픽별 핵심 단어 해석
