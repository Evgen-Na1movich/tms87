from flask import Flask
from _datetime import datetime
import pytz

app = Flask(__name__)


@app.route('/gg')
def hello_world():
    tz_Minsk = pytz.timezone('Europe/Minsk')
    datetime_Minks = datetime.now(tz_Minsk)

    return f' Минское время:  {datetime.now().strftime("%H:%M:%S  %d.%m.%y")}'


if __name__ == '__main__':
    app.run()
