import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('example.db')
c = conn.cursor()

# Create the supplier table
c.execute("""
CREATE TABLE Partners (
    ID INTEGER PRIMARY KEY,
    PartnerName TEXT NOT NULL,
    PartnerType TEXT NOT NULL,
    ContactPerson TEXT NOT NULL,
    ContactEmail TEXT NOT NULL,
    ContactPhone TEXT NOT NULL,
    Address TEXT NOT NULL,
    Website TEXT
);
""")

c.execute("""
INSERT INTO Partners (PartnerName, PartnerType, ContactPerson, ContactEmail, ContactPhone, Address, Website)
VALUES
    ('ABC Inc.', 'Business', 'John Doe', 'john.doe@abc.com', '123-456-7890', '123 Main St, Anytown, USA', 'www.abc.com,
    ('XYZ Corp.', 'Community', 'Jane Smith', 'jane.smith@xyz.org', '987-654-3210', '456 Oak St, Anytown, USA', 'www.xyz.org'),
    ('Acme Co.', 'Business', 'Bob Johnson', 'bob.johnson@acme.com', '555-555-5555', '789 Elm St, Anytown, USA', 'www.acme.com'),
    ('Community Foundation', 'Community', 'Sarah Lee', 'sarah.lee@cf.org', '111-222-3333', '321 Pine St, Anytown, USA', 'www.cf.org'),
    ('Local Chamber of Commerce', 'Community', 'Tom Smith', 'tom.smith@chamber.org', '444-555-6666', '654 Maple St, Anytown, USA', 'www.chamber.org'),
    ('Big Brothers Big Sisters', 'Community', 'Mary Johnson', 'mary.johnson@bbbs.org', '777-888-9999', '987 Cedar St, Anytown, USA', 'www.bbbs.org'),
    ('Anytown Rotary Club', 'Community', 'Joe Brown', 'joe.brown@rotary.org', '222-333-4444', '789 Oak St, Anytown, USA', 'www.rotary.org'),
    ('Anytown Kiwanis Club', 'Community', 'Susan Lee', 'susan.lee@kiwanis.org', '333-444-5555', '456 Pine St, Anytown, USA', 'www.kiwanis.org'),
    ('Anytown Lions Club', 'Community', 'David Smith', 'david.smith@lions.org', '444-555-6666', '123 Elm St, Anytown, USA', 'www.lions.org'),
    ('Anytown Women''s Club', 'Community', 'Linda Johnson', 'linda.johnson@womensclub.org', '555-666-7777', '321 Cedar St, Anytown, USA', 'www.womensclub.org'),
    ('Anytown Men''s Club', 'Community', 'Mike Brown', 'mike.brown@mensclub.org', '666-777-8888', '654 Pine St, Anytown, USA', 'www.mensclub.org'),
    ('Anytown Garden Club', 'Community', 'Karen Lee', 'karen.lee@gardenclub.org', '777-888-9999', '789 Cedar St, Anytown, USA', 'www.gardenclub.org'),
    ('Anytown Historical Society', 'Community', 'Bill Smith', 'bill.smith@historicalsociety.org', '888-999-0000', '456 Elm St, Anytown, USA', 'www.historicalsociety.org'),
    ('Anytown Arts Council', 'Community', 'Emily Johnson', 'emily.johnson@artscouncil.org', '111-222-3333', '123 Pine St, Anytown, USA', 'www.artscouncil.org'),
    ('Anytown Youth Sports', 'Community', 'Tim Brown', 'tim.brown@youthsports.org', '444-555-6666', '321 Oak St, Anytown, USA', 'www.youthsports.org'),
    ('Anytown High School', 'Education', 'Principal Smith', 'principal.smith@anytownschools.org', '555-666-7777', '654 Cedar St, Anytown, USA', 'www.anytownschools.org');
    """)

# Commit the changes and close the connection
conn.commit()
conn.close()