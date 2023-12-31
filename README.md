# Multinational Retail Data Centralization

## Table of Contents
- [Description](#description)
- [Key Features](#key-features)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [License](#license)

## Description
The Multinational Retail Data Centralization project aims to centralize sales data from various sources into a single, easily accessible database. This initiative is driven by the goal of making sales data more accessible and analyzable for the organization, fostering a more data-driven approach to decision-making.

### Project Goals
- Centralize sales data into a single database.
- Create a system that acts as a single source of truth for sales data.
- Provide up-to-date metrics for business analysis.

## Key Features

### 1. Data Extraction and Transformation
- **Data Extraction (data_extraction.py):** Extracts data from various sources, including RDS tables and S3, providing flexibility for integrating data from different formats.
- **Data Cleaning (data_cleaning.py):** Implements methods for cleaning and transforming data, ensuring consistency and reliability in the central dataset.
  
### 2. Database Connection (database_utils.py)
- **Database Connection Management:** Manages the connection to the centralized database using SQLAlchemy, allowing seamless integration with different database systems.

### 3. Centralized Database
- **Initialization (main.py):** Initializes components, including DataExtractor, DatabaseConnector, and DataCleaning, creating a foundation for centralized data processing.
- **Table Listing (database_utils.py):** Lists all tables in the centralized database, providing visibility into available data.

### 4. Business Metrics
- **Real-time Business Metrics (main.py):** Executes processes to extract and clean store data and process orders data, facilitating the generation of real-time business metrics.

### 5. YAML Configuration (database_utils.py)
- **Credentials Management:** Reads database connection credentials from a YAML file (`db_creds.yaml`), enhancing security and configurability.

## Installation
Before running the project, make sure you have the required dependencies installed.

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/your-repo.git
    ```

   Replace `your-username` and `your-repo` with your actual GitHub username and repository name.

2. **Navigate to the project directory:**
    ```bash
    cd your-repo
    ```

3. **Install dependencies:**
    You can use pip install to ensure you have the required dependencies installed. 

## Usage
1. Ensure that the necessary credentials are set up (refer to `database_utils.py` for more information on `db_creds.yaml`).
2. Run the `main.py` file to initialize the components, list tables, extract and clean store data, and process orders data.

    ```bash
    python main.py
    ```

3. Explore other files such as `data_extraction.py` and `data_cleaning.py` for more specific functionalities and examples.

## File Structure
- `main.py`: Entry point of the project, initializes components and performs data processing.
- `database_utils.py`: Manages the connection to the database, reads credentials from `db_creds.yaml`.
- `data_extraction.py`: Extracts data from various sources, including RDS tables and S3.
- `data_cleaning.py`: Implements data cleaning and transformation methods.
- `db_creds.yaml`: YAML file containing database connection credentials.


## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

