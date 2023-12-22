#!/usr/bin/python3
'''Log parser
'''
import sys


if __name__ == '__main__':
    file_size = [0]
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0,
                    403: 0, 404: 0, 405: 0, 500: 0}

    def print_stats():
        ''' Print the stats from above data.
        '''
        print('File size: {:d}'.format(file_size[0]))
        for key in sorted(status_codes.keys()):
            if status_codes[key]:
                print('{}: {}'.format(key, status_codes[key]))

    line_num = 0
    try:
        for line in sys.stdin:
            match = line.split(' ')
            try:
                status_code = int(match[-2])
                fileSize = int(match[-1])
            except Exception:
                pass

            file_size[0] += fileSize
            if status_code in status_codes:
                status_codes[status_code] += 1

            line_num += 1
            # print after every 10 lines
            if line_num % 10 == 0:
                print_stats()
        print_stats()
    except KeyboardInterrupt:
        print_stats()
        raise
