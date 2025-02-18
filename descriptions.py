# descriptions.py
# Descriptions for road signs
# All descriptions retrieved from https://routetogermany.com/drivingingermany/road-signs (date of retrieval 10-01-2025)

DESCRIPTIONS = {
    0 : "20 km/h speed limit",
    1 : "30 km/h speed limit",
    2 : "50 km/h speed limit",
    3 : "60 km/h speed limit",
    4 : "70 km/h speed limit",
    5 : "80 km/h speed limit",
    6 : "End of 80 km/h speed limit",
    7 : "100 km/h speed limit",
    8 : "120 km/h speed limit",
    9 : "No passing/overtaking for any vehicle type",
    10 : "No passing/overtaking for vehicles with a weight over 3.5 tonnes",
    11 : "Priority at the upcoming intersection or crossing",
    12 : "Priority road start - priority at all upcoming intersections and crossings",
    13 : "Yield right-of-way",
    14 : "Stop and yield",
    15 : "No entry for any vehicle type",
    16 : "No entry for vehicles with a weight over 3.5 tonnes",
    17 : "Do not enter",
    18 : "General danger/warning sign",
    19 : "Single curve approaching in the left direction",
    20 : "Single curve approaching in the right direction",
    21 : "Double curve approaching - first to the left",
    22 : "Rough road ahead",
    23 : "Danger of skidding or slipping",
    24 : "Road narrows from the right side - yield to oncoming traffic",
    25 : "Work in process - be aware of workers on the road",
    26 : "Traffic signal ahead",
    27 : "Pedestrian crossing ahead",
    28 : "Pay attention to children",
    29 : "Be aware of cyclists",
    30 : "Icy road ahead - can be slippery",
    31 : "Wild animals may cross the road",
    32 : "End of all previously set passing and speed restrictions",
    33 : "Must turn right",
    34 : "Must turn left",
    35 : "Must continue straight ahead - no permitted turns",
    36 : "Must continue straight ahead or turn right",
    37 : "Must continue straight ahead or turn left",
    38 : "Drive from the right of the obstacle",
    39 : "Drive from the left of the obstacle",
    40 : "Roundabout",
    41 : "End of no-passing zone for vehicles under 3.5 tonnes",
    42 : "End of all passing restrictions"
}

def get_description(label):
    return DESCRIPTIONS.get(label, "Unknown Sign")

# Test
if __name__ == "__main__":
    test_label = 9
    print(f"Sign {test_label}: {get_description(test_label)}")