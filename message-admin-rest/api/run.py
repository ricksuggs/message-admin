from eve import Eve
from eve_sqlalchemy import SQL
from eve_sqlalchemy.validation import ValidatorSQL
from api.models import Base

app = Eve(validator=ValidatorSQL, data=SQL)
db = app.data.driver
Base.metadata.bind = db.engine
db.Model = Base


if __name__ == "__main__":
    # using reloader will destroy the in-memory sqlite db
    app.run(debug=True, use_reloader=False)
