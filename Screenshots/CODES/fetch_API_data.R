library(httr)
library(jsonlite)

# Define API URL
api_url <- "https://abcd1234.execute-api.us-east-1.amazonaws.com/weather"

# Fetch Data
response <- GET(api_url)
data <- fromJSON(content(response, "text"))

print(data)  # Check the data
