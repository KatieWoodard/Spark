import json
import csv


"""
data_json = open('TMobile.json', mode='r').read() #reads in the JSON file into Python as a string
data_python = json.loads(data_json) #turns the string into a json Python object
data_python = data_python.filter(word for word in data_python if word.lower() not in stopwords)"""
csv_out = open('TMobileTweets.csv', 'a') #opens csv file
writer = csv.writer(csv_out) #create the csv writer object


with open('TMobile.json', 'r') as f:
    for line in f:
        data_python = json.loads(line) #turns the string into a json Python object
        print data_python["text"]
        writer.writerow([data_python["text"].encode('utf-8')])
csv_out.close()
"""
for line in df:
    #writes a row and gets the fields from the json object
    #screen_name and followers/friends are found on the second level hence two get methods
    writer.writerow([line.get('created_at'),
                     line.get('text').encode('unicode_escape')]) #unicode escape to fix emoji issue
                #     line.get('user').get('screen_name'),
                #     line.get('user').get('followers_count'),
                #     line.get('user').get('friends_count'),
                #     line.get('retweet_count'),
            #         line.get('favorite_count')])
csv_out.close()
"""
