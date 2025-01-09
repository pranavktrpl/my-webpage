# Python code to clean tweets.txt and save only the tweet text
def clean_tweets(input_file, output_file):
    """
    Reads a file with tweets in the specified format, extracts only the tweet text, 
    and saves the cleaned text to a new file.
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
            tweet_texts = []
            for line in infile:
                # Check if the line starts with 'Tweet:', indicating it has the tweet text
                if line.startswith("Tweet:"):
                    # Extract the text after 'Tweet:' and clean any leading/trailing spaces
                    tweet_text = line[len("Tweet:"):].strip()
                    tweet_texts.append(tweet_text)
            
            # Write the cleaned tweets to the output file, one per line
            for text in tweet_texts:
                outfile.write(f"{text}\n")
        
        print(f"Cleaned tweets have been saved to '{output_file}'")
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Specify the input and output file names
input_filename = "tweets.txt"
output_filename = "cleaned_tweets.txt"

# Call the function to clean and save the tweets
clean_tweets(input_filename, output_filename)
