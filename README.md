# README.md

## Usage

To run the Celery worker and the beat schedule at the same time, open a terminal window and execute the following commands:

```bash
python -m celery -A tasks worker -l info --loglevel=info
python -m celery -A system_beat beat -l info
