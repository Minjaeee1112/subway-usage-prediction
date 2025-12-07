# 1. 나눔고딕 설치 (이미 설치했으면 다시 실행해도 괜찮음)
!apt-get update -qq
!apt-get install -qq fonts-nanum fonts-nanum-extra

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns

# 2. 나눔 폰트 경로 찾기
nanum_paths = fm.findSystemFonts(fontpaths=['/usr/share/fonts/truetype/nanum'])
print("찾은 나눔 폰트 개수:", len(nanum_paths))

# 3. 폰트 매니저에 수동 등록
for path in nanum_paths:
    fm.fontManager.addfont(path)

# 4. NanumGothic 폰트 이름 얻기
nanum_gothic_path = '/usr/share/fonts/truetype/nanum/NanumGothic.ttf'
nanum_gothic_name = fm.FontProperties(fname=nanum_gothic_path).get_name()
print("NanumGothic 폰트 이름:", nanum_gothic_name)

# 5. matplotlib / seaborn 설정
plt.rcParams['font.family'] = nanum_gothic_name
plt.rcParams['axes.unicode_minus'] = False
sns.set(font=nanum_gothic_name)

print("현재 설정된 폰트:", plt.rcParams['font.family'])

import pandas as pd
import matplotlib.pyplot as plt
from google.colab import files

# 1) 파일 업로드
uploaded = files.upload()
file_name = list(uploaded.keys())[0]
print("읽을 파일:", file_name)

# 2) 필요한 컬럼 + 타입 강제 지정해서 읽기
df = pd.read_csv(
    file_name,
    encoding='utf-8-sig',
    usecols=['사용일자', '노선명', '역명', '승차총승객수', '하차총승객수', '등록일자'],
    dtype={
        '사용일자': 'string',
        '노선명': 'string',
        '역명': 'string',
        '승차총승객수': 'int64',
        '하차총승객수': 'int64'
    }
)

print(df.head())
print(df.dtypes)

import pandas as pd
import matplotlib.pyplot as plt
from google.colab import files

# 1) 파일 업로드
uploaded = files.upload()
file_name = list(uploaded.keys())[0]
print("읽을 파일:", file_name)

# 2) 필요한 컬럼 + 타입 강제 지정해서 읽기
df = pd.read_csv(
    file_name,
    encoding='utf-8-sig',
    usecols=['사용일자', '노선명', '역명', '승차총승객수', '하차총승객수', '등록일자'],
    dtype={
        '사용일자': 'string',
        '노선명': 'string',
        '역명': 'string',
        '승차총승객수': 'int64',
        '하차총승객수': 'int64'
    }
)

print(df.head())
print(df.dtypes)

