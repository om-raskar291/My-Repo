import tkinter as tk
from tkinter import messagebox
import smtplib

class MailApp:
    def __init__(self, master):
        self.master = master
        master.title("Mail Application")

        # create sender email widgets
        self.sender_email_label = tk.Label(master, text="Sender Email:")
        self.sender_email_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.sender_email_entry = tk.Entry(master, width=30)
        self.sender_email_entry.grid(row=0, column=1, padx=5, pady=5)

        # create sender password widgets
        self.sender_password_label = tk.Label(master, text="Password:")
        self.sender_password_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.sender_password_entry = tk.Entry(master, width=30, show="*")
        self.sender_password_entry.grid(row=1, column=1, padx=5, pady=5)

        # create recipient email widgets
        self.recipient_email_label = tk.Label(master, text="Recipient Email:")
        self.recipient_email_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.recipient_email_entry = tk.Entry(master, width=30)
        self.recipient_email_entry.grid(row=2, column=1, padx=5, pady=5)

        # create email subject widgets
        self.subject_label = tk.Label(master, text="Subject:")
        self.subject_label.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
        self.subject_entry = tk.Entry(master, width=30)
        self.subject_entry.grid(row=3, column=1, padx=5, pady=5)

        # create email message widgets
        self.message_label = tk.Label(master, text="Message:")
        self.message_label.grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)
        self.message_entry = tk.Text(master, width=30, height=10)
        self.message_entry.grid(row=4, column=1, padx=5, pady=5)

        # create send email button
        self.send_button = tk.Button(master, text="Send Email", command=self.send_email)
        self.send_button.grid(row=5, column=1, padx=5, pady=5)

    def send_email(self):
        # get user inputs
        sender_email = self.sender_email_entry.get()
        sender_password = self.sender_password_entry.get()
        recipient_email = self.recipient_email_entry.get()
        subject = self.subject_entry.get()
        message = self.message_entry.get("1.0", tk.END)

        try:
            # create SMTP server connection and send email
            smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
            smtp_server.ehlo()
            smtp_server.starttls()
            smtp_server.login(sender_email, sender_password)
            smtp_server.sendmail(sender_email, recipient_email, f"Subject: {subject}\n\n{message}")
            smtp_server.close()

            messagebox.showinfo("Success", "Email sent successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

# create and run the GUI
root = tk.Tk()
mail_app = MailApp(root)
root.mainloop()
