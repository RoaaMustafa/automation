from faker import Faker

fake = Faker('en_US')
# print( fake.phone_number())

content = ""

for _ in range(100):
    content += fake.paragraph()
    content += fake.email()
    content += fake.address()
    content += fake.phone_number()
    content += fake.word()

with open('automation/assest/potential-contacts.txt', 'w+') as file:
    file.write(content)

# import shutil

# shutil.copy('contacts.txt', 'contacts.txt.bak')