from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import cv2
import numpy as np

# reading image

WIDTH = 1920  #WIDTH OF VIDEO FRAME
HEIGHT = 1080 #HEIGHT OF VIDEO FRAME
cropBegin = 50 #CROP VIDEO FRAME FROM THIS POINT
img = cv2.imread('testpic.png')
img = cv2.resize(img, (1500, 900))[cropBegin:HEIGHT,0:WIDTH]
picture = px.imshow(img)



def blackout(image,ld,lu,rd,ru):
    
    
    triangle_cnt = np.array( [[0,0], [lu,0], [0,900+ld]] )
    triangle_cnt2 = np.array( [[WIDTH,0], [WIDTH-ru,0], [WIDTH,rd]] )
    cv2.drawContours(image, [triangle_cnt], 0, (0,0,0), -1)
    cv2.drawContours(image, [triangle_cnt2], 0, (0,0,0), -1)

    return image
# dashboard

app = Dash(__name__)


app.layout = html.Div([
    html.H1('speed detection', style={'textAlign': 'center'}),


    html.Div(children=[

        html.Table([
            html.Tr([
                html.Label('left-side down : ',
                           style={'padding-right': '10px'}),
                dcc.Input(value=0, type='number', min=0, step=50, id='ld'),
            ]),
            html.Tr([html.Label('left-side up :', style={'padding-right': '33px'}),
                     dcc.Input(value=0, type='number',
                               min=0, step=50, id='lu'),
                     ]),

            html.Tr(
                [html.Label('right-side down   : ', style={'padding-right': '1px'}),
                 dcc.Input(value=0, type='number', min=0, step=50, id='rd'),
                 ]),

            html.Tr(
                [html.Label('right-side up   : ', style={'padding-right': '20px'}),
                 dcc.Input(value=0, type='number', min=0, step=50, id='ru'),
                 ]),
            # html.Tr([html.Button('submit', id='save'),])

        ]),
        

    ]),
    html.Hr(),
    html.Div([
        dcc.Graph(id='image',
                 figure=picture )
    ], style={'width': '1920'}),
    html.Hr(),
    
    
])


@app.callback(
    
    Output('image','figure'),
    Input('ld', 'value'),
    Input('lu', 'value'),
    Input('rd', 'value'),
    Input('ru', 'value')
)
def update(ld,lu,rd ,ru):
    
    global img
    
    image = blackout(img,ld,lu,rd,ru)
    picture = px.imshow(image)
    return picture



    


if __name__ == '__main__':
    app.run_server(debug=True)



# اشکالی داشتی تلگرام پیام بده
# this_is_alli