import pandas as pd

from deepselect.wizards.chart_wizards.chart_wizard import ChartWizard

df = pd.read_csv('simplified_agent_life/First_type4.csv')

chw = ChartWizard()
chw.show_node_id_chart(df)
chw.show_resources_chart(df, "First_type4")