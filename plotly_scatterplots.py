{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "        <script type=\"text/javascript\">\n",
       "        window.PlotlyConfig = {MathJaxConfig: 'local'};\n",
       "        if (window.MathJax) {MathJax.Hub.Config({SVG: {font: \"STIX-Web\"}});}\n",
       "        if (typeof require !== 'undefined') {\n",
       "        require.undef(\"plotly\");\n",
       "        requirejs.config({\n",
       "            paths: {\n",
       "                'plotly': ['https://cdn.plot.ly/plotly-latest.min']\n",
       "            }\n",
       "        });\n",
       "        require(['plotly'], function(Plotly) {\n",
       "            window._Plotly = Plotly;\n",
       "        });\n",
       "        }\n",
       "        </script>\n",
       "        "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "        <script type=\"text/javascript\">\n",
       "        window.PlotlyConfig = {MathJaxConfig: 'local'};\n",
       "        if (window.MathJax) {MathJax.Hub.Config({SVG: {font: \"STIX-Web\"}});}\n",
       "        if (typeof require !== 'undefined') {\n",
       "        require.undef(\"plotly\");\n",
       "        requirejs.config({\n",
       "            paths: {\n",
       "                'plotly': ['https://cdn.plot.ly/plotly-latest.min']\n",
       "            }\n",
       "        });\n",
       "        require(['plotly'], function(Plotly) {\n",
       "            window._Plotly = Plotly;\n",
       "        });\n",
       "        }\n",
       "        </script>\n",
       "        "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import plotly\n",
    "import plotly.plotly as py\n",
    "import plotly.graph_objs as go\n",
    "import cufflinks as cf\n",
    "from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot\n",
    "init_notebook_mode(connected=True)\n",
    "cf.go_offline()\n",
    "\n",
    "plotly.tools.set_credentials_file(username='rsarkar', api_key='soC4UzltcUBSXM3o1a33')\n",
    "\n",
    "\n",
    "class plotly_graphs:\n",
    "    def __init__(self,df):\n",
    "        self.df = df\n",
    "        \n",
    "    def scatterplot(self,target,response):\n",
    "        trace = go.Scatter(\n",
    "            x = self.df[response],\n",
    "            y = self.df[target],\n",
    "            name = response,\n",
    "            mode = 'markers',\n",
    "            marker = dict(\n",
    "            size = 10,\n",
    "            color = 'rgba(152, 0, 0, .8)'\n",
    "        )\n",
    "    )\n",
    "\n",
    "\n",
    "        data = [trace]\n",
    "\n",
    "        layout = go.Layout(title = 'ScatterPlot between {} and {}'.format(target,response),\n",
    "                  yaxis = dict(\n",
    "                  title = response,\n",
    "                  zeroline = False\n",
    "                  ),\n",
    "                  xaxis = dict(\n",
    "                  title = target,\n",
    "                  zeroline = False)\n",
    "                 )\n",
    "\n",
    "        fig= go.Figure(data=data, layout=layout)\n",
    "        return py.iplot(fig)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import pandas_profiling as pp\n",
    "%matplotlib inline"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "def data_ingestion(path):\n",
    "    '''\n",
    "    To ingest the data \n",
    "    @param path: path of the file where the data is\n",
    "    '''\n",
    "    \n",
    "    try:\n",
    "        df = pd.read_csv(path) # this will read the csv file\n",
    "        return df\n",
    "    except:\n",
    "        print(\"Enter the valid Path!!! or check the accessibility\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "hp_train = data_ingestion('https://s3.us-east-2.amazonaws.com/housepriceskaggle/train.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "df =plots_plotly(hp_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Rohit\\AppData\\Local\\Continuum\\anaconda3\\envs\\houseprices\\lib\\site-packages\\IPython\\core\\display.py:689: UserWarning:\n",
      "\n",
      "Consider using IPython.display.IFrame instead\n",
      "\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<iframe id=\"igraph\" scrolling=\"no\" style=\"border:none;\" seamless=\"seamless\" src=\"https://plot.ly/~rsarkar/10.embed\" height=\"525px\" width=\"100%\"></iframe>"
      ],
      "text/plain": [
       "<chart_studio.tools.PlotlyDisplay object>"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.scatterplot_target_response('SalePrice','LotArea')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
