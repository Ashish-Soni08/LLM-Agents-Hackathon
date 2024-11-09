import os
import json
from collections import defaultdict
import logging

logging.basicConfig(level=logging.INFO)

def process_reviews(input_file, output_file):
    """
    Processes restaurant reviews from an input file and writes them to an output file in JSON format.

    Args:
        input_file (str): The path to the input file containing restaurant reviews.
        output_file (str): The path to the output file where the processed reviews will be saved.

    Returns:
        None

    The input file should contain reviews in the format:
        RestaurantName. Review text...

    The function reads the reviews, organizes them by restaurant name, and writes the resulting dictionary
    to the output file in JSON format. If the input file is not found, an error is logged. If there is an
    error writing to the output file, an error is logged.
    """
    try:
        with open(input_file, "r") as restaurant_reviews_dataset:
            reviews = restaurant_reviews_dataset.readlines()
            logging.info("Completed reading file")
    except FileNotFoundError:
        logging.error(f"File {input_file} not found.")
        return

    restaurant_dict = defaultdict(list)
    for review in reviews:
        restaurant_name, restaurant_review = review.split(".", 1)
        restaurant_name = restaurant_name.strip()
        restaurant_review = restaurant_review.strip()
        restaurant_dict[restaurant_name].append(restaurant_review)
    logging.info("Finished creating dict")

    if not os.path.exists(output_file):
        try:
            with open(output_file, "w") as fp:
                logging.info("Started writing dict to file")
                json.dump(restaurant_dict, fp)
                logging.info("Completed writing dict to file")
        except IOError as e:
            logging.error(f"Error writing to file {output_file}: {e}")

if __name__ == "__main__":
    process_reviews("restaurant-data.txt", "restaurant_review_dataset.txt")