# Django-Api

Initial Setop
```
Install python and django
Clone the Repository
Change Directory to myproject
Run the command -: python manage.py runserver

```

For Donation Data Use -:

```
const donationData = {
  name: 'John Doe',
  amount: 100,
  phone: '1234567890',
  email: 'johndoe@example.com',
  address: '123 Main St',
  pin_code: '12345',
  purpose: 'Charitable cause'
};

fetch('http://localhost:8000/api/donation/', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify(donationData),
})
.then(response => response.json())
.then(data => {
  console.log(data);
})
.catch(error => {
  console.error('Error:', error);
});

```

FOR REGISTRATION DATA USE -:
```
const registrationData = {
  name: 'John Doe',
  email: 'johndoe@example.com',
  phone: '1234567890',
  address: '123 Main St',
  dob: '1990-01-01',
  experience: '5 years'
};

fetch('http://localhost:8000/api/register/', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify(registrationData),
})
.then(response => response.json())
.then(data => {
  console.log(data);
})
.catch(error => {
  console.error('Error:', error);
});
```


FOR CONTACT US DATA USE -:
```
const contactData = {
  name: 'John Doe',
  email: 'johndoe@example.com',
  phone: '1234567890',
  message: 'Hello'
};

fetch('http://localhost:8000/api/contact-us/', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify(contactData),
})
.then(response => response.json())
.then(data => {
  console.log(data);
})
.catch(error => {
  console.error('Error:', error);
});

```
