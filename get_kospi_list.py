import pandas as pd

# 코스피 종목 리스트 불러와서 보통주만 필터링 한다음, 단축코드에 A를 붙여주기
df = pd.read_excel("kospi_list.xlsx")
kospi_df = df[df["주식종류"] == "보통주"]

a_codes = "A" + kospi_df["단축코드"]
kospi_df["단축코드"] = a_codes


k_df = kospi_df.loc[:, ['단축코드', '종목명']]
codes = k_df['단축코드']

all_kospi_code = []

for df_code in codes:
    if df_code is not None:
        all_kospi_code.append(df_code)
    else:
        pass

afraccyear = "2020"
atoaccyear = "2020"

df2 = pd.DataFrame()

for i in range(0, len(all_kospi_code)):
    acode = all_kospi_code[i]
    json_url = "http://www.fnspace.com/Api/FinanceApi?key=34868A3196DDF56BFE35&format=json&code=" + acode + "&item=M111000,M122700,M131000,M221000,M222000,M113000,M121500,M231000&consolgb=M&annualgb=A&fraccyear=" + afraccyear + "&toaccyear=" + atoaccyear

    print(json_url)


    dsf_data = pd.read_json(json_url)
    # df = pd.DataFrame(dsf_data["dataset"][0]["DATA"])
    df = pd.DataFrame(dsf_data["dataset"][0])


    df2 = df2.append(df)

    print(df2)

# df2.to_excel("all_kospi_2020.xlsx")
df2.to_excel("all_kospi_2020_name.xlsx")
