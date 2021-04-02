import pandas as pd

# 코스피 종목 리스트 불러와서 보통주만 필터링 한다음, 단축코드에 A를 붙여주기
df = pd.read_excel("kospi_list_1.xlsx")
kospi_df = df[df["주식종류"] == "보통주"]

a_codes = "A" + kospi_df["단축코드"]
kospi_df["단축코드"] = a_codes


k_df = kospi_df.loc[:, ['단축코드', '종목명']]
codes = k_df['단축코드']


# 관리종목 기업 29개 리스트
adm_corp_code = ['A003620', 'A003280', 'A011690', 'A012600', 'A010580', 'A007630',
                'A109070', 'A145210', 'A012170', 'A016380', 'A097230', 'A011230',
                'A071970', 'A005090', 'A010420', 'A140910', 'A007280', 'A042660',
                'A128820', 'A011810', 'A001440', 'A027970', 'A005960', 'A001470',
                'A077970', 'A009190', 'A001380', 'A003960', 'A003120']

# 불러온 코스피 리스트에 관리종목(29개)을 제외하고 비관리종목 리스트 만들기
non_adm_corp_code = []

for df_code in codes:
    if df_code in adm_corp_code:
        pass
    else:
        non_adm_corp_code.append(df_code)

print(non_adm_corp_code)
print(len(non_adm_corp_code))


afraccyear = "2019"
atoaccyear = "2019"


df2 = pd.DataFrame()

for i in range(0, len(non_adm_corp_code)):
    acode = non_adm_corp_code[i]
    json_url = "http://www.fnspace.com/Api/FinanceApi?key=34868A3196DDF56BFE35&format=json&code=" + acode + "&item=M111000,M122700,M131000,M221000,M222000,M113000,M121500,M231000&consolgb=M&annualgb=A&fraccyear=" + afraccyear + "&toaccyear=" + atoaccyear

    print(json_url)

    dsf_data = pd.read_json(json_url)
    df = pd.DataFrame(dsf_data["dataset"][0])

    df2 = df2.append(df)

    print(df2)

df2.to_excel("non_adm_corp_742_name.xlsx")
