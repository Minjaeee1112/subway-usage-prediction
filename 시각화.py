# 1) 사용일자에서 숫자만 뽑아 앞 8자리 사용
date_str = (
    df['사용일자']
      .astype(str)
      .str.replace(r'\D', '', regex=True)  # 숫자가 아닌 것 제거
      .str.slice(0, 8)                     # 앞 8자리: 20251001
)

df['사용일자'] = pd.to_datetime(date_str, format='%Y%m%d', errors='coerce')

# 2) 총 이용객수
df['총이용객수'] = df['승차총승객수'] + df['하차총승객수']

print("NaN 개수:")
print(df[['사용일자','승차총승객수','하차총승객수','총이용객수']].isna().sum())
print("형 변환 후 dtypes:")
print(df.dtypes)

# 3) 날짜 있는 행만 사용
df_clean = df.dropna(subset=['사용일자'])
print("정제 후 df 크기:", df_clean.shape)
print(df_clean.head())

# 4) 날짜별 합계
daily = (
    df_clean.groupby('사용일자')[['승차총승객수','하차총승객수','총이용객수']]
            .sum()
            .reset_index()
)

print("daily head:")
print(daily.head())

# 5) 그래프
plt.figure(figsize=(10,5))
plt.plot(daily['사용일자'], daily['총이용객수'], marker='o', linewidth=1)
plt.title('날짜별 지하철 총 이용객수 추세')
plt.xlabel('날짜')
plt.ylabel('총 이용객수')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 1호선~9호선 필터링
valid_lines = [f"{i}호선" for i in range(1, 10)]

df_1to9 = df_clean[df_clean['노선명'].isin(valid_lines)].copy()

print("필터링된 노선 목록:", df_1to9['노선명'].unique())


# 노선별 날짜별 총 이용객수 집계
line_daily = (
    df_1to9.groupby(['사용일자', '노선명'])['총이용객수']
    .sum()
    .reset_index()
)

# 그래프
plt.figure(figsize=(14,7))

for line in sorted(line_daily['노선명'].unique()):
    temp = line_daily[line_daily['노선명'] == line]
    plt.plot(temp['사용일자'], temp['총이용객수'], marker='o', label=line)

plt.title('1호선 ~ 9호선 날짜별 총 이용객수 추이', fontsize=14)
plt.xlabel('날짜')
plt.ylabel('총 이용객수')
plt.xticks(rotation=45)
plt.legend(title='노선명')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# 역별 총 이용객수 집계
station_usage = (
    df_clean.groupby('역명')['총이용객수']
    .sum()
    .reset_index()
    .sort_values('총이용객수', ascending=False)
)

# Top 10
top10 = station_usage.head(10)
print("역별 이용객수 TOP10")
print(top10)

plt.figure(figsize=(12,6))
plt.bar(top10['역명'], top10['총이용객수'], color='steelblue')
plt.title('역별 총 이용객수 TOP10')
plt.xlabel('역명')
plt.ylabel('총 이용객수')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt
import pandas as pd

# 1) 날짜별로 승차·하차·총 이용객수 합계
daily_pred = (
    pred_pivot.groupby('사용일자')[['승차총승객수', '하차총승객수', '총이용객수_예측']]
    .sum()
    .reset_index()
)

print("=== 2025년 11월 날짜별 예측 이용객수 ===")
print(daily_pred.head())

# 2) 그래프
plt.figure(figsize=(12, 6))

plt.plot(daily_pred['사용일자'], daily_pred['승차총승객수'], marker='o', label='승차 예측', linewidth=2)
plt.plot(daily_pred['사용일자'], daily_pred['하차총승객수'], marker='o', label='하차 예측', linewidth=2)
plt.plot(daily_pred['사용일자'], daily_pred['총이용객수_예측'], marker='o', label='총 이용객수 예측', linewidth=3)

plt.title('2025년 11월 서울시 지하철 승차/하차/총 이용객수 예측', fontsize=14)
plt.xlabel('날짜')
plt.ylabel('예측 이용객수')
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.tight_layout()
plt.show()

