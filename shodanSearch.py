import shodan
#VSAT is used by boats.
#Cameras is used for searching webcams
#ICS for industrial control system
SHODAN_API_KEY = "7ZZOLTZGEwwMNRO07zy2Gbp4rXiNM9uM"

api = shodan.Shodan(SHODAN_API_KEY)

try:
    print('You can search for common IOT devices such as: \n 1 VSAT (for searching boats) '+
    '\n 2 Cameras (for searching webcams) \n 3 ICS (for industrial control systems)')

    input = input('So... whats your choice?')

    aux = ''
    if input == 1:
        aux = 'VSAT'
    if input == 2:
        aux = 'Cameras'
    if input == 3:
        aux = 'ICS'

    if aux != '':
        results = ''
        results = api.search(input)

    if results == '':
        print 'No results found'
    else:
        print('Results found: {}'.format(results['total']))

    for result in results['matches']:
        print('IP: {}'.format(result['ip_str']))
        print('Host name: {}'.format(result['hostnames']))
        print(result['data'])
        print('')
except Exception as e:
    print e
