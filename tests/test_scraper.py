import unittest
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class TestScraping(unittest.TestCase):

    def test_env_variables_exist(self):
        """Check if required environment variables are loaded"""
        self.assertIsNotNone(os.getenv("TEXT_DATA_PATH"), "TEXT_DATA_PATH is not set in .env")
        self.assertIsNotNone(os.getenv("IMAGE_FOLDER"), "IMAGE_FOLDER is not set in .env")

    def test_text_file_exists_and_not_empty(self):
        """Check if the text data file exists and is not empty"""
        text_file = os.getenv("TEXT_DATA_PATH")
        self.assertTrue(os.path.exists(text_file), "Text data file does not exist")
        self.assertGreater(os.path.getsize(text_file), 0, "Text data file is empty")

    
if __name__ == "__main__":
    unittest.main()
