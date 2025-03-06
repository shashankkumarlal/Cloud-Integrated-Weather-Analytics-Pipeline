# Load necessary libraries
library(httr)
library(jsonlite)
library(aws.s3)

# API URL (replace with your actual API)
api_url <- "https://f2r1kaj839.execute-api.us-east-1.amazonaws.com/....yourURL"

# Fetch data
response <- GET(api_url)
weather_data <- fromJSON(content(response, "text"))

# Convert to JSON & Save Locally
weather_json <- jsonlite::toJSON(weather_data, auto_unbox = TRUE)
write(weather_json, file = "weather_data.json")

# Upload to S3
Sys.setenv(AWS_SHARED_CREDENTIALS_FILE = "C:/Users/USERNAME/Downloads/.aws/credentials")
Sys.setenv(AWS_PROFILE = "default")

put_object(
    file = "weather_data.json",
    object = paste0("weather_", Sys.Date(), ".json"),  # Timestamped file name
    bucket = "shash-weather-data-bucket"
)

print("Weather data uploaded successfully!")
