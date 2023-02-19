from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from data_ingest import WeatherRecord, WeatherStats, Base

app = Flask(__name__)
api = Api(app)

# Define the maximum number of items per page
MAX_ITEMS_PER_PAGE = 50

# Configure database connection
engine = create_engine("sqlite:///weather_data.db")
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)

# Define the data models for Swagger documentation
weather_record_model = api.model(
    "WeatherRecord",
    {
        "station": fields.String,
        "date": fields.Date,
        "max_temp": fields.Float,
        "min_temp": fields.Float,
        "precipitation": fields.Float,
    },
)

weather_stats_model = api.model(
    "WeatherStats",
    {
        "year": fields.Integer,
        "station": fields.String,
        "avg_max_temp": fields.Float,
        "avg_min_temp": fields.Float,
        "total_precipitation": fields.Float,
    },
)


@api.route("/api/weather")
class WeatherRecords(Resource):
    @api.expect(weather_record_model)
    @api.doc(
        params={
            "date": "Filter by date (YYYY-MM-DD)",
            "station": "Filter by station ID",
            "page": "Page number",
            "page_size": "Number of records per page",
        }
    )
    def get(self):
        session = DBSession()
        # Parse query string parameters
        date = request.args.get("date", None)
        station = request.args.get("station", None)
        page = int(request.args.get("page", 1))
        page_size = int(request.args.get("page_size", 100))
        # Build query based on query string parameters
        query = session.query(WeatherRecord)
        if date:
            query = query.filter(WeatherRecord.date == date)
        if station:
            query = query.filter(WeatherRecord.station == station)
        query = query.order_by(WeatherRecord.date.asc())
        query = query.limit(page_size).offset((page - 1) * page_size)

        # Serialize query results and return as JSON
        results = [row.__dict__ for row in query.all()]
        results = [
            {key: value for key, value in row.items() if key != "_sa_instance_state"}
            for row in results
        ]
        session.close()
        print(results)
        return jsonify(results)


@api.route("/api/weather/stats")
class WeatherStat(Resource):
    @api.expect(weather_stats_model)
    @api.doc(
        params={
            "year": "Filter by year",
            "station": "Filter by station ID",
            "page": "Page number",
            "page_size": "Number of records per page",
        }
    )
    def get(self):
        session = DBSession()
        # Parse query string parameters
        year = int(request.args.get("year", 1998))
        station = request.args.get("station", None)
        page = int(request.args.get("page", 1))
        page_size = int(request.args.get("page_size", 100))

        # Build query based on query string parameters
        query = session.query(WeatherStats)
        if year:
            query = query.filter(WeatherStats.year == year)
        if station:
            query = query.filter(WeatherStats.station == station)
        query = query.order_by(WeatherStats.year.asc())

        query = query.limit(page_size).offset((page - 1) * page_size)

        # Serialize query results and return as JSON
        results = [row.__dict__ for row in query.all()]
        results = [
            {key: value for key, value in row.items() if key != "_sa_instance_state"}
            for row in results
        ]
        session.close()
        return jsonify(results)


# Add Swagger documentation
api.add_namespace(api.namespace("swagger", description="Swagger UI"))


@api.route("/swagger.json")
class Swagger(Resource):
    def get(self):
        return api.as_json()


if __name__ == "__main__":
    app.run(debug=True, port=8080)
