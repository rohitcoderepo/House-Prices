import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import cufflinks as cf
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.io as pio
init_notebook_mode(connected=True)
cf.go_offline()

plotly.tools.set_credentials_file(username='rsarkar', api_key='soC4UzltcUBSXM3o1a33')


class plotly_graphs:

    def __init__(self,df):
        self.data = df
        self.data = self.data.reset_index()

        
    def scatterplot(self,target,response):
        trace = go.Scatter(
            x = self.data[response],
            y = self.data[target],
            name = response,
            text = self.data['index'],
            hoverinfo = 'text',
            mode = 'markers',
            marker = dict(
            size = 8,
            color = 'rgba(152, 0, 0, .8)'
            )
        )


        data = [trace]

        layout = go.Layout(title = 'ScatterPlot between {} and {}'.format(target,response),
                  yaxis = dict(
                  title = target,
                  zeroline = False
                  ),
                  xaxis = dict(
                  title = response,
                  zeroline = False),
                          
                 )

        fig= go.Figure(data=data, layout=layout)
        return py.iplot(fig)