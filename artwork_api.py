
# This Api provides information related to arts.It takes data from cma_artworks.json
import json


# Get all artworks information

def get_artwork_details(search=None):
    with open('cma_artworks.json') as json_file:
        data = json.load(json_file)
    return data

# Get all artworks with unique acession_number
def get_artStyles_Details(accession_number):
    art_data = get_artwork_details()
    output_dict = [x for x in art_data if x['accession_number'] == accession_number]
    output_json = json.dumps(output_dict)

    return output_dict

#  It provides all artworks information and also gives the arts based up on title value
def get_All_Arts_Based_On_Accession_Number(search=None):
    art_data = get_artwork_details()

    if search:
        data=[x for x in art_data if search.lower() in x['title'].lower()]
        art_data=data

    returnValue = []
    size = len(art_data)
    uniqueNames = []

    for x in art_data :
        if x['accession_number'] not  in uniqueNames:
            uniqueNames.append(x['accession_number'])
            returnValue.append(x)
    return returnValue





