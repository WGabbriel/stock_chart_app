import yfinance
import plotly.express as express


def plot_price(ticker):

    data = yfinance.download(ticker, multi_level_index=False)

    fig = express.line(data.reset_index(), x="Date", y=["Close"])

    return fig
