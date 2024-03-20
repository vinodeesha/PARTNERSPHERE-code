import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('example.db')
c = conn.cursor()


c.execute("""
INSERT INTO Partners (PartnerName, PartnerType, ContactPerson, ContactEmail, ContactPhone, Address, Website)
VALUES
    ('Innovative Solutions Pvt. Ltd.', 'Business', 'Aarav Patel', 'aarav@example.com', '1234567890', '123 Main St, Mumbai, Maharashtra 400001', 'www.innovativesolutions.com'),
    ('Community Connect Foundation', 'Community', 'Aaradhya Sharma', 'aaradhya@example.com', '9876543210', '456 Elm St, New Delhi, Delhi 110001', 'www.communityconnect.org'),
    ('Education Elevation Academy', 'Education', 'Aarav Singh', 'aarav.singh@example.com', '4567890123', '789 Oak St, Bengaluru, Karnataka 560001', 'www.educationelevation.in'),
    ('Dynamic Business Ventures', 'Business', 'Advik Gupta', 'advik@example.com', '3216549870', '901 Pine St, Hyderabad, Telangana 500001', 'www.dynamicbusinessventures.com'),
    ('Global Harmony Foundation', 'Community', 'Aisha Khan', 'aisha.khan@example.com', '7890123456', '234 Maple St, Chennai, Tamil Nadu 600001', 'www.globalharmonyfoundation.org'),
    ('TechEd Solutions Pvt. Ltd.', 'Education', 'Akshara Mishra', 'akshara.mishra@example.com', '2109876543', '567 Birch St, Kolkata, West Bengal 700001', 'www.techedsolutions.in'),
    ('Business Brilliance Group', 'Business', 'Arjun Reddy', 'arjun@example.com', '5432109876', '876 Cedar St, Pune, Maharashtra 411001', 'www.businessbrilliancegroup.com'),
    ('Society Service Initiative', 'Community', 'Avani Sharma', 'avani.sharma@example.com', '4321098765', '543 Walnut St, Jaipur, Rajasthan 302001', 'www.societyservice.org'),
    ('Bright Future Academy', 'Education', 'Aayush Patel', 'aayush.patel@example.com', '2109876543', '789 Spruce St, Ahmedabad, Gujarat 380001', 'www.brightfutureacademy.in'),
    ('Innovative Business Solutions', 'Business', 'Amit Kumar', 'amit.kumar@example.com', '8765432109', '901 Pine St, Lucknow, Uttar Pradesh 226001', 'www.innovativebusinesssolutions.com');
    """)

# Commit the changes and close the connection
conn.commit()
conn.close()