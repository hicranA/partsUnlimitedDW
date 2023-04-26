# partsUnlimitedDW - Data-Warehouse-Project
## Background information 
The topic I wish to explore for my data warehouse project is the management of Parts Unlimited's EV parts business. This topic was inspired by "The Unicorn Project," which describes the challenges and opportunities of digital transformation in a large organization. Specifically, I plan to focus on storing and analyzing data related to charging stations, EV product price lists, EV car information, and EV customer data, such as their geographic location, the model of the car they own, and location data.In this scnerio Parts Unlimited already sells EV parts, and my goal is to improve the organization's data management, reporting, and analysis capabilities related to this business.

## Project Summary:
The primary objective of this project is to create a concep data-warehouse project using slowly changing dimensional. 

**Project Objective**
The primary objective of this project is to create a concept data warehouse project using a slowly changing dimension approach. I will identify the business requirements by formulating specific business questions that the data warehouse will help answer. Based on these requirements, I will develop a consolidated ERD schema for the data warehouse.

I will focus on storing and analyzing data related to EV charging stations, product information, customer purchases, and geographic location. To accomplish this, I will use a slowly changing dimension approach to ensure that data is properly tracked over time. Specifically, I will use SCD Type 2 to track changes to the customer's location, SCD Type 3 to track changes to the EV product information, and SCD Type 1 to track changes to the charging station information.

Finally, I will use Tableau and Postgres SQL to create reports that will help the business make data-driven decisions based on the data stored in the data warehouse. By using a consolidated ERD schema and slowly changing dimensions, I will ensure that the data warehouse accurately reflects the business needs and can be used to provide valuable insights to the organization.

*** Road Map**
Planned project imporevements:
- ev charging station table: ev_charhing_station_id : this is a source code and might confuse the end user, I will remove this from my design 
