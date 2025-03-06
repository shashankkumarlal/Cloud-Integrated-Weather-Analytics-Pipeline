library(httr)
library(jsonlite)

# Define API URL
api_url <- "https://f2r1kaj839.execute-api.us-east-1.amazonaws.com/prod/weather"

# Fetch data from API
response <- GET(api_url)

# Convert JSON response to R list
weather_data <- fromJSON(content(response, "text"))

# Print the weather data
print(weather_data)
