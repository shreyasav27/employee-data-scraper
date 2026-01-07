import requests
import pandas as pd

URL = "https://api.slingacademy.com/v1/sample-data/files/employees.json"


def fetch_employee_data():
    try:
        response = requests.get(URL, timeout=10)

        if response.status_code != 200:
            print(f"API Error: {response.status_code}")
            return None

        data = response.json()
        df = pd.DataFrame(data)

        # Phone validation
        def validate_phone(phone):
            if isinstance(phone, str):
                return "Invalid Number"
            if "@" in phone:
                return "Invalid Number"
            return phone.strip()

        df["phone"] = df["phone"].apply(validate_phone)

        return df.to_dict(orient="records")

    except requests.exceptions.Timeout:
        print("Error: Request timed out")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

    return None


def main():
    data = fetch_employee_data()
    if not data:
        print("No data fetched")
        return

    df = pd.DataFrame(data)

    print(" Columns from API:", df.columns.tolist())

    # Full Name
    df["full_name"] = df["first_name"] + " " + df["last_name"]

    # Designation logic
    def get_designation(exp):
        if exp < 3:
            return "System Engineer"
        elif 3 <= exp <= 5:
            return "Data Engineer"
        elif 5 < exp <= 10:
            return "Senior Data Engineer"
        else:
            return "Lead"

    df["designation"] = df["years_of_experience"].apply(get_designation)

    # Data type conversions
    df["age"] = df["age"].astype(int)
    df["years_of_experience"] = df["years_of_experience"].astype(int)
    df["salary"] = df["salary"].astype(int)

    # Handle hire_date only if present
    if "hire_date" in df.columns:
        df["hire_date"] = pd.to_datetime(df["hire_date"]).dt.strftime("%Y-%m-%d")
    else:
        print("ℹ hire_date column not present – skipping")

    # Final columns
    final_columns = [
        "full_name",
        "email",
        "phone",
        "gender",
        "age",
        "job_title",
        "years_of_experience",
        "salary",
        "department",
        "designation"
    ]

    if "hire_date" in df.columns:
        final_columns.append("hire_date")

    final_df = df[final_columns]
    final_df.to_csv("clean_employee_data.csv", index=False)

    print(" Scraped successfully!!!")
    print(" Output file: clean_employee_data.csv")


if __name__ == "__main__":
    main()
