import random
import logging
from web3 import Web3
import pandas as pd
import os

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler("check_and_trigger.log"), logging.StreamHandler()],
)

def main():
    try:
        # Connect to Ethereum node
        w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

        if not w3.is_connected():
            logging.error("Failed to connect to Ethereum network. Please check the node URL.")
            return

        logging.info("Connected to Ethereum network.")
        latest_block = w3.eth.block_number
        logging.info(f"Latest block number: {latest_block}")

        # Load dataset
        dataset_path = 'dataset_without_predictions.csv'
        if not os.path.exists(dataset_path):
            logging.error(f"Dataset not found at {dataset_path}.")
            return

        df = pd.read_csv(dataset_path)

        # Process blocks
        for block_num in range(1, latest_block + 1):
            block = w3.eth.get_block(block_num)
            logging.info(f"Processing block {block_num}...")

            # Randomized or algorithmic trigger
            trigger = random.choice([True, False])

            if trigger:
                # Fetch mitigation steps
                row = df.sample().iloc[0]
                mitigation = row.get('mitigation_steps', 'No mitigation steps found')
                logging.info(f"Block {block_num}: Triggered! Mitigation: {mitigation}")
            else:
                logging.info(f"Block {block_num}: No trigger.")

    except Exception as e:
        logging.error(f"Unexpected error: {e}", exc_info=True)

if __name__ == "__main__":
    main()
