import os
import datetime as dt
import argparse


class Driver:
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


def build_report(data_path='data'):
    drivers = []
    # create drivers
    with open(os.path.join(data_path, 'abbreviations.txt'), 'r', encoding='UTF-8') as f:
        for line in f:
            abbr, name, team = line.split('_')
            new_driver = Driver(abbr, name, team.rstrip())
            drivers.append(new_driver)
    # add start times
    with open(os.path.join(data_path, 'start.log'), 'r', encoding='UTF-8') as f:
        # use only non-blank lines
        lines = (line for line in f if line.strip())
        for line in lines:
            abbr, start_time = line[:3], line.split('_')[1].rstrip()
            for driver in drivers:
                if driver.abbr == abbr:
                    driver.start_time = dt.datetime.strptime(start_time, "%H:%M:%S.%f")
                    break
    # add stop times
    with open(os.path.join(data_path, 'end.log'), 'r', encoding='UTF-8') as f:
        # use only non-blank lines
        lines = (line for line in f if line.strip())
        for line in lines:
            abbr, stop_time = line[:3], line.split('_')[1].rstrip()
            for driver in drivers:
                if driver.abbr == abbr:
                    driver.stop_time = dt.datetime.strptime(stop_time, "%H:%M:%S.%f")
                    break
    # validate times: start must be less than stop
    for driver in drivers:
        if driver.start_time > driver.stop_time:
            driver.start_time, driver.stop_time = driver.stop_time, driver.start_time
        # calc and add best lap times
        driver.best_lap = driver.stop_time - driver.start_time
    return drivers


def print_report(drivers, asc=True, driver=None):
    # if requested report about one driver only
    if driver:
        res = []
        for d in drivers:
            if driver in d.name:
                return d.statistics()
        else:
            return 'Driver not found'
    # if report about all is requested
    else:
        sorted_drivers = sorted(drivers, key=lambda dr: dr.best_lap)
        res_table = ['{:2d}. '.format(i + 1) + driver.statistics() for i, driver in enumerate(sorted_drivers)]
        # divider after first 15 if the order is ascending (otherwise, no point)
        if asc:
            res_table.insert(15, '-' * 60)
        else:
            res_table.reverse()
        report = '\n'.join(res_table)
        return report


def parse_cli():
    parser = argparse.ArgumentParser(prog='Report of Monaco 2018', description='Drivers\' statistics')
    parser.add_argument('-f', '--files', nargs='?', default='data', help='Path to data files. Default: "data"')
    parser.add_argument('--asc', dest='asc', action='store_const', const=True, default=True, help='Ascending order (default)')
    parser.add_argument('--desc', dest='asc', action='store_const', const=False, help='Descending order')
    parser.add_argument('-d', '--driver', help='Provide the driver\'s name (or its part) to show the statistics of '
                                               'the particular driver')
    cli = parser.parse_args()
    return cli


if __name__ == '__main__':
    cli = parse_cli()
    print(print_report(build_report(cli.files), cli.asc, cli.driver))
