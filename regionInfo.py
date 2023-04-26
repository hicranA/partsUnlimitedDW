def get_region(state):
    regions = {
        'AL': 'South',
        'AK': 'West',
        'AZ': 'West',
        'AR': 'South',
        'CA': 'West',
        'CO': 'West',
        'CT': 'Northeast',
        'DE': 'South',
        'FL': 'South',
        'GA': 'South',
        'HI': 'West',
        'ID': 'West',
        'IL': 'Midwest',
        'IN': 'Midwest',
        'IA': 'Midwest',
        'KS': 'Midwest',
        'KY': 'South',
        'LA': 'South',
        'ME': 'Northeast',
        'MD': 'South',
        'MA': 'Northeast',
        'MI': 'Midwest',
        'MN': 'Midwest',
        'MS': 'South',
        'MO': 'Midwest',
        'MT': 'West',
        'NE': 'Midwest',
        'NV': 'West',
        'NH': 'Northeast',
        'NJ': 'Northeast',
        'NM': 'West',
        'NY': 'Northeast',
        'NC': 'South',
        'ND': 'Midwest',
        'OH': 'Midwest',
        'OK': 'South',
        'OR': 'West',
        'PA': 'Northeast',
        'RI': 'Northeast',
        'SC': 'South',
        'SD': 'Midwest',
        'TN': 'South',
        'TX': 'South',
        'UT': 'West',
        'VT': 'Northeast',
        'VA': 'South',
        'WA': 'West',
        'WV': 'South',
        'WI': 'Midwest',
        'WY': 'West',
        'Unknown':'Unknown'
    }
    return regions.get(state, None)
