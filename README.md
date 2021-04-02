# Data-analysis-Project
## 코스피 관리종목 재무제표 분석을 통해 피해야할 종목 찾기


---
__파일 설명__
* kospi200_analysis_code.ipynb : 전체 코스피에서 랜덤으로 비관리종목 200개로 언더샘플링하여 머신러닝 모델에 적용시킨 코드
* all_kospi_analysis_code.ipynb : 전체 코스피 비관리종목을 모두 머신러닝 모델에 적용시킨 코드


* adm_corp_list.py : FnSpace API로 코스피 관리종목 30개 데이터 가지고오기
* non_adm_corp_list.py : FnSpace API로 코스피 비관리종목 200개 데이터 가지고오기
* get_kospi_except_adm.py : FnSpace API로 관리종목을 제외한 전체 코스피 종목 데이터 가지고오기(2019년 기준)
* get_kospi_list.py : FnSpace API로 전체 코스피 종목 데이터 가지고오기(2020년 기준)


* adm_corp2222.xlsx : adm_corp_list.py로 가지고 온 후 전처리 과정을 끝낸 관리종목 데이터 29개
* non_adm_corp_742.xlsx : get_kospi_except_adm.py로 가지고 온 비관리종목 데이터 742개 (전처리 전)
* data_input.csv : kospi200_analysis_code.ipynb에서 모델에 적용 시키기 위한 input DataFrame (피쳐 2개)
* data_input_1.xlsx :kospi200_analysis_code.ipynb에서 모델에 적용 시키기 위한 input DataFrame (피쳐 6개)
* kospi_list.xlsx : 전체 코스피 종목 데이터 가지고 올때 필요한 코스피 종목 리스트
---
  
  
  
  
