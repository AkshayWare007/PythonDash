import dash  # (version 1.12.0)
from dash.dependencies import Input, Output
import dash_table as dt
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

df = pd.read_csv("dataset.csv")
prev_click_value = 0

print(df)


print("*****************")


# print("*****************")
#
# df2 = df.groupby("ubr_2")["set1_price", "set2_price"].sum()
# print(df2)
#
#
# print("*****************")
#
# df3 = df.groupby("ubr_7")["set1_price", "set2_price"].sum()
# print(df3)
#
# print("*****************")
#
# df4 = df.groupby("product")["set1_price", "set2_price"].sum()
# print(df4)
# stack = []

app = dash.Dash(__name__)
# Layout
app.layout = html.Div([
    # Title - Row
    html.Div(
        [
            html.H1(
                'Hackathon',
                style={'font-family': 'Helvetica',
                       "margin-left": "20",
                       "margin-bottom": "0"},
                className='eight columns',
            )
        ],
        className='row'
    ),

    #block 2
    html.Div([
        dcc.Store(id = 'memory'),
        html.H3('Chanakya'),
        html.Div(
            [
                html.Div(
                    [
                        html.P('Hierarchy:1'),
                        dcc.Dropdown(
                                id = 'filter_x',
                                options=[{'label': c, 'value': c} for c in df.columns],
                                value='0'
                        ),
                    ],
                    className='three columns',
                    style={'margin-top': '10'}
                ),
                html.Div(
                    [
                        html.P('Hierarchy:2'),
                        dcc.Dropdown(
                                id = 'filter_y',
                                options=[{'label': c, 'value': c} for c in df.columns],
                                value='0'
                        )
                    ],
                    className='three columns',
                    style={'margin-top': '10'}
                ),
                html.Div(
                    [
                        html.Button('Submit', id='submit_button', n_clicks=0)
                    ],
                    className='one columns',
                    style={'margin-top': '40', 'margin-left':'50'}
                )
            ],
            className='row'
        ),
        html.Div(
            dt.DataTable(id = 'data_table', data=[{}]), style={'display': 'none'}
        )
    ], className = 'row',  style = {'margin-top': 20, 'border':
                                    '1px solid #C6CCD5', 'padding': 15,
                                    'border-radius': '5px'})
], style = {'padding': '25px'})

def make_table(data, output):
    return html.Div(
        [
            dt.DataTable(
                id=output,
                data=data.to_dict('rows'),
                columns=[{'id': c, 'name': c} for c in data.columns],
                style_as_list_view=True,
                selected_rows=[],
                style_cell={'padding': '5px',
                            'whiteSpace': 'no-wrap',
                            'overflow': 'hidden',
                            'textOverflow': 'ellipsis',
                            'maxWidth': 0,
                            'height': 30,
                            'textAlign': 'left'},
                style_header={
                    'backgroundColor': 'white',
                    'fontWeight': 'bold',
                    'color': 'black'
                },
                style_cell_conditional=[],
                virtualization=True,
                page_action="native",
            ),
        ], className="seven columns", style={'margin-top': '35',
                                             'margin-left': '15',
                                             'border': '1px solid #C6CCD5'}
    )

@app.callback(dash.dependencies.Output('data_table', 'data'),
    [dash.dependencies.Input('filter_x', 'value'),
     dash.dependencies.Input('filter_y', 'value'),
     dash.dependencies.Input('submit_button', 'n_clicks')])
def get_input_create_table(h1, h2, sub_button):
    print("***********************************")
    print(h1)
    print(h2)
    print(sub_button)
    return make_table(df, 'data_table')


if __name__ == '__main__':
    app.run_server(debug=True)