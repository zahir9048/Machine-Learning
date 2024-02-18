import pandas as pd
from faker import Faker
import random

# Seed for reproducibility
random.seed(42)

# Load the existing data
file_path = r"D:\SSUET\8th Semester\Cryptography & Network Security (CE-408)\Project\Data Privacy Classifier\Data.csv"
df = pd.read_csv(file_path)


# Function to generate random data for a specific privacy level
def generate_random_data_for_privacy_level(num_rows, privacy_level):
    fake = Faker()
    data = []

    for _ in range(num_rows):
        name = fake.name()
        age = fake.random_int(min=18, max=60)
        email = fake.email() if random.choice([True, False]) else "-"
        medical_illness = fake.random_element(
            elements=("Hypertension", "Mental", "None", "Asthma", "False Alarm", "Headache")) if random.choice(
            [True, False]) else "-"

        # Generate ID card number as a random integer
        identity_card_number = fake.random_int(min=10000000, max=99999999) if random.choice([True, False]) else "-"

        phone_number = fake.phone_number() if random.choice([True, False]) else "-"
        address = fake.city() if random.choice([True, False]) else "-"
        has_email = 1 if email != "-" else 0
        has_id_card = 1 if identity_card_number != "-" else 0
        has_phone_number = 1 if phone_number != "-" else 0
        has_address = 1 if address != "-" else 0

        # Determine privacy level based on conditions
        if privacy_level == "High" and (has_id_card and has_address):
            data.append(
                [name, age, email, medical_illness, identity_card_number, phone_number, address, has_email, has_id_card,
                 has_phone_number, has_address, privacy_level])
        elif privacy_level == "Medium" and (has_id_card or has_address or has_email or has_phone_number):
            data.append(
                [name, age, email, medical_illness, identity_card_number, phone_number, address, has_email, has_id_card,
                 has_phone_number, has_address, privacy_level])
        elif privacy_level == "Low" and not (has_id_card or has_address or has_email or has_phone_number):
            data.append(
                [name, age, email, medical_illness, identity_card_number, phone_number, address, has_email, has_id_card,
                 has_phone_number, has_address, privacy_level])

    return data


# Generate 30 additional rows of random data for each privacy level
additional_rows_low = generate_random_data_for_privacy_level(30, "Low")
additional_rows_medium = generate_random_data_for_privacy_level(30, "Medium")
additional_rows_high = generate_random_data_for_privacy_level(30, "High")

# Combine the existing and new data
df_extended = pd.concat(
    [df, pd.DataFrame(additional_rows_low + additional_rows_medium + additional_rows_high, columns=df.columns)],
    ignore_index=True)

df_extended.to_csv(r"D:\SSUET\8th Semester\Cryptography & Network Security (CE-408)\Project\Data Privacy Classifier\Combined_Data.csv", index=False)
