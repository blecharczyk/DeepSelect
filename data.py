import pandas as pd

from deepselect.wizards.chart_wizards.chart_wizard import ChartWizard
from deepselect.wizards.chart_wizards.node_resources_wizard import NodeResourcesWizard

df = pd.read_csv('simplified_agent_life/Agent_1.csv')

chw = ChartWizard()
chw.show_node_id_chart(df, "Agent_1")
chw.show_resources_chart(df, "Agent_1")

dff = pd.read_csv("Results/node_0.csv")
nrw = NodeResourcesWizard()
nrw.show_node_id_chart(dff)