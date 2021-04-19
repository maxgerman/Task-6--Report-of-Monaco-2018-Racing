"""
Compile the statistics of the race and return it as a pretty table. Take input logs from the files in DATA_PATH or
any other specified path (by CLI argument --files). List all results in ascending or descending order or show only the
specified driver (by -d, --driver command line argument).

    Classes:

        Driver

    Functions:

        build_report(data_path=DATA_PATH) -> list of drivers. Uses:
            drivers_from_abbr(data_path) -> list of driver instances
            parse_logs(data_path, drivers) - modifies the drivers list passed as an argument
        print_report(drivers, asc=True, driver=None) -> str
        parse_cli -> namespace
"""

import os
import datetime as dt
import argparse

# defaults
DATA_PATH = '../data'
ABBR_FILENAME = 'abbreviations.txt'
START_LOG = 'start.log'
END_LOG = 'end.log'


class Driver:
    """
    A class to represent a driver.

    Attributes
    ----------
    abbr : str
        name abbreviation as in abbreviation file
    name : str
        driver's name
    team : str
        driver's team
    start_time : datetime
        start time of the lap
    stop_time : datetime
        finish time of the lap
    best_lap : timedelta
        time of the best lap

    Methods
    -------
    statistics : str
        Returns the pretty string with the driver's statistics
    """

    def __init__(self, abbr, name, team, start_time=None, stop_time=None, best_lap=None):
        self.abbr = abbr
        self.name = name
        self.team = team
        self.start_time = start_time
        self.stop_time = stop_time
        self.best_lap = best_lap

    def __repr__(self):
        return f'driver ({self.__dict__})'

    def statistics(self):
        return '{:<20} |{:<25} |{}'.format(self.name, self.team, str(self.best_lap)[:-3])


def drivers_from_abbr(data_path):
    """
    Return the list of driver instances each with their name, abbreviation and team parsed from the
    data_path/ABBR_FILENAME
    """
    drivers = []
    with open(os.path.join(data_path, ABBR_FILENAME), 'r', encoding='UTF-8') as f:
        for line in f:
            abbr, name, team = line.split('_')
            new_driver = Driver(abbr, name, team.rstrip())
            drivers.append(new_driver)
    return drivers


def parse_logs(data_path, drivers):
    """
    Modify the passed drivers list in-place: update each with the start and finish times from the parsing of the logs
    in data_path
    """
    with open(os.path.join(data_path, START_LOG), 'r', encoding='UTF-8') as f:
        # use only non-blank lines
        lines = (line for line in f if line.strip())
        for line in lines:
            abbr, start_time = line[:3], line.split('_')[1].rstrip()
            for driver in drivers:
                if driver.abbr == abbr:
                    driver.start_time = dt.datetime.strptime(start_time, "%H:%M:%S.%f")
                    break
    with open(os.path.join(data_path, END_LOG), 'r', encoding='UTF-8') as f:
        # use only non-blank lines
        lines = (line for line in f if line.strip())
        for line in lines:
            abbr, stop_time = line[:3], line.split('_')[1].rstrip()
            for driver in drivers:
                if driver.abbr == abbr:
                    driver.stop_time = dt.datetime.strptime(stop_time, "%H:%M:%S.%f")
                    break


def build_report(data_path=DATA_PATH):
    """
    Build the report based on files of name abbreviations and time logs in DATA_PATH. Calculate the best lap time for
    each driver. Return the list of drivers.
    """
    drivers = drivers_from_abbr(data_path)
    parse_logs(data_path, drivers)
    for driver in drivers:
        if driver.start_time > driver.stop_time:
            driver.start_time, driver.stop_time = driver.stop_time, driver.start_time
        driver.best_lap = driver.stop_time - driver.start_time
    return drivers


def print_report(drivers, asc=True, driver=None):
    """
    Return str report based on the report of the build_report function.

    Parameters:
    drivers - the list of drivers each with their info as properties
    asc - ascending order if True
    driver - if set, print the report of this only driver
    """
    if driver:
        for d in drivers:
            if driver.lower() in d.name.lower():
                return d.statistics()
        else:
            return 'Driver not found'

    else:
        sorted_drivers = sorted(drivers, key=lambda dr: dr.best_lap)
        res_table = ['{:2d}. '.format(i + 1) + driver.statistics() for i, driver in enumerate(sorted_drivers)]
        if asc:
            res_table.insert(15, '-' * 60)
        else:
            res_table.reverse()
        report = '\n'.join(res_table)
        return report


def parse_cli():
    """
    Parse CLI parameters and return the CLI namespace with parsed settings.

    Parameters:
        --files - path to the folder with the data files (with names ABBR_FILENAME, START_LOG, END_LOG)
        --asc or --desc - order of the report
        --driver - name or its part of the driver whose report to show

    """
    parser = argparse.ArgumentParser(prog='Report of Monaco 2018', description='Drivers\' statistics')
    parser.add_argument('-f', '--files', nargs='?', default=DATA_PATH,
                        help=f'Path to data files. Default: "{DATA_PATH}"')
    parser.add_argument('--asc', dest='asc', action='store_const', const=True, default=True,
                        help='Ascending order (default)')
    parser.add_argument('--desc', dest='asc', action='store_const', const=False, help='Descending order')
    parser.add_argument('-d', '--driver', help='Provide the driver\'s name (or its part) to show the statistics of '
                                               'the particular driver')
    cli = parser.parse_args()
    return cli


if __name__ == '__main__':
    cli = parse_cli()
    print(print_report(build_report(cli.files), cli.asc, cli.driver))
