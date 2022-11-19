from models.database import db_session
from models.models import OnegaiContent


c1 = OnegaiContent("お願いします","5000兆円ください")
c2 = OnegaiContent("助けてください","ぽんぽんぺいん")
c3 = OnegaiContent("許してください","なんでもしますから")
db_session.add(c1)
db_session.add(c2)
db_session.add(c3)
db_session.commit()



"""

sqlite3 onegai.db

Select * from onegaicontents;




"""