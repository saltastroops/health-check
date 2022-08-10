import docker
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import Optional

RUNNING = "running"
containers = [
    os.environ["WEB_MANAGER_CONTAINER_NAME"],
    os.environ["SALT_API_CONTAINER_NAME"]
]


def is_container_running(container_name: str) -> Optional[bool]:
    """
    Verify the status of a container by its name

    :return: boolean or None
    """

    # Connect to Docker using the default socket or the configuration
    # in your environment
    docker_client = docker.from_env()

    try:
        container = docker_client.containers.get(container_name)
    except docker.errors.NotFound as exc:
        print(f"Check container name!\n{exc.explanation}")
    else:
        container_state = container.attrs["State"]
        return container_state["Status"] == RUNNING


def generate_message() -> MIMEMultipart:
    plain_body = """
Hello Team.

    """
    html_body = """
<html>
  <head></head>
  <body>
    <p>Hello Team.</p>
    """
    for container_name in containers:

        if is_container_running(container_name):
            plain_body += f"""
{container_name} is fine.

            """
            html_body += f"""
        <p>{container_name} is fine</p>
"""
        else:
            plain_body += f"""
{container_name} is down.

"""
            html_body += f"""
        <p>{container_name} is down.</p>
"""
    plain_body += """
Cheers, Web Manager Health check.
    """
    html_body += """
        <p>Cheers, Web Manager Health check.</p>
    </body>
<html>
    """
    message = MIMEMultipart("alternative")

    message["Subject"] = "Web Manager Health Check."
    message["To"] = os.environ["TO_EMAIL"]
    message["From"] = f"SALT Team <{os.environ['FROM_EMAIL']}>"
    message.attach(MIMEText(plain_body, "plain"))
    message.attach(MIMEText(html_body, "html"))
    return message


def send_email(message: MIMEMultipart) -> None:
    smtp_obj = smtplib.SMTP(os.environ["SMTP_SERVER"])
    smtp_obj.sendmail(
        msg=message.as_string(),
        from_addr=os.environ["FROM_EMAIL"],
        to_addrs=[os.environ["TO_EMAIL"]]
    )


if __name__ == "__main__":
    for cn in containers:
        if not is_container_running(cn):
            msg = generate_message()
            send_email(msg)
