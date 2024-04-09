import pyshorteners

pys = pyshorteners.Shortener()
short_url = pys.tinyurl.short('https://stackoverflow.com/questions/34418077/how-to-create-mysql-table-with-column-timestamp-default-current-date')

print(short_url)