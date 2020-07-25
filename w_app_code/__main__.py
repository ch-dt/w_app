import sys
from argparse import ArgumentParser

from w_app_code.core import parser_loader
from w_app_code.core import ForecastType
from w_app_code.core import Unit

def _validate_forecast_args(args):
    if args.forecast_option is None:
        err_msg = ('нужно использовать один из этих аргументов: -td/--today, -5d/--fivedays, -19d/--tendays, -w/--weekand')
        print(f'{argparser.prog}: error: {err_msg}', file=sys.stderr)
        sys.exit()

parsers = parser_loader.load('./w_app_code/parsers')

argparser = ArgumentParser(prog='weatherterm', description = "Прогноз с сайта weather.com")

required = argparser.add_argument_group('required arguments')

required.add_argument('-p', '--parser', choices=parsers.keys(), required=True, dest='parser', help=('Уточни, какой парсер использовать,чтобы узнать прогноз'))

unit_values = [name.title() for name, value in Unit.__members__.items()]

argparser.add_argument('-u', '--unit', choices=unit_values, required=False, dest='unit', help=('Уточни, в каких единицах измерения показывать температуру'))

required.add_argument('-a', '--areacode', required=True, dest='area_code', help=('код местности для которой искать прогноз. можно узнать на weather.com'))

argparser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')

argparser.add_argument('-td', '--today', dest='forecast_option', action='store_const', const=ForecastType.TODAY, help='Показать прогноз на сегодня')

args = argparser.parse_args()

_validate_forecast_args(args)

cls = parsers[arg.parser]
parser = cls()
results = parser.run(args)

for result in results:
    print(results)

