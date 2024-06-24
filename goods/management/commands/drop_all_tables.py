from django.core.management.base import BaseCommand
from django.db import connection


class Command(BaseCommand):
    """Удаление всех таблиц из БД."""

    help = "Drops all tables from the database"

    def handle(self, *args, **options):
        with connection.cursor() as cursor:
            cursor.execute(
                """
            DO $$ DECLARE
                r RECORD;
            BEGIN
                FOR r IN (SELECT tablename FROM pg_tables WHERE schemaname = current_schema()) LOOP
                    EXECUTE 'DROP TABLE IF EXISTS ' || quote_ident(r.tablename) || ' CASCADE';
                END LOOP;
            END $$;
            """
            )
        self.stdout.write(self.style.SUCCESS("Successfully dropped all tables"))
