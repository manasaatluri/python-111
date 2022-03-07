import pandas as pd
import plotly.express as ps

df = pd.read_csv("data.csv")

mean = df.groupby(["student_id", "level"], as_index=False)["attempt"].mean()
m=ps.scatter(mean,x="student_id" ,y="level" ,size="attempt",color="attempt")
m.show()