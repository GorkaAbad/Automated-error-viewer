import shodan
#VSAT is used by boats.
#Cameras is used for searching webcams
#ICS for industrial control system
SHODAN_API_KEY = ""
 
api = shodan.Shodan(SHODAN_API_KEY)

try:
    print('You can search for common IOT devices such as: \n VSAT (for searching boats) '+
    '\n Cameras (for searching webcams) \n ICS (for industrial control systems)')

    input = input('So... whats your choice?')

    results =  api.search(input)

    print('Results found: {}'.format(results['total']))

    for result in results['matches']:
        print('IP: {}'.format(result['ip_str']))
        print('Host name: {}'.format(result['hostnames']))
        print(result['data'])
        print('')
except Exception as e:
    raise [object Object]
