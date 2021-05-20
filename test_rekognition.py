from rekognition import tagImage


def test_tagImage():
    response = tagImage('boxoffrogs.mybucket', 'Grumpy Kitty.jpg') 
    label = response['Labels'][1]
    assert label['Name'] == 'Animal'
    
    # "{'Labels': [{'Name': 'Pet', 'Confidence': 90.67059326171875, 'Instances': [], 'Parents': [{'Name': 'Animal'}]}, {'Name': 'Animal', 'Confidence': 90.67059326171875, 'Instances': [], 'Parents': []}, {'Name': 'Cat', 'Confidence': 90.5125732421875, 'Instances': [{'BoundingBox': {'Width': 0.8149402141571045, 'Height': 0.896578848361969, 'Left': 0.11725502461194992, 'Top': 0.04479413479566574}, 'Confidence': 73.19783782958984}], 'Parents': [{'Name': 'Pet'}, {'Name': 'Mammal'}, {'Name': 'Animal'}]}, {'Name': 'Mammal', 'Confidence': 90.5125732421875, 'Instances': [], 'Parents': [{'Name': 'Animal'}]}, {'Name': 'Siamese', 'Confidence': 87.0381088256836, 'Instances': [], 'Parents': [{'Name': 'Cat'}, {'Name': 'Pet'}, {'Name': 'Mammal'}, {'Name': 'Animal'}]}, {'Name': 'Kitten', 'Confidence': 78.14095306396484, 'Instances': [], 'Parents': [{'Name': 'Cat'}, {'Name': 'Pet'}, {'Name': 'Mammal'}, {'Name': 'Animal'}]}], 'LabelModelVersion': '2.0', 'ResponseMetadata': {'RequestId': 'a1306121-fe05-41d6-94be-eb8a0bfc107f', 'HTTPStatusCode': 200, 'HTTPHeaders': {'content-type': 'application/x-amz-json-1.1', 'date': 'Thu, 20 May 2021 19:09:59 GMT', 'x-amzn-requestid': 'a1306121-fe05-41d6-94be-eb8a0bfc107f', 'content-length': '861', 'connection': 'keep-alive'}, 'RetryAttempts': 0}}"
    
