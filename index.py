import twitter_data
import validation
from dash import Dash, html, dcc
from dash.dependencies import Input, Output, State
from database import DataBase

app = Dash(__name__)

app.layout = html.Div(
    className = "body",
    children = [
        html.Div(
            className = "container",
            children = [
                html.Div(
                    className = "navbar",
                    children = [
                        html.A(
                            html.Img(
                                className = "logo",
                                src="https://cdn.icon-icons.com/icons2/122/PNG/512/twitter_socialnetwork_20007.png"
                            )
                        ),
                        dcc.Input(
                            className = "username-input",
                            id = "username-input",
                            placeholder = "Ingrese un nombre de usuario"
                        ),
                        html.Button(
                            className = "search-button",
                            id = "search-button",
                            children = "Search",
                            n_clicks = 0 
                        )
                    ]
                ),
                html.Div(
                    className = "body-info",
                    children = [
                        html.Div(
                            className = "info-card",
                            children = [
                                html.H2(
                                    className = "username",
                                    id = "username",
                                    children = "Nombre De Usuario"
                                ),
                                html.Hr(

                                ),
                                html.H3(
                                    className = "screenname",
                                    id = "screenname",
                                    children = "@thisismyname"
                                ),
                                html.Div(
                                    className = "number-info",
                                    children = [
                                        html.Div(
                                            className = "follow-card",
                                            children = [
                                                html.P(
                                                    children = "Seguidos"
                                                ),
                                                html.P(
                                                    children = "235"
                                                )
                                            ]
                                        ),
                                        html.Div(
                                            className = "followers-card",
                                            children = [
                                                html.P(
                                                    children = "Seguidores"
                                                ),
                                                html.P(
                                                    children = "235"
                                                )
                                            ]
                                        ),
                                        html.Div(
                                            className = "likes-card",
                                            children = [
                                                html.P(
                                                    children = "Likes"
                                                ),
                                                html.P(
                                                    children = "235"
                                                )
                                            ]
                                        ),
                                    ]
                                )
                            ]
                        ),
                    ]
                )
            ]
        )
    ]
)

@app.callback(
    Output('screenname', 'children'),
    Input('search-button', 'n_clicks'),
    State('username-input', 'value')
)
def call_get_user(n_clicks, username):
    response = validation.user_validation(username)
    database = DataBase()
    if response == True :
        user = database.select_user(username)
    else : 
        user = twitter_data.get_user(username)
        database.insert_user(user) 
    
    return u'@{}'.format(username)

if __name__ == '__main__':
    app.run_server(debug=True)

