import pandas as pd 

df = pd.read_excel("C:\\Users\\SanthoshKittane\\Downloads\\Test.xlsx")
print(df.head(3))

# direct_url = "https://accionglobal-my.sharepoint.com/:x:/r/personal/santhosh_kittane_accionlabs_com/_layouts/15/Doc.aspx?sourcedoc=%7BD918ADF5-F430-4343-85A9-4FB5095C57C6%7D&file=Book%203.xlsx&action=editnew&mobileredirect=true&wdTpl=TM04101071&wdlcid=1033&wdOrigin=OFFICECOM-WEB.APPBAR%2CAPPHOME-WEB.CREATE.TEMPLATEMAIN&wdPreviousSession=4d393639-fc01-4fa1-b95b-bfba9b53c603&wdPreviousSessionSrc=AppHomeWeb&ct=1784215596536"
# df = pd.read_excel(direct_url)
# print(df.tail(3))
