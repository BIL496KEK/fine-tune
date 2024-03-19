try:
    client.fine_tuning.jobs.create(
        model="gpt-3.5-turbo",
        training_file="file-eSQ3n7rQ0caKDp0OESFz2Pq7",
    )
except openai.APIConnectionError as e:
    print("The server could not be reached")
    print(e._cause_)  # an underlying Exception, likely raised within httpx.
except openai.RateLimitError as e:
    print("A 429 status code was received; we should back off a bit.")
except openai.APIStatusError as e:
    print("Another non-200-range status code was received")
    print(e.status_code)
    print(e.response)