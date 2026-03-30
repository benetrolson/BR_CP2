import numpy as np
a = np.arange(15).reshape(3, 5)

print(a)

from faker import Faker

fake = Faker()

print(fake.name())
print(fake.address())
print(fake.bank_country())
