
fields = ["temperature", "humidity"]

timesteps = ["1h"]

start_time = "nowMinus30d"

end_time = "nowMinus15d"

url = f"https://api.tomorrow.io/v4/historical?apikey={API_KEY}"

payload = {
    "location": location,
    "fields": fields,
    "timesteps": timesteps,
    "startTime": start_time,
    "endTime": end_time,
}
headers = {
    "accept": "application/json",
    "Accept-Encoding": "gzip",
    "content-type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

if (response.status_code == 200):
    historical_weather_json = response.json()
    historical_weather_timelines = historical_weather_json['data']['timelines']
    
    timeline = historical_weather_timelines[0]
    title = f"historical_temperature_and_humidity_data_from_{timeline['startTime']}_to_{timeline['endTime']}_in_{timeline['timestep']}_steps-{datetime.datetime.now()}.csv"     
    historical_weather_df = pd.DataFrame(timeline['intervals'])
    historical_weather_df = pd.concat([historical_weather_df.drop(['values'], axis=1), historical_weather_df['values'].apply(pd.Series)], axis=1)
    historical_weather_df.to_csv(title, index=False)
    print(historical_weather_df)
else:
    print(response.status_code, response.reason)