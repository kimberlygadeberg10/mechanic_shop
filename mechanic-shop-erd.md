# Mechanic Shop ERD

## ERD Diagram

```mermaid
erDiagram
    CUSTOMERS ||--o{ VEHICLES : owns
    CUSTOMERS ||--o{ SERVICE_TICKETS : creates
    VEHICLES ||--o{ SERVICE_TICKETS : receives
    SERVICE_TICKETS ||--o{ SERVICE_MECHANICS : includes
    MECHANICS ||--o{ SERVICE_MECHANICS : works_on

    CUSTOMERS {
        int customer_id PK
        string first_name
        string last_name
        string phone
        string email
        string address
    }

    VEHICLES {
        int vehicle_id PK
        int customer_id FK
        string vin
        string make
        string model
        int year
        string license_plate
        string color
    }

    SERVICE_TICKETS {
        int ticket_id PK
        int customer_id FK
        int vehicle_id FK
        date date_opened
        date date_closed
        string service_description
        string problem_reported
        string status
        decimal total_cost
    }

    MECHANICS {
        int mechanic_id PK
        string first_name
        string last_name
        string email
        string phone
        string address
        decimal salary
    }

    SERVICE_MECHANICS {
        int ticket_id PK
        int mechanic_id PK
        decimal hours_worked
    }
```

## Relationships
- One customer can own many vehicles.
- One customer can have many service tickets.
- One vehicle can have many service tickets.
- One service ticket belongs to one customer.
- One service ticket belongs to one vehicle.
- One service ticket can involve many mechanics.
- One mechanic can work on many service tickets.
