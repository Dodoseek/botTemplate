from django.core.management.base import BaseCommand, CommandError

import asyncio

from ChatBot import main


class Command(BaseCommand):
    help = 'RUN COMMAND: python manage.py runbot'

    def handle(self, *args, **options):
            asyncio.run(main())
