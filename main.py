from flask import Flask
from config import Config


from app.models.movie import Movies
from app.models.Saloon import Saloon
from app.models.Employee import Employee
from app.models.JobTitle import JobTitle
from app.models.MovingTickets import MovingTickets
from app.models.Places import Places
from app.models.PriceForTickets import PriceForTickets
from app.models.Seanses import Seanses
from app.models.SectorSaloon import SectorSaloon
from app.models.Tickets import Tickets

from app.routers.index import index_bp as index
from app.routers.movies import movies_bp as movies


app = Flask(__name__)
app.template_folder = 'app/tamplates' # папка с шаблонами
app.static_folder = 'app/static' # папка со статикой
app.config.from_object(Config) # подключаем конфигурацию


database = app.config['DATABASE']
with database:
    database.create_tables({Movies,Saloon,Employee,JobTitle,MovingTickets,Places,PriceForTickets,Seanses,SectorSaloon,Tickets})
    # Movies.create(name='Титаник', duration = 120, rentail_start_date = '1997-11-18',
    # rental_finish_date = '1997-11-18', sales_company = 'Pmvbhbkbhbhjbbyu')
    # Saloon.create(name = 'VIP', count_place = 350, description = 'Кино про корабль',
    # number_of_ros =25, number_of_places= 50)
    # Employee.create(name = 'БЕК', title = 'Один дома 1!', passord = '****')
    # JobTitle.create(title = 'МИКИ-МАУС')
    # MovingTickets.create(ticket = 'ecqd', date = '22.12.2023',
    # operation = 122,employee = 'wwec')
    # Places.create(saloon = 'VIP', row_number = 12, row_place = 25)
    # PriceForTickets.create(seanses = 'wec', sector = SectorSaloon, price = 350)
    # Seanses.create( date = '23.1.2024',time = '20:21', movie = 'Титаник')
    # SectorSaloon.create(saloon = 'wec', name = 'den', description = 'era')
    # Tickets.create( ticket_number = '14',date_created = '24.12.2023',
    # seanses = 'Титаник', places =  'wec', payed = 350,booking = 220, creashed = 2)

app.register_blueprint(index)
app.register_blueprint(movies)


@app.route('/ERBOOL')
def erbol():
    return f'<h1 style="font-size: 300px;">ERBOOOL!</h1>'

# @app.route('/seanses')
# def seanses():
#     return render_template('seanses/seanses.html', seanses=Seanses
#          .select(Seanses, Movies).join(Movies).order_by(Seanses.date))

# @app.route('/seanses/<int:id>')
# def seanse(id):
#     return render_template('seanses/seanse.html', seanses=Seanses.filter(movie=id))


if __name__ == '__main__':
    app.run(debug=True)