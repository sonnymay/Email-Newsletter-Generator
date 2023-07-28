# Email Newsletter Generator

This project is a simple email newsletter generator built in Python. It uses Python's SMTP and MIME libraries to send formatted emails. This can be used to create and send a simple email newsletter.

## Installation and Setup

1. Clone this repository to your local machine:

```bash
git clone https://github.com/sonnymay/email-newsletter-generator.git
cd email-newsletter-generator
```

2. (Optional) It's suggested to create a virtual environment to keep the project and its dependencies isolated:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install the necessary dependencies:

```bash
pip install -r requirements.txt
```

## Usage

To send an email, you will need to update the `sender_email`, `receiver_email`, and `password` variables in the `send_email` function with your email credentials. The `subject` and `body` of the email can also be customized to your liking. 

In the main function, call the `send_email` function with the correct parameters:

```python
subject = "Your Subject"
body = "Your newsletter content"
sender_email = "your_email@gmail.com"
receiver_email = "receiver_email@gmail.com"
password = "your_password"

send_email(subject, body, sender_email, receiver_email, password)
```

Then run the Python script:

```bash
python main.py
```

Please remember that in order to enable sending mail from a gmail account, you have to allow less secure apps from this [link](https://myaccount.google.com/lesssecureapps).

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
