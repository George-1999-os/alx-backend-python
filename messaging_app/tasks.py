cat > messaging_app/tasks.py <<EOL
from celery import shared_task

@shared_task
def generate_weekly_report():
    with open("/tmp/crm_report_log.txt", "a") as f:
        f.write("CRM weekly report generated.\n")
    return "Report generated"
EOL


