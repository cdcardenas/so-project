from modelo import db
from modelo import Stats
from comandos import get_all_stats, get_cpu, get_service, get_hdd



db.create_all()
#se capturan los datos según el formato indicado en modelo.py
stats = Stats(get cpu()[2], get_all_stats()[1], get_hdd()[1], get_service() )


#se agregan los cambios en la base de datos
db.session.add(stats)
#se guardan los cambios en la base de datos
db.session.commit()

#stats2 = Stats.query.all()
#print(stats2)

