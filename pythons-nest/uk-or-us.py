# A pure Python work-through of my cities create form for Vacilando (built in Django, Python, and React). The form responds, depending on the data that the user inputs.

cities = {
    'london': {
        'name': 'boroughs',
        'valid_options': ['Westminster', 'Kensington and Chelsea', 'Hammersmith and Fulham', 'Wandsworth', 'Sutton', 'Merton', 'Kingston upon Thames', 'Richmond upon Thames', 'Hounslow', 'Hillingdon', 'Ealing', 'Harrow', 'Brent', 'Barnet', 'Enfield', 'Haringey', 'Camden', 'Islington', 'Hackney', 'Tower Hamlets', 'Newham', 'Barking and Dagenham', 'Havering', 'Waltham Forest', 'Redbridge', 'Bexley', 'Bromley', 'Croydon', 'Greenwich', 'Lewisham', 'Southwark', 'Lambeth']
    },
    'new_york': {
        'name': 'boroughs',
        'valid_options': ['Manhattan', 'Brooklyn', 'Bronx', 'Staten Island', 'Queens']
    },
    'manchester': {
        'name': 'boroughs',
        'valid_options': ['Oldham', 'Stockport', 'Salford', 'Manchester', 'Rochdale', 'Bury', 'Bolton', 'Tameside', 'Trafford', 'Wigan']
    }
}

print("There are %d London boroughs" % (len(cities['london']['valid_options'])))
print("There are %d New York boroughs" % (len(cities['new_york']['valid_options'])))
print("There are %d Manchester boroughs" % (len(cities['manchester']['valid_options'])))

areas = {
    'united_kingdom': {
        'name': 'counties',
        'valid_options': ['Greater London', 'City of London', 'Kent', 'Surrey', 'Berkshire', 'Buckinghamshire', 'Hertfordshire', 'Essex', 'Bedfordshire', 'Cambridgeshire', 'Suffolk', 'Norfolk', 'East Sussex', 'West Sussex', 'Hampshire', 'Isle of Wight', 'Oxfordshire', 'Wiltshire', 'Bristol', 'Dorset', 'Somerset', 'Devon', 'Cornwall', 'Gloucestershire', 'Worcestershire', 'Warwickshire', 'West Midlands', 'Northamptonshire', 'Leicestershire', 'Rutland', 'Lincolnshire', 'Herefordshire', 'Shropshire', 'Staffordshire', 'Derbyshire', 'Cheshire', 'Merseyside', 'North Yorkshire', 'East Yorkshire', 'West Yorkshire', 'South Yorkshire', 'Nottinghamshire', 'Greater Manchester', 'Lancashire', 'Cumbria', 'Durham', 'Tyne and Wear', 'Northumberland']
    },
    'united_states_of_america': {
        'name': 'states',
        'valid_options': {
            'alabama': 'al',
            'alaska': 'ak',
            'arizona': 'az',
            'arkansas': 'ar',
            'california': 'ca',
            'colorado': 'co',
            'connecticut': 'ct',
            'delaware': 'de',
            'florida': 'fl',
            'georgia': 'ga',
            'hawaii': 'hi',
            'idaho': 'id',
            'illinois': 'il',
            'indiana': 'in',
            'iowa': 'ia',
            'kansas': 'ks',
            'kentucky': 'ky',
            'louisiana': 'la',
            'maine': 'me',
            'maryland': 'md',
            'massachusetts': 'ma',
            'michigan': 'mi',
            'minnesota': 'mn',
            'mississippi': 'ms',
            'missouri': 'mo',
            'montana': 'mt',
            'nebraska': 'ne',
            'nevada': 'nv',
            'new hampshire': 'nh',
            'new jersey': 'nj',
            'new mexico': 'nm',
            'north carolina': 'nc',
            'north dakota': 'nd',
            'new york': 'ny',
            'ohio': 'oh',
            'oklahoma': 'ok',
            'oregon': 'or',
            'pennsylvania': 'pa',
            'rhode island': 'ri',
            'south carolina': 'sc',
            'south dakota': 'sd',
            'tennessee': 'tn',
            'texas': 'tx',
            'utah': 'ut',
            'vermont': 'va',
            'virginia': 'va',
            'washington': 'wa',
            'west virginia': 'wv',
            'wisconsin': 'wi',
            'wyoming': 'wy'
        }
    }
}

print("There are %d English counties" % (len(areas['united_kingdom']['valid_options'])))
print("There are %d American states" % (len(areas['united_states_of_america']['valid_options'])))
