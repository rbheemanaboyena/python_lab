import os
import yaml
from sqlalchemy import create_engine, Column, Integer, Date, Float, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.declarative import declarative_base
from concurrent.futures import ThreadPoolExecutor, as_completed
from multiprocessing import cpu_count
import logging
import logging.config as logConfig
from datetime import datetime



Base = declarative_base()

if not os.path.exists("logs"):
    os.makedirs("logs")


def get_logger():
    with open("config/log_config.yaml") as file:
        log_configuration = yaml.safe_load(file)

    logConfig.dictConfig(log_configuration)
    logger = logging.getLogger("fileHandlingLogger")
    return logger


logger = get_logger()


class WeatherRecord(Base):
    __tablename__ = "weather_data"
    date = Column(Date, primary_key=True)
    station = Column(String)
    max_temp = Column(Float)
    min_temp = Column(Float)
    precipitation = Column(Float)


# Define the WeatherStats model to store the results
class WeatherStats(Base):
    __tablename__ = "weather_stats"
    year = Column(Integer, primary_key=True)
    station = Column(String)
    avg_max_temp = Column(Float)
    avg_min_temp = Column(Float)
    total_precipitation = Column(Float)


def create_session():
    engine = create_engine("sqlite:///weather_data.db")
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


def ingest_data(file_path):
    start_time = datetime.now()
    session = create_session()
    records_ingested = 0
    station_name = os.path.splitext(os.path.basename(file_path))[0]
    with open(file_path, "r") as file:
        for line in file:
            data = line.strip().split("\t")
            date = datetime.strptime(data[0], "%Y%m%d").date()
            max_temp = float(data[1]) / 10.0 if data[1] != "-9999" else None
            min_temp = float(data[2]) / 10.0 if data[2] != "-9999" else None
            precipitation = float(data[3]) / 10.0 if data[3] != "-9999" else None
            # Check if the record already exists in the database
            existing_record = (
                session.query(WeatherRecord).filter(WeatherRecord.date == date).first()
            )
            # If the record doesn't exist, add it to the database

            try:
                if existing_record is None:
                    record = WeatherRecord(
                        date=date,
                        station=station_name,
                        max_temp=max_temp,
                        min_temp=min_temp,
                        precipitation=precipitation,
                    )
                    session.add(record)
                    records_ingested += 1
                    session.commit()
            except IntegrityError as e:
                logging.error(f"Duplicate record for date {date}: {e}")
                session.rollback()

    end_time = datetime.now()
    logging.info(f"Ingested {records_ingested} records in {end_time - start_time}")
    session.close()
    return records_ingested


def stats():
    session = create_session()
    records_ingested = 0
    # Query the raw weather data records
    weather_data = session.query(WeatherRecord).all()

    # Create a dictionary to store the intermediate results for each year and weather station
    stats = {}
    for data in weather_data:
        # Skip missing data
        if data.max_temp is None or data.min_temp is None or data.precipitation is None:
            continue
        year = int(data.date.strftime("%Y"))
        station = data.station

        # Create a new entry in the dictionary for this year and weather station if it doesn't already exist
        if (year, station) not in stats:
            stats[(year, station)] = {
                "count": 0,
                "sum_max_temp": 0,
                "sum_min_temp": 0,
                "sum_precipitation": 0,
            }

        # Update the intermediate results for this year and weather station
        stats[(year, station)]["count"] += 1
        stats[(year, station)]["sum_max_temp"] += data.max_temp
        stats[(year, station)]["sum_min_temp"] += data.min_temp
        stats[(year, station)]["sum_precipitation"] += data.precipitation

    # Convert the intermediate results to the final results and store them in the WeatherStats table
    for (year, station), intermediate_stats in stats.items():
        count = intermediate_stats["count"]
        avg_max_temp = intermediate_stats["sum_max_temp"] / count
        avg_min_temp = intermediate_stats["sum_min_temp"] / count
        total_precipitation = intermediate_stats["sum_precipitation"] / count

        weather_stat = WeatherStats(
            year=year,
            station=station,
            avg_max_temp=avg_max_temp,
            avg_min_temp=avg_min_temp,
            total_precipitation=total_precipitation,
        )

        try:
            session.add(weather_stat)
            records_ingested += 1
            session.commit()
        except IntegrityError as e:
            logging.error(f"Duplicate record for date {datetime.now()}: {e}")
            session.rollback()

            # Update the existing record
            existing_record = (
                session.query(WeatherStats)
                .filter_by(year=year, station=station)
                .first()
            )
            if (
                data.max_temp is None
                or data.min_temp is None
                or data.precipitation is None
            ):
                existing_record.avg_max_temp = avg_max_temp
                existing_record.avg_min_temp = avg_min_temp
                existing_record.total_precipitation = total_precipitation
                session.add(existing_record)
                session.commit()
    logging.info(f"Ingested {records_ingested} records")
    session.close()


def main():
    cpu_cores = cpu_count()
    batch_size = cpu_cores * 5
    path = os.getcwd() + "/data" + "/wx_data/"
    dir_list = os.listdir(path)
    file_names = [path + file for file in dir_list]
    start_time = datetime.now()
    logging.info("Ingestion process started at {}".format(start_time))
    with ThreadPoolExecutor(max_workers=batch_size) as executor:
        results = [executor.submit(ingest_data, file_name) for file_name in file_names]
        for f in as_completed(results):
            result = f.result()
            logging.info(result)
    end_time = datetime.now()
    logging.info("Ingestion process completed at {}".format(end_time))
    logging.info("Total time taken for ingestion: {}".format(end_time - start_time))
    stats()


if __name__ == "__main__":
    engine = create_engine("sqlite:///weather_data.db")
    Base.metadata.create_all(engine)
    main()
