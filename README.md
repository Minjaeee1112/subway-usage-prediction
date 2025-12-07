# subway-usage-prediction
2025년 10월 서울시 지하철 승하차 인원 분석 및 예측 프로젝트

# 서울시 지하철 승하차 인원 분석 및 11월 예측 프로젝트

이 프로젝트는 서울 열린데이터광장에서 제공하는  
**2025년 10월 서울시 지하철 호선별·역별 승하차 인원 데이터**를 활용하여

- 데이터 전처리 및 시각화
- 역별/노선별 이용객 분석
- 2025년 11월 승하차 인원 예측

을 수행한 프로젝트입니다.

---

## 사용 데이터

- 파일명: `CARD_SUBWAY_MONTH_202510.csv`
- 출처: https://data.seoul.go.kr/](https://www.data.go.kr/data/15134550/fileData.do#tab-layer-file)


## 사용한 기술

- Python 3
- Google Colab
- Pandas
- Matplotlib
- Numpy



### 데이터 전처리
- 날짜 형식 변환 (YYYYMMDD → datetime)
- 자료형 정리
- 결측치 제거
- 총 이용객수 컬럼 생성

### 분석
- 노선별 이용객수 추이
- 역별 이용객수 TOP10
- 날짜별 총 이용객수 시각화

### 예측
- 1차 회귀 기반 단순 시계열 예측(11월 예상 승/하차 인원)
