

### 코스피 관리종목 30개 가지고오기


import pandas as pd

code = ['A003620', 'A003280', 'A011690', 'A012600', 'A010580', 'A007630',
       'A109070', 'A145210', 'A012170', 'A016380', 'A097230', 'A011230',
       'A071970', 'A005090', 'A010420', 'A140910', 'A007280', 'A042660',
       'A128820', 'A011810', 'A001440', 'A027970', 'A005960', 'A001470',
       'A077970', 'A009190', 'A001260', 'A001380', 'A003960', 'A003120']
fraccyear = ["2019", "2019", "2019", "2019", "2018", "2018", "2018", "2017", "2018", "2018", "2018", "2017", "2017", "2017", "2017",
             "2017", "2016", "2016", "2016", "2016", "2014", "2015", "2014", "2014", "2013", "2014", "2012", "2012", "2012", "2012"]
toaccyear = ["2019", "2019", "2019", "2019", "2018", "2018", "2018", "2017", "2018", "2018", "2018", "2017", "2017", "2017", "2017",
             "2017", "2016", "2016", "2016", "2016", "2014", "2015", "2014", "2014", "2013", "2014", "2012", "2012", "2012", "2012"]

df2 = pd.DataFrame()

for i in range(0, 30):
    acode = code[i]
    afraccyear = fraccyear[i]
    atoaccyear = toaccyear[i]

    json_url = "http://www.fnspace.com/Api/FinanceApi?key=34868A3196DDF56BFE35&format=json&code=" + acode + "&item=M111000,M122700,M131000,M221000,M222000&consolgb=M&annualgb=A&fraccyear=" + afraccyear + "&toaccyear=" + atoaccyear

    print(json_url)

    dsf_data = pd.read_json(json_url)
    df = pd.DataFrame(dsf_data["dataset"][0]["DATA"])

    df2 = df2.append(df)

    print(df2)

df2.to_csv("adm_corp333333.csv", mode='w')


