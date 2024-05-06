from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options
import os
from pyspark.sql import SparkSession
from delta import configure_spark_with_delta_pip
import tempfile

# Set the download directory to the "music" subfolder within the current directory
download_directory = os.path.join(os.getcwd(), "music")
os.makedirs(download_directory, exist_ok=True)

# Set up Chrome options
chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": download_directory,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})

# Set up the Selenium WebDriver (e.g., Chrome)
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the website
driver.get("https://suno.com/me")


# Wait for the sign-in button to be clickable and click it
sign_in_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#__next > div > div > div > div > div.cl-main.🔒️.cl-internal-xk295g > div > button.cl-socialButtonsIconButton.cl-socialButtonsIconButton__discord.🔒️.cl-internal-855i1h"))
    )
sign_in_button.click()

# Wait for the username field to be visible and enter the username
#username: applebottom_12
username_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#uid_8"))
    )
username_field.send_keys("asfasfasfgasdfasgfsag@gmail.com")

# Find the password field and enter the password
password_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#uid_10"))
    )
password_field.send_keys("AppleBottom12")

# Find the password button and click it
password_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#app-mount > div.appAsidePanelWrapper__5e6e2 > div.notAppAsidePanel__95814 > div.app_b1f720 > div > div > div > div > form > div.centeringWrapper__5e247 > div > div.mainLoginContainer_f58870 > div.block__681fa.marginTop20__7e0ad > button.marginBottom8_ce1fb9.button__5573c.button__581d0.lookFilled__950dd.colorBrand__27d57.sizeLarge_b395a7.fullWidth_fdb23d.grow__4c8a4"))
    )
password_button.click()

# Wait for the page to load after signing in
WebDriverWait(driver, 10).until(
        EC.url_contains("https://suno.com/me")
    )

# Click on the specific song
three_dots = WebDriverWait(driver, 10).until(
     EC.element_to_be_clickable((By.LINK_TEXT, "Samba Kickoff"))
 )
three_dots.click()

# Play the song
play_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div.css-fhtuey > div.css-7p13yq > div > div > div > div.css-47b328 > div.chakra-stack.css-1e40a21 > div.chakra-stack.css-lw6smx > div.css-0 > button > span"))
    )
play_button.click()

time.sleep(3)

three_dots = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="More Actions"]'))
)
three_dots.click()

# Wait for the Download button to be clickable and click on it
download_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//div[@role="menuitem" and contains(text(), "Download")]'))
)
download_button.click()

# Wait for the Audio element to be clickable and click on it
audio_element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//div[@role="menuitem" and contains(text(), "Audio")]'))
)
audio_element.click()

time.sleep(3)

print("Successfully signed in!")

# Create a SparkSession with Delta Lake configuration
builder = SparkSession.builder.appName("SaveMP3ToDatabricks") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")

spark = configure_spark_with_delta_pip(builder).getOrCreate()

# Setting the Retrieving Director
retrieve_directory = os.path.join(download_directory, "Samba Kickoff.mp3")

# Read the downloaded MP3 file as binary
mp3_data = spark.sparkContext.binaryFiles(retrieve_directory).collect()[0][1]

# Create a DataFrame with the MP3 data
df = spark.createDataFrame([("Samba Kickoff.mp3", mp3_data,)], ["song_name", "mp3_data"])

# Save the DataFrame to a Databricks table
df.write.format("delta").mode("append").saveAsTable("mp3_table")

print("MP3 file saved to Databricks table.")

driver.quit()