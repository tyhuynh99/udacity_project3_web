import logging
import azure.functions as func
import psycopg2
import os
from datetime import datetime
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def main(msg: func.ServiceBusMessage):

    notification_id = msg.get_body().decode('utf-8')
    logging.info('Python ServiceBus queue trigger processed message: %s',notification_id)

    # TODO: Get connection to database
    database_name = os.getenv('POSTGRES_DB')
    username = os.getenv('POSTGRES_USER')
    pwd = os.getenv('POSTGRES_PW')
    url = os.getenv('POSTGRES_URL')
    
    conn = psycopg2.connect(database=database_name, user=username, password=pwd, host=url)
    logging.info("Connect to database success")

    try:
        # TODO: Get notification message and subject from database using the notification_id
        logging.info("Get notification message and subject from database using the notification_id")
        cur = conn.cursor()
        cur.execute("SELECT message, subject from notification WHERE id = {}".format(notification_id))
        notification = cur.fetchone()
        
        # TODO: Get attendees email and name
        logging.info("Get attendees email and name")
        cur.execute("SELECT email, first_name from attendee")
        attendees = cur.fetchall()
        
        # TODO: Loop through each attendee and send an email with a personalized subject
        logging.info("Loop through each attendee and send an email with a personalized subject")
        count = 0
        for attendee in attendees:
            subject = '{}: {}'.format(attendee[1], notification[1])
            send_email(attendee[0], subject, notification[0])
            count += 1
            
        # TODO: Update the notification table by setting the completed date and updating the status with the total number of attendees notified
        logging.info("Update the notification table by setting the completed date and updating the status with the total number of attendees notified")
        status = "Notified {} attendees".format(count)
        date = datetime.utcnow()
        cur.execute("UPDATE notification set status = \'{}\', completed_date = \'{}\' WHERE id = {}".format(status, date, notification_id))
        conn.commit()
        
    except (Exception, psycopg2.DatabaseError) as error:
        logging.error(error)
    finally:
        cur.close()
        conn.close()
        
        
def send_email(email, subject, body):
    if not os.getenv('SENDGRID_API_KEY'):
        message = Mail(
            from_email=os.getenv('ADMIN_EMAIL_ADDRESS'),
            to_emails=email,
            subject=subject,
            plain_text_content=body)
        
        sg = SendGridAPIClient(os.getenv('SENDGRID_API_KEY'))
        sg.send(message)