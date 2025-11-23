import time
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


MOVIE_URL = "https://cgv.co.kr/cnm/cgvChart/movieChart/81774"


def create_driver(headless: bool = False) -> webdriver.Chrome:
    options = Options()
    if headless:
        options.add_argument("--headless=new")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options,
    )
    return driver


def scroll_to_load_all_reviews(
    driver: webdriver.Chrome,
    max_scroll: int = 1000,
    wait_per_scroll: float = 5.0,
) -> None:
    last_height = driver.execute_script("return document.body.scrollHeight")
    same_height_count = 0

    for i in range(max_scroll):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(wait_per_scroll)

        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            same_height_count += 1
            wait_per_scroll +=2
            if same_height_count >= 20:
                print("더 이상 스크롤로 늘어나는 컨텐츠가 없어 보입니다. 스크롤 종료.")
                break
        else:
            wait_per_scroll -=2
            same_height_count = 0

        last_height = new_height
        print(f"{i + 1}회 스크롤 완료, 현재 높이: {new_height}")


def main():
    start_time = time.time()

    driver = create_driver(headless=False)

    try:
        print("페이지 접속 중...")
        driver.get(MOVIE_URL)

        #관람평 조회 API 로딩 시간이 있어서 아래 코드 추가함
        print("실관람평 로딩 대기 중 (10초)...")
        time.sleep(10)

        print("스크롤을 시작합니다. (400회)")
        scroll_to_load_all_reviews(driver, max_scroll=400, wait_per_scroll=5.0)

        # 리뷰 리스트 ul 찾기
        review_list_selector_candidates = [
            "ul.cnms01020_reviewList__UuNuN",
            'ul[class*="cnms01020_reviewList"]',
        ]

        review_list = None
        for selector in review_list_selector_candidates:
            elems = driver.find_elements(By.CSS_SELECTOR, selector)
            if elems:
                review_list = elems[0]
                print(f"리뷰 리스트 ul을 {selector} 셀렉터로 찾았습니다.")
                break

        if review_list is None:
            print("리뷰 리스트 ul 요소를 찾지 못했습니다.")
            return

        # p 태그 탐색
        inner_selector_candidates = [
            "li p.reveiwCard_txt__RrTgu",
            "li p.reviewCard_txt__RrTgu",
            'li p[class*="reveiwCard_txt"]',
            'li p[class*="reviewCard_txt"]',
            "li p",
        ]

        review_elements = []
        used_selector = None
        for selector in inner_selector_candidates:
            elems = review_list.find_elements(By.CSS_SELECTOR, selector)
            print(f"테스트용: '{selector}' 셀렉터로 찾은 p 개수 = {len(elems)}")
            if elems:
                review_elements = elems
                used_selector = selector
                break

        if not review_elements:
            print("리뷰 p 요소를 찾지 못했습니다.")
            return

        print(f"최종 사용 셀렉터: {used_selector}, 총 {len(review_elements)}개 p 수집.")

        # 텍스트 추출
        reviews = []
        for el in review_elements:
            text = el.text.strip()
            if text:
                reviews.append({"review": text})

        df = pd.DataFrame(reviews)
        df.to_csv("movie_81774_reviews.csv", index=False, encoding="utf-8-sig")

        print(f"총 {len(df)}개의 리뷰를 수집했습니다.")
        print("CSV 저장 완료!")

    finally:
        driver.quit()

        end_time = time.time()
        total_sec = end_time - start_time
        total_min = total_sec / 60

        print("\n====================")
        print(f"총 소요 시간: {total_sec:.2f}초")
        print(f"총 소요 시간: {total_min:.2f}분")
        print("====================\n")


if __name__ == "__main__":
    main()
